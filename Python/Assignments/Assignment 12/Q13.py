#13. Python Program to count number of digits and letters in a string.
s = input("Enter string: ")

digits = 0
letters = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1

print("Digits =", digits)
print("Letters =", letters)
