#12. Python Program to count number of lowercase characters in a string.
s = input("Enter string: ")
count = 0

for ch in s:
    if 'a' <= ch <= 'z':
        count += 1

print("Lowercase letters =", count)
