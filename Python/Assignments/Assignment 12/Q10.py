#10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# find lengths manually
l1 = 0
for _ in s1:
    l1 += 1

l2 = 0
for _ in s2:
    l2 += 1

if l1 > l2:
    print("Larger string:", s1)
else:
    print("Larger string:", s2)
