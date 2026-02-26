import threading
import time
import random

buffer = []
buffer_size = 5

lock = threading.Condition()

def producer(name):
    while True:
        item = random.randint(1, 100)
        with lock:
            while len(buffer) == buffer_size:
                lock.wait()
            buffer.append(item)
            print(f"{name} produced {item} | Buffer: {buffer}")
            lock.notify()
        time.sleep(1)

def consumer(name):
    while True:
        with lock:
            while not buffer:
                lock.wait()
            item = buffer.pop(0)
            print(f"{name} consumed {item} | Buffer: {buffer}")
            lock.notify()
        time.sleep(1)

p1 = threading.Thread(target=producer, args=("Producer-1",))
p2 = threading.Thread(target=producer, args=("Producer-2",))
c1 = threading.Thread(target=consumer, args=("Consumer-1",))
c2 = threading.Thread(target=consumer, args=("Consumer-2",))

p1.start()
p2.start()
c1.start()
c2.start()
