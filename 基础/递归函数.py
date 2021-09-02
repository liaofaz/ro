# -*-  codeing = utf-8 -*-
# @Time : 2021/5/23 9:32
# @Author : 漫天烟华
# @File : 递归函数.py
# @Software : PyCharm

# 递归函数: 函数内部调用自己，且必须有出口,例子:
# def sum_n(n):
#     if n==1:
#         return 1
#     return n + sum_n(n-1)
# print(sum_n(10))



# 阶乘
# def factorial(x):
#     n = x
#     for i in range(1,x):
#         n = n * i
#     return n
# print(factorial(10))
# def jc(x):
#     if x == 1:
#         return x
#     return x * jc(x-1)
# print(jc(10))

# 0,1,1,2,3,5,8,13,21,33...
# 斐波那契数列
# 用迭代方法实现:
# def fs1(n):
#     n2 = 1
#     n1 = 1
#     if n == 0:
#         result = 0
#     elif n == 1 or n == 2:
#         result = 1
#     elif n < 0:
#         result = None
#     while n > 2:
#         n3 = n1 + n2
#         n1, n2 = n2, n3
#         n -= 1
#     return n3
# print(fs1(20))
# 用递归函数实现:
# def fs2(n):
#     if n < 0:
#         return None
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     return fs2(n-1)+fs2(n-2)
# print(fs2(20))


# 用递归函数方法实现汉诺塔游戏的攻略:
# def hannuota(n,x,y,z):
#     if n == 1:
#         print(x, "→", z)
#     else:
#         hannuota(n-1, x, z, y)
#         print(x, "→", z)
#         hannuota(n-1, y, x, z)
#
# hannuota(5,'X','Y','Z')