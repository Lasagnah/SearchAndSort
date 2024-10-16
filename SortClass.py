
def selection(list):
    n = len(list)
    
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        
        # Iterate through the unsorted part of the array
        for j in range(i + 1, n):
            if list[j] < list[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        list[i], list[min_index] = list[min_index], list[i]
    
    return list
    
def insertion(list):
    # Traverse through 1 to len(list)
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        
        # Place key at its correct position
        list[j + 1] = key
    
    return list

def bubble(list):
    n = len(list)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to detect any swap
        swapped = False
        
        # Last i elements are already sorted, so we can skip them
        for j in range(0, n - i - 1):
            # If the element found is greater than the next element
            if list[j] > list[j + 1]:
                # Swap them
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        
    # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    
    return list

def merge(list):
    # Base Case
    if len(list) <= 1:
        return list

    # Find the middle to divide and conquer
    mid = len(list) // 2
    # Divide
    leftHalf = list[:mid]
    rightHalf = list[mid:]

    # Conquer
    sortedLeft = merge(leftHalf)
    sortedRight = merge(rightHalf)

    return mergeSort(sortedLeft, sortedRight)

def mergeSort(left, right):
    result = []
    i = j = 0

    # Merge the two lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def isSorted(list):
    sortedl = sorted(list)
    if list == sortedl:
        return True
    else:
        return False