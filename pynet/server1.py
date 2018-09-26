# from socket import *
# import os, sys

# def do_child(s, addr):
#     while True:
#         msg = input("管理员消息:")
#         msg = "C 管理员" + msg
#         s.sendto(msg.encode(), addr)

# def do_parent(s):
#     user = {}

#     while True:
#         msg, addr = s.recvfrom(1024)
#         msgList = msg.decode().split(' ')

#         if msgList[0] == 'L':
#             do_login(s, user, msgList[1], addr)
#         elif msgList[0] =='C':
#             do_chat(s, user, msgList[1], \
#                 ' '.join(msgList[2:]))
#         elif msgList[0] == 'Q':
#             do_quit(s, user, msgList[1])

# def do_login(s, user, name, addr):
#     if (name in user) or name == '管理员':
#         s.sendto('该用户已存在'.encode(), addr)
#         return
#     s.sendto(b'OK', addr)

#     msg = "\n欢迎%s进入聊天室" % name
#     for i in user:
#         s.sendto(msg.encode(), user[i])
#     user[name] = addr

# def do_chat(s, user, name, data):
#     msg = "\n%s说:%s" % (name, data)
#     for i in user:
#         if i != name:
#             s.sendto(msg.encode(), user[i])

# def do_quit(s, user, name):
#     msg = "\n%s离开了聊天室" % name
#     for i in user:
#         if i == name:
#             s.sendto(b'EXIT', user[i])
#         else:
#             s.sendto(msg.encode(), user[i])
#     del user[name]

# def main():
#     ADDR = ('0.0.0.0', 8888)
#     s = socket(AF_INET, SOCK_DGRAM)
#     s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#     s.bind(ADDR)

#     pid = os.fork()
#     if pid < 0:
#         sys.exit('创建进程失败')
#     elif pid == 0:
#         do_child(s, ADDR)
#     else:
#         do_parent(s)

# if __name__ == "__main__":
#     main()

# #多进程复制图片一半

# from multiprocessing import Process
# from time import sleep
# import os

# filename = "./11.jpg"
# size = os.path.getsize(filename)

# def fun1():
#     f = open(filename, 'rb')
#     n = size // 2
#     fw = open('file1.jpg', 'wb')

#     while True:
#         if n < 1024:
#             data = f.read(n)
#             fw.write(data)
#             break
#         data = f.read(1024)
#         fw.write(data)
#         n -= 1024
#     f.close()
#     fw.close()

# def fun2():
#     f = open(filename, 'rb')
#     fw = open('file2.jpg', 'wb')

#     f.seek(size // 2, 0)
#     while True:
#         data = f.read(1024)
#         if not data:
#             break
#         fw.write(data)
#     fw.close()
#     f.close()

# p1 = Process(target=fun1)
# p2 = Process(target=fun2)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

# #注意：
# １．如果子进程从父进程拷贝对象，对象和网络或者文件相关联
# ，那么父子进程会使用同一套对象属性，相互有一定

# 多进程中行参传参
# from multiprocessing import Process
# from time import sleep

# def worker(sec, name):
#     for i in range(3):
#         sleep(sec)
#         print("I'm %s" % name)
#         print("I'm working．．")

# p = Process(target=worker, args=(2,),\
#     kwargs={'name':"Daivl"}, name='workname')

# p.start()
# print("Process name:", p.name)
# print('child process PID:', p.pid)
# p.join()

# #多进程参数
# from multiprocessing import Process
# from time import sleep,ctime

# def tm():
#     while True:
#         sleep(2)
#         print(ctime())

# p = Process(target=tm)

# p.daemon = True

# p.start()
# sleep(5)
# print('main process Exit')

# #自定义进程类
# from multiprocessing import Process
# from time import sleep

# class Call_Process(Process):
#     def __init__(self, Value):
#         super().__init__()
#         self.Value = Value

#     def run(self):
#         sleep(1)
#         print('开始运行%d秒' % self.Value)

# p = Call_Process(2)

# p.start()
# p.join()

# #创建进程池Ｐool
# from multiprocessing import Pool
# from time import sleep, ctime

# # pool = Pool(processes)

# # pool.apply_async(func, args, kwds)

# # pool.close()
# # pool.join()
# def worker(msg):
#     sleep(2)
#     print(msg)

# pool = Pool(processes=4)
# for i in range(10):
#     msg = 'hello world %d' % i
#     pool.apply_async(func=worker, args=(msg,))

# pool.close()
# pool.join()


# from multiprocessing import Pool
# import time

# def fun(n):
#     time.sleep(1)
#     print("执行pool map事件")
#     return n * n

# pool = Pool(4)
# r = pool.map(fun, range(10))
# pool .close()
# pool.join()
# print(r)

# #进程间通信　的　管道通信
# from multiprocessing import Process, Pipe
# import os,time

# fd1, fd2 = Pipe()

# def fun(name):
#     time.sleep(3)
#     fd1.send([1, 2, 3, 4, 5])

# jobs=[]
# for i in range(5):
#     p = Process(target=fun, args=(i,))
#     jobs.append(p)
#     p.start()

# for i in range(5):
#     data = fd2.recv()
#     print(data)

# for i in jobs:
#     i.join()

# # 进程间通信的消息队列
# from multiprocessing import Queue
# from time import sleep

# q = Queue(3)

# q.put(1)
# sleep(0.01)
# print(q.empty())
# q.put(2)
# print(q.full())
# print(4)
# print('内存', q.qsize())
# q.close()

# #进程间通信的消息队列
# from multiprocessing import Process,Queue
# import time

# q = Queue()

# def fun1():
#     time.sleep(1)
#     q.put({"a":1, 'b':2})

# def fun2():
#     time.sleep(2)
#     print('收到消息:', q.get())
# p1 = Process(target=fun1)
# p2 = Process(target=fun2)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# #进程间通信共享内存
# from multiprocessing import Process,Value
# import time
# import random

# money = Value('i', 2000)

# def deposite():
#     for i in range(100):
#         time.sleep(0.05)
#         money.value += random.randint(1,200)
# def withdraw():
#     for i in range(100):
#         time.sleep(0.02)
#         money.value -= random.randint(1,180)

# d = Process(target=deposite)
# w = Process(target=withdraw)

# d.start()
# w.start()
# d.join()
# w.join()
# print('余额:', money.value)

# from multiprocessing import Process, Array
# import time

# # shm = Array('i', [1,2,3,4,5])
# shm = Array('c', b'Hello')

# def fun():
#     for i in shm:
#         print(i)
#     # shm[3] = 10000
#     shm[0] = b'h'

# p = Process(target=fun)
# p.start()
# p.join()

# for i in shm:
#     print(i)
# print(shm.value)

# #信号
# import os
# import signal

# os.kill(1234, signal.SIGKILL)
# import signal
# import time

# time.sleep(2)
# signal.alarm(4)
# signal.pause()

# import os
# n = os.path.getsize('文件')
# #n 表示文件的大小

# #信号的不同触发
# from multiprocessing import Process
# import os
# from signal import *
# from time import sleep

# def saler_handler(sig, frame):
#     if sig == SIGINT:
#         os.kill(os.getppid(), SIGUSR1)
#     elif sig == SIGQUIT:
#         os.kill(os.getppid(), SIGUSR2)
#     elif sig == SIGUSR1:
#         print('到站了请下车!')
#         os._exit(0)

# def saler():
#     signal(SIGINT, saler_handler)
#     signal(SIGQUIT, saler_handler)
#     signal(SIGUSR1, saler_handler)
#     signal(SIGTSTP, SIG_IGN)
#     while True:
#         sleep(1)
#         print('带你去远方，去看晴空万里!')

# def driver(sig, frame):
#     if sig == SIGUSR1:
#         print('老司机开车了')
#     elif sig == SIGUSR2:
#         print('车速有点快，请寄好安全带!')
#     elif sig == SIGTSTP:
#         os.kill(p.pid, SIGUSR1)

# p = Process(target=saler)
# p.start()

# signal(SIGUSR1, driver)
# signal(SIGUSR2, driver)
# signal(SIGTSTP, driver)
# signal(SIGINT, SIG_IGN)
# signal(SIGQUIT, SIG_IGN)

# p.join()

# 使用fork实现多进程并发
# 1,创建套接字，绑定，监听
# 2,等待接收客户端请求
# 3,创建新的进程处理客户端请求
# 4,原有进程继续等待接收新的客户端链接
# 5,如果客户端退出则关闭子进程

# import os,sys
# from socket import *
# from signal import *

# HOST = '0.0.0.0'
# PORT = 8888
# ADDR = (HOST, PORT)

# s = socket()
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# s.bind(ADDR)
# s.listen(5)

# print('正在链接中...%d' % os.getpid())
# #在父进程中忽乐子进程状态改变，子进程退出自动由系统处理
# signal(SIGCHLD, SIG_IGN)

# def client_handler(c):
#     print('处理子进程的请求:', c.getpeername())
#     try:
#         while True:
#             data = c.recv(1024).decode()
#             if not data:
#                 break
#             print(data)
#             c.sendall(b'message is come')
#     except (KeyboardInterrupt, SystemError):
#         sys.exit('客户端退出')
#     except Exception as e:
#         print(e)
#     c.close()
#     sys.exit('客户端退出d')


# while True:
#     try:
#         c, addr = s.accept()
#     except KeyboardInterrupt:
#         sys.exit('服务器退出')
#     except Exception as e:
#         print('Error:', e)
#         continue
#     pid = os.fork()
#     if pid == 0:
#         s.close()
#         client_handler(c)
#     else:
#         c.close()
#         continue


'''
ftcp 文件服务器
'''
from socket import *
import os,sys
from time import sleep
import signal

FILE_PATH = '/home/tarena/ftcp/'
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

class ftpserver(object):
    """docstring for ftpserver"""
    def __init__(self, c):
        self.c = c
    
    def do_list(self):
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.c.send('文件库为空'.encode())
            return
        else:
            self.c.send(b'OK')
            sleep(0.1)
        files = ''
        for file in file_list:
            if file[0] != '.' and os.path.isfile(FILE_PATH + file):
                files = files + file + '#'
        self.c.sendall(files.encode())
    def get_file(self):
        data = c.recv(1024).decode()
        file_py = FILE_PATH + data
　       if os.path.exists(file_py):
            self.c.send(b'OK')
            sleep(0.1)
        fil = open(file_py, 'rb')
        self.c.sendall(fil)

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("listen the port 8000...")

    while True:
        try:
            c, addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print("服务端异常:", e)
            continue
        print('已链接客户端:', addr)
       #创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            ftp = ftpserver(c)
            while True:
                try:
                    data = c.recv(1024).decode()
                    if not data:
                        c.close()
                        sys.exit('客户端退出')
                    elif data[0] == 'L':
                        ftp.do_list()
                    elif data[0] == 'G':
                        ftp.get_file()

                except Exception:
                    sys.exit('客户端退出')

        else:
            c.close()
            continue

if __name__ == '__main__':
    main()

sock_file = './sock_file'
if os.path.exists(sock_file):
    os.remove(sock_file)
