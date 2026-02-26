# 3 Program to check if a given key exists in a dictionary

d = {"name": "John", "age": 25, "city": "Pune"}
key = input("Enter key to search: ")

if key in d:                
    print("Key exists in dictionary")
else:
    print("Key does not exist")
