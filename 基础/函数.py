# -*-  codeing = utf-8 -*-
# @Time : 2021/3/9 下午 4:31
# @Author : 漫天烟华
# @File : 函数.py
# @Software : PyCharm


# 函数的作用: 封装代码，使代码能够快速常用


# 写一个打印一条横线的函数（打印"-"*50）

# def line():
#     print("-"*50)
# line()

# 写一个函数，可以通过输入的参数，打印自定义行数的横线，要求调用上面的函数。
'''
def lines(n):
    a = 0
    while a<n:
        line()
        a += 1
lines(3)
'''


# 写一个函数，求三个数的和
'''
def sum_3gs(a,b,c):
    return a+b+c

# 写一个函数，求三个数的平均值，要求调用求三个数的和的函数
def pingjun_three(a,b,c):
    sum = sum_3gs(a,b,c)
    pjz = sum / 3
    return pjz
print(pingjun_three(11,22,33))
'''


# ------------------------------------------------------------------------------------------------------------
                                                                                        # 全局变量与局部变量
# 全局变量与局部变量

# a = 100
# def test1():
#     a = 300
#     print(a)
#     a = 200
#     print(a)     #优先使用局部变量
#
# def test2():
#     print(a)     #局部变量只在函数内生效，test1虽然修改过a，但是test2仍然是全局变量的值
#
# def test3():
#     global a     #（global 变量名）可以实现在函数内修改全局变量
#     a = 50
#     print(a)
#
# def test4():
#     print(a)     #这里因为test3修改过全局变量，使用新的变量
# test1()
# test2()
# test3()
# test4()

# 补充: 若没有global声明，在函数内重新赋值不能改变全局变量，但是非重新赋值的其他方法可以改变全局变量
# 即可变类型可通过增删改等方式在函数内对全局变量进行修改，而无需global声明
# a = [1,2,3]
# def local_a():
#     a = []
#     print(a)
#     return a
# local_a()
# print(a)
# def add_a():
#     a.append(4)
#     print(a)
#     a[1] = 9
#     print(a)
#     a.clear()
#     print(a)
#     return a
# add_a()
# print(a)


# ------------------------------------------------------------------------------------------------------------
                                                                                     # 函数说明文档
# 函数说明文档，在函数定义的第一行插入多行文字即可定义，通过help（函数名）来查看
# def main():
#     '''这是函数说明'''
#     print('月舒是笨蛋')
# 在定义说明文档时，打了多行注释的引号后直接回车时，会有说明文档模板，用以说明函数、参数以及返回值的作用
# def sum_2(number1,number2):
#     '''
#     求两个数的和
#     :param number1: 第一个待求和参数
#     :param number2: 第二个待求和参数
#     :return: 返回两参数的和
#     '''
#     return number1+number2
# help(main)
# help(sum_2)


# ------------------------------------------------------------------------------------------------------------
# 函数的参数 （位置参数、关键字参数、缺省参数、不定长参数）                                     # 函数参数详解

# 位置参数: 调用函数时根据函数定义的参数位置来传递参数，传递参数和定义参数的顺序及个数必须一致
# def info(name,age,gender):
#     print("您的用户名为%s，年龄为%s，性别为%s"%(name,age,gender))
# info("Tom",27,"男")
# info(27,"Tom","男")          # 传入参数位置顺序与定义参数不同时，传入的数据无意义
# info("John",16,"男","上海")   # 传入参数比定义参数多或者少，都会报错


# 关键字参数: 定义与位置参数例子一致，调用时以（键=值）形式加以指定
# 如果有为位置参数时，必须放在关键字参数前面，而关键字参数之间没有先后顺序
# def info(name,age,gender,city):
#     print(f"您的用户名为{name}，年龄为{age}，性别为{gender}，城市为{city}")
# info(city="杭州",age=27,gender="女",name="Rose")
# info("Ben",35,city="苏州",gender="男")


# 缺省参数: 也叫默认参数，指在定义函数时为参数提供默认值，调用参数时可不传入该参数的值
# 缺省函数调用时，如果为缺省参数传值则本次调用使用传入值，无传值则使用默认值
# 注意事项（参数位置）： 调用函数时，位置参数必须在关键字参数前面，缺省参数形参要在位置参数后、不定长参数前
# def info(name,age,city,gender="男"):
#     print(f"您的用户名为{name}，年龄为{age}，城市为{city}，性别为{gender}")
# info("Ben",city="苏州",age=26)
# info("John",16,"上海",gender="女")


# 不定长参数: 又叫可变参数，可以在调用参数时传入0个或多个参数，有以下两种形式
# 不定长位置参数，*args只接收位置参数,传入的参数为一个元组tuple()
# def info(*args):
#     print(args)
# info(233)
# info("Ben","苏州")
# info("上海","John","女",16)
# info()
# 不定长关键字参数，**kwargs只接收关键字参数，传入的参数为一个字典dict{}
# def info(**kwargs):
#     print(kwargs)
# info(name="Ben",city="苏州")
# info(city="上海",name="John",gender="女",age=16)
# info()

# 多种参数定义函数实例:
# def register(name,age,country='CN',course='python',*args,**kwargs):
#     print("----注册学生信息------")
#     print("姓名:", name)
#     print("年龄:", age)
#     print("国籍:", country)
#     print("课程:", course)
#     if len(args) or len(kwargs) != 0:
#         print('其他信息:')
#     if len(args) != 0:
#         print(args)
#     if len(kwargs) != 0:
#         print(kwargs)
# register("李明",19)
# register("Drake",18,Job="police",sex="男")
# register("Amy",18,'EN','Java',13600131314, "女")
# register("Mike",19,"USA","C#","党员",phone=14456789521,sex="男")


# ------------------------------------------------------------------------------------------------------------

# 多元素的容器都可以拆包（包括字符串、列表、元组、字典、集合）                        # 拆包(解包)和交换变量值
# str1 = 'DJ'
# list1 = [1,2]
# tuple1 = (3,4)
# dict1 = {'age':11,'name':'Lisa'}
# set1 = {5,6}
# i,j = str1
# a,b = list1
# c,d = tuple1
# e,f = dict1
# g,h = set1
# print('',a,b,'\n',c,d,'\n',g,h,'\n',i,j)
# print(e,dict1[e],f,dict1[f])



# 交换两个变量的值的两个方法

# 方法一: 定义中间变量的方法，临时存储a或b的值
# a = 100
# b = 200
# print(f'交换前: a = {a}   b = {b}')
# c = a
# a = b
# b = c
# del c
# print(f'交换后: a = {a}   b = {b}')

# 方法二: 同时交换赋值
# c = 123
# d = 456
# c,d = d,c
# print(c,d)


# ------------------------------------------------------------------------------------------------------------
