#Write a Python program to find the longest common prefix of all strings. Use the Python set.

def longest_common_prefix(strings):
    if not strings:
        return ""

    # Find the minimum length string in the list
    min_length = min(len(s) for s in strings)

    # Create a set of all prefixes of the minimum length
    prefixes = set()
    for s in strings:
        prefixes.add(s[:min_length])

    # Find the longest common prefix
    common_prefix = ""
    for i in range(min_length, 0, -1):
        prefix = strings[0][:i]
        if all(s.startswith(prefix) for s in strings):
            common_prefix = prefix
            break

    return common_prefix

strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print("Longest common prefix:", result)