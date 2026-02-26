#use a dictionary comprehension to count length of each word  in a given string
input=str (input("Enter a string: "))
count=0
word_length={word:len(word) for word in input.split()}
print("Length of each word in the given string is: ",word_length)