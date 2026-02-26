#1. Develop a memoization decorator that caches the results of function
#calls and returns the cached result when the same inputs occur again.
#This can greatly improve the performance of recursive or
#computationally intensive functions.
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(10):
    print(fibonacci(i))

    