# 1: Find all of the numbers from 1–1000 that are divisible by 8
a=1
b=1000
for num in range(a,b+1):
    if num % 8 == 0:
        print(num)  
     