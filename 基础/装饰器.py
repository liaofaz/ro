# -*- codeing = utf-8 -*-
# @Time : 2021/8/5 上午 5:39
# @Author : 漫天烟华
# @File : 装饰器.py
# @Software : PyCharm


# 内置装饰器 classmethod,staticmethod,property


# from functools import wraps
#
#
# def wrapper(func):
#     @wraps(func)
#     def inner(a):
#         print(a ** 2)
#         return func(a)
#     print(3)
#     return inner
#
#
# def test(a):
#     print(a)
#     print(test.__name__)
#
#
# # wrapper(test)(6)
# # print('-' * 60)
# test = wrapper(test)    # 装饰器原理
# test(3)
