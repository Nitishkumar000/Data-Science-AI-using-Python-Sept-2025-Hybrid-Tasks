import threading

total_sum = 0
lock = threading.Lock()

def sum_of_squares(start, end):
    global total_sum
    local_sum = 0
    for i in range(start, end + 1):
        local_sum += i * i

    with lock:
        total_sum += local_sum

threads = []

ranges = [(1, 25), (26, 50), (51, 75), (76, 100)]

for r in ranges:
    t = threading.Thread(target=sum_of_squares, args=r)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Total sum of squares:", total_sum)
