#5. Python Program to Count the Number of Vowels in a String
s = input("Enter string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Vowel count =", count)
