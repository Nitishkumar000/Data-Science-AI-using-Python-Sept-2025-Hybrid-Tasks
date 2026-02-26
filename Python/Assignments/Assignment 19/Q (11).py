#Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit.
result = [num for num in range(1, 1001) if any(num % i == 0 for i in range(1, 10))]
print(result)
