# -*-  codeing = utf-8 -*-
# @Time : 2021/3/7 下午 6:59
# @Author : 漫天烟华
# @File : 元组.py
# @Software : PyCharm


# 【元组】    （注：元组不可修改，但是元组中的变量元素中的元素可修改。）

"""
tuple1 = ()
print(type(tuple1))         #创建空元组
# <class 'tuple'>

tuple2 = (1)
print(type(tuple2))         #创建单元素元组时，直接加括号会默认把括号当成运算符号，此时变量的类型还是括号内的类型，并非元组
# <class 'int'>
a = "字符串"
tuple2 = (a)
print(type(tuple2))
#<class 'str'>

tuple3 = (1,)
print(type(tuple3))         #在单元素后面加逗号，单元素元组创建成功。多元素元组无需在最后一个元素结尾加逗号
# <class 'tuple'>

"""


'''

#  给【元组】增加元素

tuple1 = (1,2,3)
print(id(tuple1))
#2845766361728
tuple2 = ("a","b","c")

#tuple1(1) = 4                   #报错，元组无法修改自身元素

tuple1 = tuple1 + tuple2
print(tuple1)                    #看似增加其实是原来的tuple1被覆盖了
#(1, 2, 3, 'a', 'b', 'c')
print(id(tuple1))
#2845766587488

'''


# 【删除】元组

# tuple_1 = (1,2,3,4,5)
# print(tuple_1)
# del tuple_1
# print(tuple_1)     #报错，整个元组被从内存中删除，变量回到未定义状态
# NameError: name 'tuple_1' is not defined
