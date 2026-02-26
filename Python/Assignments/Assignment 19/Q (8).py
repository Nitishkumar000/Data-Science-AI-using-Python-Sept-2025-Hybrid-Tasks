#4 : Remove all the vowels from a string
input=str (input("Enter a string: "))
count=0
for char in input:
    if char in 'aeiouAEIOU':
        input = input.replace(char, "")
print("String after removing vowels:", input)