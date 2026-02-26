import re

def word_count(text):
    words = re.findall(r'\b\w+\b', text.lower())
    count = {}

    for word in words:
        count[word] = count.get(word, 0) + 1

    return count

text = "Python is easy and Python is powerful"
print(word_count(text))
