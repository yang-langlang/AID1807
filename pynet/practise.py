# from socket import *

# s = socket()
# s.bind(('localhost', 8888))
# s.listen(5)

# while True:
#     print("正在链接中..")
#     connfd, addr = s.accept()
#     print('Connect come from', addr)
#     while True:
#         data = connfd.recv(5)
#         if not data:
#             break
#         print(data.decode())
#         connfd.sendall(b'message is coming')
#     connfd.close()
# s.close()

#UDPServer.py
# from socket import *
# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(("0.0.0.0", 8888))

# while True:
#     print('正在连接中..')
#     data, addr = s.recvfrom(1024)
#     if not data:
#         break
#     print(">>%s:%s" % (addr, data.decode()))
#     n = s.sendto(b'Message is coming', addr)

# s.close()

# #套接子属性
# from socket import *
# s = socket()

# print(s.family)
# print(s.type)
# s.bind(('127.0.0.1', 8888))
# print(s.getsockname())
# print(s.fileno())
# #每一个ＩＯ事件系统都分一个正整数编号，改正编号即为文件描述符
# print(c.getpeername())
# s.setsockopt(level, option, value)
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# #udp之应用广播
# from socket import *
# s = socket(AF_INET, SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# s.bind(('0.0.0.0', 8889))

# while True:
#     try:
#         data, addr = s.recvfrom(1024)
#         print('从{}获取信息:{}'.format(addr, data.decode()))
#         s.sendto(b'message is coming', addr)
#     except KeyboardInterrupt:
#         raise
# s.close()

# #httpsever1协议
# from socket import *
# s = socket()
# s.bind(('0.0.0.0', 8889))
# s.listen(5)

# while True:
#     print("正在链接中..")
#     c, addr = s.accept()
#     print('connect from', addr)
#     data = c.recv(4096)
#     print('**********************')
#     print(data)
#     print('**********************')
#     data = '''HTTP/1.1 200 OK
#     User-Agent: Mozilla/5.0

#     <h1>Welcome to China</h1>
#     '''
#     c.sendall(data.encode())
#     c.close()

# s.close()

##用tcp服务复制图片
# from socket import *
# from time import *

# s = socket()
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# s.bind(('0.0.0.0', 8888))
# s.listen(5)

# print("正在链接中...")
# c, addr = s.accept()
# print('connect from', addr)

# f = open('./11.jpg', 'rb')
# c.send('11.jpg'.encode())
# sleep(0.1)

# while True:
#     data = f.read(4096)
#     if not data:
#         break
#     c.sendall(data)

# sleep(0.1)
# c.send('##'.encode())

# data = c.recv(1024)
# print(data.decode())

# c.close()
# f.close()
# s.close()

#带网页HttpServer
# from socket import *

# def handleClient(c):
#     request = c.recv(4096)
#     request_lines = request.splitlines()
#     for line in request_lines:
#         print(line.decode('utf-8'))

#     try:
#         f = open("http.html")
#     except IOError:
#         response = 'HTTP/1.1 404  NOT Found\r\n'
#         response += "\r\n"
#         response += "not found"
#     else:
#         response = 'HTTP/1.1 200  OK\r\n'
#         response += "\r\n"
#         response += f.read()
#     finally:
#         c.sendall(response.encode())

# def main():
#     s = socket()
#     s.setsockopt\
#     (SOL_SOCKET, SO_REUSEADDR, 1)
#     s.bind(('0.0.0.0', 8888))
#     s.listen(5)
#     print('正在链接中...')
#     while True:
#         c, addr = s.accept()

#         handleClient(c)
#         c.close()
#     s.close()

# if __name__ == '__main__':
#     main()


# #IO多路复用
# #epoll方法
# from select import *
# from socket import *

# s = socket()
# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# s.bind(('0.0.0.0', 8888))
# s.listen(5)

# p = epoll()

# famap = {s.fileno():s}

# p.register(s, EPOLLIN | EPOLLERR)

# while  True:
#     events = p.poll()
#     for fd,event in events:
#         if fd == s.fileno():
#             c, addr = fdmap[fd].accept()
#             print("connect from", addr)

#             p.register(c, EPOLLIN | EPOLLERR)
#             fdmap[c.fileno()] = c
#         elif event & POLLIN:
#             data = fdmap[fd].recv(1024)
#             if not data:
#                 p.unregister(fd)
#                 fdmap[fd].close()
#                 def fdmap[fd]
#             else:
#                 print(data.decode())
#                 fdmap[fd].send(b'Receive')

# 本地套接字
# from socket import *
# import os

# sock_file = './sock_file'
# if os.path.exists(sock_file):
#     os.remove(sock_file)

# s = socket(AF_UNIX, SOCK_STREAM)
# s.bind(sock_file)
# s.listen(5)
# while True:
#     c, addr = s.accept()
#     print('connect from', addr)
#     while True:
#         data = c.recv(1024).decode()
#         if not data:
#             break
#         print(data)
#         c.send(b'message is comming')
#     c.close()
# s.close()

# #!/usr/bin/env/practise.py
# #进程（Process）
# from time import sleep, ctime

# while True:
#     sleep(1)
#     print(ctime())
# #查看进程控制块
# ps -aux　
# #查看进程树
# pstree
# #查看父进程的ＰＩＤ号
# ps -ajx

# #多进程编程
# import os
# pid = os.fork()
# 功能：创建新的进程
# 返回值：失败时返回一个负数
# 　　　　　　　成功：在原有进程中返回新的进程的ＰＩＤ号
# 　　　　　　　　　　　　在新的进程中返回０

# #! /usr/bin/python3
# import os
# from time import sleep

# print("**************************")
# a = 1

# pid = os.fork()
# if pid < 0:
#     print("创建进程失败!")
# elif pid == 0:
#     sleep(1)
#     print("这是新的进程")
#     print("a =", a)
#     a = 10000
# else:

#     print("这是原有进程")
#     print("a=", a)
# print("程序完毕")

# import os, sys

# # os._exit(0)
# # sys.exit("Hello World!")
# try:
#     sys.exit("Hello World!")
# except SystemExit as e:
#     print('退出原因：', e)

# print("Process is Exit")


# 循环服务器

#　coding=utf-8
'''
http server v2,0
1,　多线程并发
２，可以请求简单数据
３，能进行简单解析
４，使用类进行封装
'''
# from socket import *
# from threading import Thread
# import sys


# class HTTPServer():
#     def __init__(self, server_addr, static_dir):
#         self.server_address = server_addr
#         self.static_dir = static_dir
#         self.ip = server_addr[0]
#         self.port = server_addr[1]
#         self.create_socket()

#     def create_socket(self):
#         self.s = socket()
#         self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#         self.s.bind(self.server_address)

#     def server_forever(self):
#         self.s.listen(5)
#         print('listen the port %d' % self.port)
#         while True:
#             try:
#                 c, addr = self.s.accept()
#             except KeyboardInterrupt:
#                 self.s.close()
#                 sys.exit('服务器退出')
#             except Exception:
#                 traceback.print_exc()
#                 continue
#             clientThread = Thread(target=self.handleRequest,args=(c,))
#             clientThread.setDaemon(True)
#             clientThread.start()

#     def handleRequest(self, c):
#         request = c.recv(4096)
#         requestHeaders = request.splitlines()
#         print(c.getpeername(), ':', requestHeaders[0].decode())

#         getRequest = str(requestHeaders[0]).split(' ')[1]
#         if getRequest == '/' or getRequest[-5:] == '.html':
#             self.get_html(c, getRequest)
#         else:
#             pass
#         c.close()

#     def get_html(self, c, getRequest):
#         if getRequest == '/':
#             filename = self.static_dir + '/http.html'
#         else:
#             filename = self.static_dir + getRequest
#         try:
#             f = open(filename, 'r')
#         except IOError:
#             response = 'HTTP/1.1 404  NOT Found\r\n'
#             response += "\r\n"
#             response += "not found the page"
#         else:
#             response = 'HTTP/1.1 200  OK\r\n'
#             response += "\r\n"
#             response += f.read()
#         finally:
#             c.sendall(response.encode())
#     def get_data(self, connfd, getRequest):
#         urls = ['/time', '/tedu', '/python']
#         if getRequest in urls:
#             response = 'HTTP/1.1 200  OK\r\n'
#             response += "\r\n"
#             if getRequest == "/time":
#                 import time
#                 response += time.ctime()
#             elif getRequest == 'tedu':
#                 response += 'Welcome to china'

#         else:
#             response = 'HTTP/1.1 404  NOT Found\r\n'
#             response += "\r\n"
#             response += "not found the data"

# if __name__ == '__main__':
#     server_addr = ('0.0.0.0', 8888)
#     static_dir = './static'

#     httpd = HTTPServer(server_addr, static_dir)
#     httpd.server_forever()

# #greenlet0.py
# from greenlet import greenlet

# def test1():
#     print(12)
#     gr2.switch()
#     print(34)

# def test2():
#     print(56)
#     gr1.switch()
#     print(78)

# gr1 = greenlet(test1)
# gr2 = greenlet(test2)

# gr1.switch()

from socket import *
import os


