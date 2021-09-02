# -*-  codeing = utf-8 -*-
# @Time : 2021/5/27 6:20
# @Author : 漫天烟华
# @File : 类对象魔法方法.py
# @Software : PyCharm


# 魔法方法的格式一般为双下划线包围的字符，如__init__

# ----------------------------------------------------------------------------------------------------------------------
# 构造与析构

# 构造器__init__、__new__
# 一般来,要定义属性的时候就会重构__init__,且__init__返回值必须是None，不可return
# 一般需要传入参数时，就要重写__init__
# __new__(cls[,...]) 实例化对象时最先调用的方法，详情待了解.....
# ----------------------------------------------------------------------------------------------------------------------
# 析构器__del__
# __del__(self) 当实例化对象的所有引用对象被删除时（没有对象指向id）才执行，程序运行完全部代码关闭时也会执行
# class C:
#     def __init__(self):
#         print("我是__init__方法，我被调用了...")
#     def __del__(self):
#         print("我是__del__方法，我被调用了...")
# c = C()
# b = c
# a = b
# del c
# print("程序正在结束...")  # 删除c后没执行
# del b
# print("程序正在结束...")  # 删除b后没执行
# del a                   # 全部引用删除完时执行
# print("程序已结束...")

# ----------------------------------------------------------------------------------------------------------------------
# 反运算
# class N_int(int):
#     def __rsub__(self, other):
#         return int.__sub__(self, other)  # 这里修改了父类的方法
# a = N_int(5)
# print(2-a)  # 2没有方法，实际运算时为a-2(被减的方法换成了减的方法)
# print(a-2)
# b = int(5)
# print(2-b)  # 用了b对象的方法，return int.__sub__(other,self)
# ----------------------------------------------------------------------------------------------------------------------
# __str__ 当直接打印实例化对象时默认返回实例化对象的内存地址（id），重写打印则返回return的值，交互式仍返回id
# __repr__ 与__str__类似，作为除字符串外的容器的元素时调用，交互式的IDLE直接取值也会调用
# 只要重写上两方法的其中一个，返回值就会改变，__repr__影响所有返回值，str只影响print打印的返回值（都重写后优先级更高）
# class Repr:
#     def __init__(self, color=None):
#         self.color = color
#
#     def __repr__(self):
#         return '正在调用__repr__...'
#
#     def __str__(self):
#         return '正在调用__str__...'
#
#
# r = Repr()
# print(r)    # 直接打印时，调用__str__
# print(str(r))
# print(repr(r))
# print(type(r))
# print('-'*100)
# # 作为列表、元组、字典、集合等容器的元素时，调用__repr__
# print([r])
# print({'method': r})
# print((r,))
# print({r})
# ----------------------------
# 简单定制(定制计时器)
# import time
#
#
# class Mytimer:
#     def __init__(self):
#         self.unit = ['年','月','天','时','分','秒']
#         print('计时器准备就绪！')
#         self.rep = '未开始计时！'
#         self.t1 = 0
#
#     def __add__(self, other):
#         rep = '一共过去了'
#         result = []
#         for i in range(3):
#             result.append(self.t[i] + other.t[i])
#             if result[i]:
#                 rep += (str(result[i]) + self.unit[i+3])
#         return rep
#
#     def __repr__(self):
#         return self.rep
#
#     def start(self):
#         self.t1 = time.localtime()
#         print("开始计时...")
#
#     def stop(self):
#         if self.t1 == 0:
#             print('请先调用start方法开始计时！')
#         else:
#             self.t2 = time.localtime()
#             print("计时结束!")
#             self.__time()
#
#     def __time(self):       # 内部方法
#         self.t = []
#         self.rep = '时间过去了'
#         for i in range(3,6):
#             self.t.append(self.t2[i] - self.t1[i])
#             if self.t[i-3]:
#                 self.rep += str(self.t[i-3]) + self.unit[i]
#
#
# t1 = Mytimer()
# print(t1)
# t1.stop()
# t1.start()
# time.sleep(3)
# t1.stop()
# print(t1)
# print('-'*30)
# t2 = Mytimer()
# t2.start()
# time.sleep(2)
# t2.stop()
# print(t2)
# print('-'*30)
# print(t1+t2)
# ----------------------------------------------------------------------------------------------------------------------
# 属性访问的魔法方法（__getattr__,__getattribute__,__setattr__,__delattr__）
# __getattr__(self,name) 定义当用户试图获取一个不存在的属性时的行为（object默认没有这方法且报错，设置了不报错）
# __getattribute__（self,name） 定义当该类的属性被访问时的行为（无论该属性存不存在，都会先访问该方法）
# __setattr__（self,name,value） 定义当一个属性被设置时的行为
# __delattr__（self,name） 定义当一个属性被删除时的行为
# -----------------------------------------------
# class C:
#     def __getattribute__(self, name):
#         print('__getattribute__...')
#         return super().__getattribute__(name)
#     def __getattr__(self, name):
#         print('__getattr__...')
#         return '没有该属性...'       # 与getattr函数的参数三功能类似，不设置则默认返回None
#
#     def __setattr__(self, name, value):
#         print('__setattr__...')
#         super().__setattr__(name,value)
#     def __delattr__(self, name):
#         print('__delattr__...')
#         super().__delattr__(name)
# c = C()
# c.x         # 访问不存在属性时，先调用__getattribute__,再调用__getattr__
# print(c.x)  # 若设置了返回值，可通过print打印，没设置默认返回None
# c.x = 1     # 新增属性时，调用__setattr__
# c.x         # 访问存在的属性时，只调用__getattribute__
# del c.x     # 删除属性时，调用__delattr__
# -----------------------------------------------
# 设置一个矩形的类，默认属性宽和高，若给一个square属性赋值，则矩形为正方形，变长等于值，宽与高等于边长
# -------------
# class Juxing:
#     def __init__(self,wide=0,high=0):
#         self.wide = wide
#         self.high = high
#     def __setattr__(self, key, value):
#         if key == 'square':
#             self.wide = value
#             self.high = value
#             print(f'这是一个正方形，边长为{value}')
#         else:
#             super().__setattr__(key,value)  #（方法一）直接self.name = value会无限递归死循环
#             # self.__dict__[key] = value    #(方法二)
# s = Juxing()
# s.square = 5
# print(s.wide)
# print(s.high)
# ----------------------------------------------------------------------------------------------------------------------
# 描述符: 将某种特殊类型的类的实例指派给另一个类的属性
# __get__(self,instance,owner)  用于访问属性，它返回属性的值
# __set__(self,instance,owner)  将在属性分配操作中调用，不返回任何内容
# __delete__(self,instance)     控制删除操作，不返回任何内容
# --------------------------------------------
# class Mytest:
#     def __get__(self, instance, owner):
#         print('__get__...', self, instance, owner)
#         return None
#     def __set__(self, instance, value):
#         print('__set__...', self, instance, value)
#     def __delete__(self, instance):
#         print('__delete__...', self, instance)
#
# class Test:
#     x = Mytest()
#
# test = Test()
# print(test)         # 实例化对象test的内存地址
# print(test.x)              # self=193行实例化的Mytest内存地址，instance=实例化test内存地址，owner=类Test（类对象）
# test.x = 'x的值'     # self值同上，instance值同上，value=为传入值
# del test.x
# --------------------------------------------
# class Myproperty:
#     def __init__(self,get_a=None,set_a=None,del_a=None):
#         self.get = get_a
#         self.set = set_a
#         self.dele = del_a
#     def __get__(self, instance, owner):
#         return self.get(instance)
#     def __set__(self, instance, value):
#         self.set(instance,value)
#     def __delete__(self, instance):
#         self.dele(instance)
#
# class CC:
#     def __init__(self):
#         self.a = 10
#     def get_a(self):
#         print('属性的值为:',end="")
#         return self.a
#     def set_a(self,value):
#         self.a = value
#         print(f'属性值已修改为{self.a}')
#     def del_a(self):
#         del self.a
#         print('self.a已删除')
#     x = Myproperty(get_a,set_a,del_a)
# c = CC()
# print(c.x)
# c.x = 5
# print(c.x)
# del c.x
# ----------------------------------------------------------------------------------------------------------------------
# 迭代器的魔法方法，一个类要成为迭代器需要两种方法__iter__与__next__
# -------------------------
# 用while循环实现for循环功能
# s = 'you are my sun'
# i = iter(s)     # 将序列转化为迭代器
# while True:
#     try:
#         each = next(i)  # 逐个访问序列元素
#     except StopIteration:
#         break
#     print(each)
# -------------------------
# 斐波那契数列迭代器
# class Fibs:
#     def __init__(self, n=30):
#         self.a = 0
#         self.b = 1
#         self.n = n
#         self.o = True
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a+self.b
#         if self.o:
#             self.a, self.o = 0, False
#         if self.a > self.n:
#             raise StopIteration
#         return self.a
#
#
# f = Fibs()
# for i in f:
#     print(i)
# ----------------------------------------------------------------------------------------------------------------------
