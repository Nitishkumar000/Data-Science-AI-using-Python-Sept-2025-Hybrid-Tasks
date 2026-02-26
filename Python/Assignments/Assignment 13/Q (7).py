# Program to remove a given key from a dictionary

d = {"a": 1, "b": 2, "c": 3}
key = input("Enter key to remove: ")

if key in d:                
    d.pop(key)              
    print("Updated dictionary:", d)
else:
    print("Key not found")
