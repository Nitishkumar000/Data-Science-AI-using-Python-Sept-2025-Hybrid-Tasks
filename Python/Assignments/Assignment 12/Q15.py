# 15 Python Program to find larger string without using built-in functions.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

l1 = 0
for _ in s1:
    l1 += 1

l2 = 0
for _ in s2:
    l2 += 1

if l1 > l2:
    print(s1)
else:
    print(s2)
