#4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged
s = input("Enter string: ")
new_s = s[-1] + s[1:-1] + s[0]
print(new_s)
