# # del_method.py


# # 此示例示意析构方法的用法


# c1 = Car('BYD E6')
# c2 = c1

# del c1  # 此时是删除c1变量,同时解除c1绑定的对象的引用
# input("请按回车键结束程序的执行!")
# class Car:
#     def __init__(self, name):
#         self.name = name
#         print("汽车", name, '被创建')

#     def __del__(self):
#         '''析构方法,此方法会在对象销毁时自动被调用'''
#         print('汽车', self.name, '被销毁')

# class Human:
#     __slots__ = ['name', 'age']
#     def __init__(self, name, age):
#         self.name, self.age = name, age

# h1 = Human('Tarena', 15)
# print(h1.age)

#httpsever1协议
from socket import *
s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)

while True:
    print("正在链接中..")
    c, addr = s.accept()
    print('connect from', addr)
    data = c.recv(4096)
    print('**********************')
    print(data)
    print('**********************')
    c.close()

s.close()
