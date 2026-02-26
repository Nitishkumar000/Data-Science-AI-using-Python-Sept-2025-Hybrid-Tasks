# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
s = input("Enter string: ")

# character count
char_count = 0
for _ in s:
    char_count += 1

# word count
words = s.split()
word_count = len(words)

print("Words =", word_count)
print("Characters =", char_count)
