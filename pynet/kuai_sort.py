# def sort0(arr):
#     if len(arr) < 1:
#         return arr
#     else:
#         pivot = arr[0]
#         left_arr = [i for i in arr[1:] if i <= pivot]
#         right_arr = [i for i in arr[1:] if i > pivot]
#         return sort0(left_arr) + [pivot] + sort0(right_arr)

# A = [2, 5, 45, 78, 4, 24, 15, 7, 1, 89, 212, 9]
# print(sort0(A))


# def baobao(arr):
#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr
# A = [2, 5, 45, 78, 4, 24, 15, 7, 1, 89, 212, 9]
# print(baobao(A))

# import json
# di = {'name':'alc', 'age':23, 'sex':'m'}
# # print(type(di))

# j = json.dumps(di)
# # print(type(j))
# # print(j)

# f = open('序列化对象', 'w')
# f.write(j)
# f.close()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# super_init.py

# 此示例示意 用super函数显示调用基类__init__初始化方法


class Human:

    def __init__(self, n, a):
        self.name, self.age = n, a
        print("Human的__init__方法被调用")

    def infos(self):
        print("姓名:", self.name)
        print("年龄:", self.age)


class Student(Human):

    def __init__(self, n, a, s=0):
        super().__init__(n, a)  # 显式调用父类的初始化方法
        self.score = s  # 添加成绩属性
        print("Student类的__init__方法被调用")

    def infos(self):
        super().infos()  # 调用父类的方法
        print("成绩:", self.score)


s1 = Student('小张', 20, 100)
s1.infos()
