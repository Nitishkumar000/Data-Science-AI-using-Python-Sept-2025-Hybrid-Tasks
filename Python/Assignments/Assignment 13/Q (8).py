# Program to count the frequency of each word in a string using a dictionary

s = input("Enter a sentence: ")
words = s.split()           

freq = {}                   
for w in words:
    if w in freq:           
        freq[w] += 1
    else:                   
        freq[w] = 1

print("Word frequency:", freq)
