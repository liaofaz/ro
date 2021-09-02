# -*-  codeing = utf-8 -*-
# @Time : 2021/5/17 8:44
# @Author : 漫天烟华
# @File : 类对象Class.py
# @Software : PyCharm

# --------------------------------
# Object Oriented 面向对象三大特性:

# 封装    信息隐蔽技术
# 继承    子类自动共享父类之间的数据和方法的机制
# 多态    是指同一个方法调用，由于对象不同可能会产生不同的行为。


#

# class Complex:     # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是self。
#     def __init__(self, realpart, imagpart):         # __init__在类实例化后会自动调用
#         self.r = realpart                           # r、i这些称为类的属性
#         self.i = imagpart
#     def return_args(self):                          # 类内定义的函数定义称为类的方法
#         print(self.r,self.i)                        # self代表类的实例，而非类
#         return self.r,self.i
# x = Complex(3.0, -4.5)
# print(x.r, x.i)         # 打印类的属性
# item = x.return_args()  # 调用类的方法
# print(item)


'''
class People（要继承的父类，可多个，可省略）:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问   print(p.__weight)会报错
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我%d岁了 %s公斤" % (self.name, self.age,self.__weight))

# 实例化类
p = People('runoob', 10, 30)
p.speak()
'''


#
# Python 的 self 相当于 C++ 的 this 指针。如果说类是图纸，实例化的对象是一个个房子，那么self就是房子的门牌号

# class Call:
#     def yourname(self,name):
#         self.name = name
#
#     def call(self):
#         print(f"{self.name}，是您在叫我吗？")
#
# a = Call()
# a.yourname("都督")      # 没__init__时，要在调用调用对象的方法时传入参数
# b = Call()
# b.yourname("主人")
# a.call()
# b.call()
# -------------------------------------------------------
# Python 的魔法方法之(__init__)，类似C++的构造函数

# class Call:
#     def __init__(self,name="主公"):
#         self.name = name
#
#     def call(self):
#         print(f"{self.name}，是您在叫我吗？")
#
# a = Call("老师")      # 与上面的方法相比，__init__可在实例化类对象时就传入参数
# b = Call("老板")
# c = Call()
# a.call()
# b.call()
# c.call()

# --------------------------------------------------------------------------------------------------------
# 多态(polymorphism)是指同一个方法调用，由于对象不同可能会产生不同的行为。                           # 多态特性
# 多态是方法的多态，属性没有多态   （存疑）
# 2.多态的存在有两个必要条件：继承、方法重写    （存疑）
# ----------------------------
# # 例子一:
# class Man:
#     def eat(self):
#         print("饿了，吃饭了!")
# class Chinese(Man):
#     def eat(self):
#         print("中国人用筷子吃饭")
# class English(Man):
#     def eat(self):
#         print("英国人用刀叉吃饭")
# Chinese().eat()
# English().eat()
# Man().eat()
# # ----------------------------
# # 例子二:
# print("AAAAAA".count("A"))
# print([1,2,5,6,1,].count(1))
# print((5,6,1,9).count(6))
# -------------------------------------------------------

# 默认上来说，对象的属性和方法都是公开的，都是共有的，我们可以通过点（.）操作符来进行访问
# 为了实现类似于私有变量的特征，Python内部采用了一种叫做 name mangling（名字改编，名字重整）的技术，
# 在Python 中定义私有变量只主要在变量名或函数名前加上“__”两个下划线，那么这个函数或变量就会为私有的了。
# 理论上私有变量无法直接外部访问，只能内部间接访问，但其实name mangling 技术的意思就是名字改编、名字重整
# Python只是动了一下手脚把双下划线开头的变量改了名字而已，会自动是改成了  _类名__变量名

# class Person:
#     name = "豆腐"
#     __name = "凉茶"
#
#     def getname(self):
#         return self.__name
# p = Person()
# print(p.name)       # 公有
# #print(p.__name)    # 会报错，无法直接外部访问
# print(p.getname())  # 调用对象方法间接访问
# print(p._Person__name)# Python类的私有只是改了变量名字，即_类名__变量名，输入更改过后的变量名即可直接外部访问

# --------------------------------------------------------------------------
# 按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
# 假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
# 游戏生成1只乌龟和10条鱼
# 它们的移动方向均随机
# 乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
# 当移动到场景边缘，自动向反方向移动
# 乌龟初始化体力为100（上限）
# 乌龟每移动一次，体力消耗1
# 当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
# 鱼暂不计算体力
# 当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束


# import random as r
# class Game:
#     def __init__(self,num1=1,num2=10):
#         self.turtle = []
#         self.fish = []
#         # 初始化鱼跟乌龟的位置
#         for i in range(num1):
#             self.turtle.append([r.randint(0,10),r.randint(0,10)])
#         for i in range(num2):
#             self.fish.append([r.randint(0,10),r.randint(0,10)])
#         self.run()
#
#     def run(self):
#         n = 100
#         while n > 0:
#             # 判断有多少条鱼位置与龟重合（被吃）
#             for i in self.turtle:
#                 if i in self.fish:
#                     f = self.fish.count(i)
#                     n += f*20
#                     print(f"有{f}条鱼被吃掉了...")
#                     self.fish.remove(i)
#                     if len(self.fish) == 0:
#                         break
#             # 判断还有没有鱼
#             if len(self.fish) == 0:
#                 print("鱼都被吃光了！游戏结束！")
#                 break
#             for i in self.turtle:       # 乌龟的随机移动
#                 step = [-2,-1,1,2]
#                 x = r.choice(step)
#                 y = r.choice(step)
#                 i[0] += x
#                 i[1] += y
#                 if i[0]<0 or i[0]>10:
#                     i[0] -= x*2
#                 if i[1]<0 or i[1]>10:
#                     i[1] -= x*2
#             for i in self.fish:         # 鱼的随机移动
#                 x = r.randint(-1,1)
#                 y = r.randint(-1,1)
#                 i[0] += x
#                 i[1] += y
#                 if i[0] < 0 or i[0] > 10:
#                     i[0] -= x * 2
#                 if i[1] < 0 or i[1] > 10:
#                     i[1] -= x * 2
#             n -= 1
#         else:
#             print(f"还有{len(self.fish)}条鱼没被吃掉了")
#             print("乌龟饿死了！game over~")
# go = Game()
# ------------------------------------------------------------------------------------------------
                                                                                # 组合（拾遗）
# 组合 定义第三个类对象来把前两个类对象组合在一起，类对象的属性会与方法重名时会覆盖方法，而这时组合就上场了

# class Turtle:
#     def __init__(self,x):
#         self.num = x
#
# class Fish:
#     def __init__(self,y):
#         self.num = y
#
# class Pool:
#     def __init__(self,x,y):
#         self.turtle = Turtle(x).num
#         self.fish = Fish(y).num
#         self.num()
#     def num(self):
#         print(f"水池里有{self.turtle}只乌龟，有{self.fish}条鱼。")
#
# pool = Pool(1,10)

# -----------------------------------------------------------------------------------------------
                                                                                    # 继承
# 继承
#   python中所有类默认继承object类，object称为顶级类或基类，其他子类叫做派生类
#   子类自动继承父类的属性和方法，如果子类对象重写父类方法属性，实例化子类对象时以子类对象为先
#   重写父类属性和方法后，可以通过 调用未绑定的父类方法 或 使用super（）函数 来调用已重写的属性和方法
#       相当于重写前把父类的属性和方法复制过来（自己悟的，不知道有没有错）
#   继承多个类时，第一个全部继承，后面的作为补充(继承与第一个里不同名的属性和方法)
#   __mro__方法 可以打印类的继承关系元祖
#   super()方法 调用父类的方法

# class Fish:
#     def __init__(self):
#         self.x = "鳃"
#         self.y = "鳍"
#         print("我是一条鱼...")
# class Salmon(Fish):
#     def __init__(self):
#         # Fish.__init__(self)     # 调用未绑定的父类方法（方法一）
#         super().__init__()        # 使用super（）函数（方法二）
#         self.print_xy()
#     def print_xy(self):
#         print("我是一条三文鱼...")
#         print("鱼有的我也有:",self.x,self.y)
# s = Salmon()

# ---------------------------------------------------------------------------------------------------
                                                                                # 类的内置函数
# 类对象相关的BIF（内置函数）

# ------------------------------------------------------------
# issubclass(class,classinfo),检查参数一是否为参数二的子类
# 1.一个类可以认为是它本身的子类 2.classinfo可以是类对象组成的元组，只要class in classinfo则返回True
class A:
    pass
class B(A):
    pass
class C:
    pass
# print(issubclass(A,B))  # A不是B的子类
# print(issubclass(B,A))  # B是A的子类
# print(issubclass(B,B))  # B是B自身的子类
# print(issubclass(B,C))  # B不是C的子类
# ------------------------------------------------------------
# isinstance(object,classinfo),检查实例对象是否属于类对象（classinfo可以是类对象组成的元组）
# 1.object需要是实例化对象，否则永远返回False 2.classinfo如果不是类对象或类对象组成的元组是会抛出TypeError异常
# b = B()
# print(isinstance(b,B))
# print(isinstance(b,A))  # 因为B继承于A，所以b也是A的实例化对象
# print(isinstance(b,C))
# ------------------------------------------------------------
# hasattr（object,name）,检查类对象是否有某属性
class D:
    a = 0
    def __init__(self,x=0):
        self.b = x
d = D()
# print(hasattr(D,"a"))
# print(hasattr(D,"b"))   # 没实例化前没有构造属性
# print(hasattr(d,"b"))   # 实例化后，属性可检查可出来
# ------------------------------------------------------------
# getattr(object,name[,default]),返回类对象的属性值，若属性不存在会报错，设置参数三默认值则返回默认值而不报错
# print(getattr(d,'b'))
# print(getattr(d,'d','您访问的属性不存在...'))
# ------------------------------------------------------------
# setattr(object,name,value),实例化对象增加属性，若本来就有则覆盖掉,返回值None
# setattr(d,'e',100)
# print(getattr(d,'e',100))
# ------------------------------------------------------------
# delattr(object,name),删除实例化对象的属性
# delattr(d,'e')
# print(getattr(d,'e','您访问的属性不存在...'))
# ------------------------------------------------------------
# property(fget=None,fset=None,fdel=None,doc=None),通过属性来设置属性的函数
# 设置属性来设置定义好的属性，第一个参数是获取属性的方法，第二个是设置属性的方法，第三个是删除属性的方法
# 优点是要修改类对象时，如外部调用的是封装的属性x，则只需内部修改外部无需更改即可同时更新，就不用修改外部调用接口

# class E:
#     def __init__(self,size=10):
#         self.size = size
#     def getSize(self):
#         return self.size
#     def setSize(self,value):
#         self.size = value
#     def delSize(self):
#         del self.size
#     x = property(getSize,setSize,delSize)
# e = E()
# print(e.getSize())  # 普通的通过方法getSize方法访问属性
# print(e.x)          # 通过property函数调用getSize方法访问属性
# e.setSize(20)       # 普通的通过方法setSize方法修改属性
# print(e.getSize())
# e.delSize()         # 普通的通过方法delSize方法删除属性
# print(getattr(e,'size','没有找到该属性...'))
# e.x = 30            # 通过property函数调用setSize方法修改属性
# print(e.x)
# del e.x             # 通过property函数调用delSize方法删除属性
# print(getattr(e,'size','没有找到该属性...'))
