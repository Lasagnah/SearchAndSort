import SearchClass, SortClass, random
import time

Pool = []
for i in range(10000):
    Pool.append(random.randint(1,150000))
# print(len(Pool))
Target = random.randint(1,150000)

# Linear Search
PoolUse = Pool.copy()
start_time = time.time()
print(SearchClass.linear(PoolUse, Target))
print("--- Linear search in %s seconds ---" % (time.time() - start_time))
# Binary Search
# Sort first
PoolUse = Pool.copy()
PoolUse.sort()
start_time = time.time()
print(SearchClass.binary(PoolUse, Target))
print("--- Binary search in %s seconds ---" % (time.time() - start_time))
# Min/Max
PoolUse = Pool.copy()
start_time = time.time()
print(SearchClass.min(PoolUse))
print("--- Min search in %s seconds ---" % (time.time() - start_time))
PoolUse = Pool.copy()
start_time = time.time()
print(SearchClass.max(PoolUse))
print("--- Max search in %s seconds ---" % (time.time() - start_time))
# Find distinct
PoolUse = Pool.copy()
start_time = time.time()
print(SearchClass.distinct(PoolUse))
print("--- Distinct in %s seconds ---" % (time.time() - start_time))
# Selection Sort
PoolUse = Pool.copy()
start_time = time.time()
print(SortClass.isSorted(SortClass.selection(PoolUse)))
print("--- Selection sort in %s seconds ---" % (time.time() - start_time))
# Insertion Sort
PoolUse = Pool.copy()
start_time = time.time()
print(SortClass.isSorted(SortClass.insertion(PoolUse)))
print("--- Insertion sort in %s seconds ---" % (time.time() - start_time))
# Bubble Sort
PoolUse = Pool.copy()
start_time = time.time()
print(SortClass.isSorted(SortClass.bubble(PoolUse)))
print("--- Bubble sort in %s seconds ---" % (time.time() - start_time))
# Merge Sort
PoolUse = Pool.copy()
start_time = time.time()
print(SortClass.isSorted(SortClass.merge(PoolUse)))
print("--- Merge sort in %s seconds ---" % (time.time() - start_time))