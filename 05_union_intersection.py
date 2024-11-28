# Union of two sets (combines all unique elements from both sets)
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8, 9}
result = set1.union(set2)
print(result, type(result))

# Intersection of two sets (common elements between both sets)
result = set1.intersection(set2)
print(result, type(result))

# Difference between two sets (elements in set1 but not in set2)
result = set1.difference(set2)
print(result, type(result))

# Symmetric difference between two sets (elements in either set1 or set2, but not both)
result = set1.symmetric_difference(set2)
print(result, type(result))

# Checking if set1 is a subset of set2 (if all elements of set1 are in set2)
result = set1.issubset(set2)
print(result, type(result))

# Checking if set1 is a superset of set2 (if all elements of set2 are in set1)
result = set1.issuperset(set2)
print(result, type(result))

# Checking if two sets are disjoint (if there are no common elements between them)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result, type(result))