#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
def find_pairs(numbers, target_sum):
    seen = set()
    pairs = set()

    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    return pairs

numbers = [1, 2, 3, 4, 5]
target_sum = 6
result = find_pairs(numbers, target_sum)
print("Pairs with sum", target_sum, ":", result)