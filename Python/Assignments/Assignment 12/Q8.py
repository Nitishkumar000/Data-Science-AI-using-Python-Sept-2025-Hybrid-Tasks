#8 .Python Program to Remove the Characters of Odd Index Values in a String
s = input("Enter string: ")
new_s = ""

for i in range(len(s)):
    if i % 2 == 0:  # keep even index
        new_s += s[i]

print(new_s)
