# from socket import *

# s = socket()
# s.connect(('127.0.0.1', 8888))

# while True:
#     msg = input(">>")
#     if not msg:
#         break
#     s.send(msg.encode())
#     data = s.recv(1024)
#     print(data.decode())
# s.close()

# #UDPClient.py
# from socket import *
# import sys
# try: 
#     HOST = sys.argv[1]
#     PORT = int(sys.argv[2])
#     addr = (HOST, PORT)
#     s = socket(AF_INET, SOCK_DGRAM)
#     # addr = (('127.0.0.1', 8888))

#     while True:
#         msg = input(">>")
#         if not msg:
#             break
#         s.sendto(msg.encode(), addr)
#         data, addr = s.recvfrom(1024)
#         print(data.decode())
#     s.close()
# except IndexError:
#     if len(sys.argv) < 3:
#         print('''
#             argv is error!
#             run as
#             udp_client.py 127.0.0.1 8888
#             ''')

# from socket import *
# from time import sleep

# dest = ('176.122.16.255', 8889)
# s = socket(AF_INET, SOCK_DGRAM)
# s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# while True:
#     sleep(2)
#     s.sendto('来啊，欢迎你来中国'.encode(), dest)

# s.close()

# #用tcp服务复制图片
# from socket import *
# import sys

# s = socket()
# HOST = sys.argv[1]
# PORT = int(sys.argv[2])
# addr = (HOST, PORT)

# s.connect(addr)

# filename = s.recv(1024).decode()

# f = open('/home/tarena/' + filename, 'wb')

# while True:
#     data = s.recv(4096)
#     if data == '##':
#         break
#     f.write(data)

# s.send("接收完成".encode())

# f.close()
# s.close()

# #IO
# from socket import *
# from time import sleep,ctime

# s = socket()
# s.setsockopt\
# (SOL_SOCKET, SO_REUSEADDR, 1)
# s.bind(('0.0.0.0', 8888))
# s.listen(3)

# s.setblocking(False)

# while True:
#     print('正在链接中..')
#     try:
#         c, addr = s.accept()
#     except BlockingIOError:
#         sleep(2)
#         print(ctime())
#         continue
#     else:
#         print('connect from:', addr)
#         while True:
#             data = c.recv(1024).decode()
#             if not data:
#                 break
#             print(data)
#             c.sendall(b'message is comming')
#         c.close()
# s.close()

# #本地套接字
# from socket import *
# sock_file = './sock_file'

# s = socket(AF_UNIX, SOCK_STREAM)
# s.connect(sock_file)

# while True:
#     msg = input('>>')
#     if not msg:
#         break
#     s.send(msg.encode())
#     print(s.recv(1024).decode())
# s.close()

#进程（Process）

#功能项目编程
from socket import *
import sys,os
from time import *

class ftpclient(object):
    """docstring for ftpserver"""
    def __init__(self, s):
        self.s = s

    def do_list(self):
        self.s.send(b'L')
        data = self.s.recv(1024).decode()
        if data == 'OK':
            data = self.s.recv(4096).decode()
            files = data.split('#')
            for file in files:
                print(file)
            print("文件列表展示完毕\n")
        else:
            print(data)

    def get_file(self):
        self.s.send(b'G')
        msg = input('请输入下载的文件:')
        self.s.send(msg.encode())
        
def main():
    if len(sys.argv) < 3:
        print('argv is error')
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print('连接服务器失败:', e)
        return

    ftp = ftpclient(s)
    while True:
        print("**************************")
        print("|%s|" % '1,查看服务端文件'.center(17))
　
print("|%s|" % '2,下载文件到本地'.center(17))
        print("|%s|" % '3,上传文件到服务器'.center(16))
        print("|%s|" % 'quit'.center(24))
        print("**************************")
        try:
            cmd = input('请输入命令>>')
            if cmd == '1':
                ftp.do_list()
            if cmd == '2':
                ftp.get_file()

        except KeyboardInterrupt:
            sys.exit('窗口退出')

if __name__ == "__main__":
    main()

# def info():
#     print("**************************")
#     print("*%s*" % '1,查看服务端文件'.center(17))
#     print("*%s*" % '2,下载文件到本地'.center(17))
#     print("*%s*" % '3,上传文件到服务器'.center(16))
#     print("**************************")

# def see_files(num):
#     if num == '1':
#         data = c.recv(1024).encode()
#         print(data)

# def recv_files(num):
#     if num == '2':
#         pass

# def send_files(num):
#     pass

# def main():
#     if len(sys.argv) < 3:
#         print('argv is error')
#         return
#     HOST = sys.argv[1]
#     PORT = sys.argv[2]
#     ADDR = (HOST, PORT)
#     s = socket()
#     s.connect(ADDR)
