#Python Program to Remove the nth Index Character from a Non-Empty String
s = input("Enter string: ")
n = int(input("Enter index to remove: "))

new_s = s[:n] + s[n+1:]

print(new_s)
