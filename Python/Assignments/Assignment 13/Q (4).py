# Program to generate a dictionary of the form (x : x*x)
# for numbers between 1 and n

n = int(input("Enter value of n: "))
d = {}

for x in range(1, n + 1):   
    d[x] = x * x            

print("Generated dictionary:", d)
