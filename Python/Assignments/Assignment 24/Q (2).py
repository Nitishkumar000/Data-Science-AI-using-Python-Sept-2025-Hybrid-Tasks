import threading

lock = threading.Condition()
number = 1

def print_odd():
    global number
    while number <= 10:
        with lock:
            if number % 2 == 1:
                print("Odd:", number)
                number += 1
                lock.notify()
            else:
                lock.wait()

def print_even():
    global number
    while number <= 10:
        with lock:
            if number % 2 == 0:
                print("Even:", number)
                number += 1
                lock.notify()
            else:
                lock.wait()

t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

t1.start()
t2.start()

t1.join()
t2.join()
