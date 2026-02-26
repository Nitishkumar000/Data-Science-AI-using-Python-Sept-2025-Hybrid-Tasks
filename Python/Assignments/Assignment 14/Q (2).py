#WAP to remove the intersection of a second set with a first set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

set1 = set1 - (set1 & set2)
print("After removing intersection:", set1)
