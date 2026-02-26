#5 : find the number of words with less than 5 letters in a string
input=str(input("Enter a sentence: ")) 
count=0
input=input.split()
for word in input:
    if len(word) < 5:
        count+=1
print("Number of words with less than 5 letters:", count)