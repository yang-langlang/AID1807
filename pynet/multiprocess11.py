# from multiprocessing import Process
# from time import sleep

# def fun():
#     sleep(3)
#     print("子进程事件")

# p = Process(target = fun)

# p.start()

# sleep(1)
# print("这是父进程")

# p.join()

from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), "_______", os.getpid())

def th2():
    sleep(5)
    print("睡觉")
    print(os.getppid(), "_______", os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(), "_______", os.getpid())

things = [th1, th2, th3]
p1 = []

for th in things:
    p = Process(target=th)
    p.start()
    p1.append(p)

for i in p1:
    i.join()
