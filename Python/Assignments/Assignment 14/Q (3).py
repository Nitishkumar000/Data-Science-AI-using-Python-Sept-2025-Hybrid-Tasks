#WAP program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
strings = ["apple banana apple", "banana orange apple"]

words = []
for s in strings:
    words.extend(s.split())

unique_words = set(words)

for word in unique_words:
    print(word, ":", words.count(word))
