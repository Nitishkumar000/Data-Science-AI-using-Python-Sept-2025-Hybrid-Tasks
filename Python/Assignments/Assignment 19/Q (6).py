#3 :find the number of spaces in a string
a=str(input("enter a string:"))
print("the given string is :",a)
count=0
for i in a:
    if i==' ':
        count+=1
print("the number of spaces in the given string is:",count)