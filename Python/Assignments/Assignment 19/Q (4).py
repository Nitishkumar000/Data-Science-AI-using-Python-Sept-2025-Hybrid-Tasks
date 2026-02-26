# 2  : find all numbers from 1-1000 that have a 6 in them
a=1
b=1000
for num in range(a,b+1):
    if '6' in str(num):
        print(num)
