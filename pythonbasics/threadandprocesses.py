from threading import Thread
import time

from multiprocessing import Process

result = {}
def calc(n):
    time.sleep(1)
    result[n] = n * n
    print(result)

t1 = Thread(target=calc, args={3})
t2 = Thread(target=calc, args={5})


t1.start()
t2.start()
t1.join()
t2.join()

print(result)


p1 = Process(target=calc, args={6})
p2 = Process(target=calc, args={8})


p1.start()
p2.start()
p1.join()
p2.join()

print(result)


