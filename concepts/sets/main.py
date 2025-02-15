# Sets - an unordered collection of elements which only contain unique elements

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union - combines all elements from both sets, without duplicates
union = set_a.union(set_b)
print(union)

# Intersection - returns elements that are common to both sets
intersection = set_a.intersection(set_b)
print(intersection)

# Intersection Update - similar to intersection but modifies the original set directly
set_a.intersection_update(set_b)
print(set_a)

# Adding an element to the set - unlike lists, add function adds the element to the set (position is not guaranteed)
set_b.add(34)
print(set_b)

# Symmetric Difference - elements in either set but not in both sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.symmetric_difference(s2))

# Symmetric Difference Update - similar to symmetric difference but directly modifies the original set
s1.symmetric_difference_update(s2)
print(s1)

# Difference - returns the difference between the set and the other set
s1 = {1, 2, 3}
s2 = {3, 4}
print(s1.difference(s2))

# Difference Update - similar to difference but directly modifies the original set instead of creating a new one
s1.difference_update(s2)
print(s1)

# issubset - checks whether the given set is a subset of the other set or not
print(s2.issubset(s1))

# issuperset - checks whether set A contains all the elements of set B or not
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4}
print(s1.issuperset(s2))

# isdisjoint - checks whether there are no common elements between the sets
print(s1.isdisjoint(s2))

# Merge two sets - updates set s1 with elements from set s2
s1.update(s2)
print(s1)
