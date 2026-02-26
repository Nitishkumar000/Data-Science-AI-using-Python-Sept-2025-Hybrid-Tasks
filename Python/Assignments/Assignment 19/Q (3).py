#1. We want to generate Fibonacci numbers up to a certain limit.
#Instead of computing and storing the entire sequence in memory,
#create generator to yield Fibonacci numbers one by one,
#conserving memory and allowing for easy iteration.
def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b 
for fib in fibonacci_generator(10):
    print(fib)