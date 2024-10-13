import SearchClass, SortClass, random

Pool = []
for i in range(50000):
    Pool.append(random.randint(1,100000))
# print(len(Pool))
Target = random.randint(1,100000)

# Linear Search
PoolUse = Pool.copy()
SearchClass.linear(PoolUse, Target)
# Binary Search
# Sort first
PoolUse = Pool.copy()
PoolUse.sort()
print(SearchClass.binary(PoolUse, Target))
# Min/Max
PoolUse = Pool.copy()
print(SearchClass.min(PoolUse))
PoolUse = Pool.copy()
print(SearchClass.max(PoolUse))
# Find distinct
PoolUse = Pool.copy()
print(SearchClass.distinct(PoolUse))
# Selection Sort
PoolUse = Pool.copy()

# Insertion Sort
PoolUse = Pool.copy()

# Bubble Sort
PoolUse = Pool.copy()

# Merge Sort
PoolUse = Pool.copy()
