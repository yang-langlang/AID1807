# from socket import *
# import sys, os

# def send_msg(s, name, addr):
#     while True:
#         text = input('发言：')
#         msg = "C %s %s" % (name, text)
#         s.sendto(msg.encode(), addr)

# def recv_msg(s):
#     while True:
#         data,addr = s.recvfrom(2048)
#         print(data.decode())

# #创建套接字，登录，创建子进程
# def main():
#     if len(sys.argv) < 3:
#         print('argv is error')
#         return
#     HOST = sys.argv[1]
#     PORT = int(sys.argv[2])
#     ADDR = (HOST, PORT)

#     s = socket(AF_INET, SOCK_DGRAM)

#     if login(s, ADDR):
#         pid = os.fork()
#         if pid < 0:
#             sys.exit("创建子进程失败")
#         elif pid == 0:
#             do_child()
#         else:
#             do_parent()
#     else:
#         return

# def login(s, ADDR):
#     while True:
#         name = input('请输入姓名:')
#         msg = 'L ' + name
#         s.sendto(msg.encode(), ADDR)
#         data, addr = s.recvfrom(1024)
#         if data.decode() == 'OK':
#             print('@您已进入聊天室@')
#             return name

#         else:
#             print(data.decode())

# def do_child(s, name, addr):
#     while True:
#         text = input("发言(quit退出):")
#         if text.strip() == "quit":
#             msg = "Q" + name
#             s.sendto(msg.encode(), addr)
#             sys.exit("退出聊天室")

#         msg = "C %s %s"%(name, text)
#         s.sendto(msg.encode(), addr)

# def do_parent():
#     while True:
#         msg, addr = s.recvfrom(1024)
#         if msg.decode() == "EXIT":
#             sys.exit(0)
#         print(msg.decode() + "\n发言(quit退出):", end='')


# if __name__ == "__main__":
#     main()

# 进程线程的区别与联系
# １，两者都是多任务编程方式，都是能够使用计算机的多核资源
# ２，进程的创建删除消耗的计算机资源比线程要多
# ３，进程空间独立，数据相互不干扰，有专门的ＩＰＣ，线程使
# 用全局变量进行通信
# ４，一个进程可以创建多个线程分支，两者之间存在包含关系
# ５，多个线程公用进程的资源
# ６，进程线程在系统中都有自己特有的属性，ＩＤ，代码段，栈区等
# 资源

# 使用场景
# ＊需要创建较多并发，同时任务关联性比较强时一般用多线程
# ＊不同的任务模块可能更多使用进程
# ＊使用进程线程需要考虑数据的处理复杂度，比如进程间通
# 信是否方便，同步互斥是否过于复杂

# １，进程线程的区别和联系
# ２，进程间通信方式都知道哪些，有什么特点
# ３，同步互斥意义是什么，什么情况下用
# ４，给一个情形，分析下用进程还是用线程，理由
# ５，一些常见概念挖掘：僵尸进程，进程状态，ＧＩＬ