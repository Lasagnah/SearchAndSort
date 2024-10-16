
def linear(list, target):
# Returns true if the target is in the list
# Returns false if the target is not in the list
# Loops through the list to find the target
    for element in list:
        if element == target:
            return True
    return False    
    
def binary(list, target):
# Returns true if the target is in the list
# Returns false if the target is not in the list
    left, right = 0, len(list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Check if the target is present at the middle of the list
        if list[mid] == target:
            return True
        # If target is greater, ignore the left half
        elif list[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    # Target was not found
    return False

def min(list):
# Returns the lowest number in the list
# Loops through the list and compares it to the current lowest
    m = 100000
    for element in list:
        if element < m:
            m = element
    return m
    
def max(list):
# Returns the greatest number in the list
# Loops through the list and compares it to the current greatest
    m = 0
    for element in list:
        if element > m:
            m = element
    return m
    
def distinct(list):
# Creates a set of elements that we have already went through
# Checks to see if the element is in the set
# If it is, add it to set
    s = set()
    l = []
    for element in list:
        if element in s:
            l.append(element)
        else:
            s.add(element)
    if len(l) == 0:
        return True
    else:
        return l
        
    
