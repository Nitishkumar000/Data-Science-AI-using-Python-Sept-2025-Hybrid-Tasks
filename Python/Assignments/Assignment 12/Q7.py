#7. Python Program to Calculate the Length of a String Without Using a Library Function
s = input("Enter string: ")
count = 0

for _ in s:
    count += 1

print("Length =", count)
