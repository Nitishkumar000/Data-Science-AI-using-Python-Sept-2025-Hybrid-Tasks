#9. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
from itertools import combinations

def find_combinations(numbers, target):
    combinations_list = []
    for combo in combinations(numbers, 3):
        if sum(combo) == target:
            combinations_list.append(combo)
    return combinations_list

numbers = [1, 2, 3, 4, 5, 6]
target = 10
result = find_combinations(numbers, target)
print("Combinations that sum to target:", result)
