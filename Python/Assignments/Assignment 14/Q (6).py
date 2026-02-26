#Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

def find_max_product(numbers):
    if len(numbers) < 2:
        return None

    max_product = float('-inf')
    max_pair = None

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]
            if product > max_product:
                max_product = product
                max_pair = (numbers[i], numbers[j])

    return max_pair

numbers = [1, 2, 3, 4, 5]
result = find_max_product(numbers)
print("Pair with maximum product:", result)