#Implement a generator function that yields palindrome numbers.
#Palindromes are numbers that read the same backward as forward
#(e.g., 121, 1331). Generate palindromes lazily and infinitely.
def is_palindrome(num):
    return str(num) == str(num)[::-1]
def palindrome_generator():
    num = 0
    while True:
        if is_palindrome(num):
            yield num
        num += 1
pal_gen = palindrome_generator()
for _ in range(20):
    print(next(pal_gen))