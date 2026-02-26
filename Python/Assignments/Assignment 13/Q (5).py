# 5 Program to sum all the items in a dictionary

d = {"a": 10, "b": 20, "c": 30}
total = 0

for value in d.values():    
    total += value          

print("Sum of dictionary items:", total)
