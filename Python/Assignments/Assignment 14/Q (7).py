#Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Missing in second set:", set1 - set2)
print("Missing in first set:", set2 - set1)
