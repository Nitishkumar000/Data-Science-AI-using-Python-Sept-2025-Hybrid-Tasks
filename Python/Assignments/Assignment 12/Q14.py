# 14. Python Program to count the occurrences of ach word in a string.
s = input("Enter string: ")
words = s.split()
count = {}

for w in words:
    if w in count:
        count[w] += 1
    else:
        count[w] = 1

print(count)
