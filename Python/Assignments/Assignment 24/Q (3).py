import threading
import time

def lowercase():
    for c in range(ord('a'), ord('z') + 1):
        print(chr(c), end=" ")
        time.sleep(0.1)

def uppercase():
    for c in range(ord('A'), ord('Z') + 1):
        print(chr(c), end=" ")
        time.sleep(0.1)

t1 = threading.Thread(target=lowercase)
t2 = threading.Thread(target=uppercase)

t1.start()
t2.start()

t1.join()
t2.join()
