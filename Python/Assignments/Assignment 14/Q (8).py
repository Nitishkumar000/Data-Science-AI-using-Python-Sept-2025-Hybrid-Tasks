#8. Write a Python program to find all the anagrams and group them together from a given list of strings.
from collections import defaultdict 
def group_anagrams(strings):
    anagrams = defaultdict(list)

    for s in strings:
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)

    return list(anagrams.values())
strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strings)
print("Grouped anagrams:", result)
