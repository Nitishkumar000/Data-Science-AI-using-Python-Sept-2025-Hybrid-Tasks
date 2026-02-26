# 6  Program to multiply all the items in a dictionary

d = {"a": 2, "b": 3, "c": 4}
product = 1

for value in d.values():    
    product *= value        
print("Product of dictionary items:", product)
