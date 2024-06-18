import time
from threading import Thread

def perebor_1():
    spisok_1 = list(range(1, 11))
    for elem in spisok_1:
        print(elem)
        time.sleep(1)

def perebor_2():
    spisok_2 = [chr(x) for x in range(ord('a'), ord('j') + 1)]
    for elem in spisok_2:
        print(elem)
        time.sleep(1)

thread_1 = Thread(target=perebor_1)
thread_2 = Thread(target=perebor_2)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()