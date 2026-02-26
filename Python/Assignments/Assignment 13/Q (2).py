#2  Program to concatenate two dictionaries into one

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d3 = d1.copy()              
d3.update(d2)               

print("Concatenated dictionary:", d3)
