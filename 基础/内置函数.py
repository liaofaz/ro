# -----------------------------------------------------------------
# Python 小函数
# abs()函数可以求数字的绝对值
# print(abs(-3.6))
# round()函数可以求数字四舍五入后的值
# print(round(3.14))

# -----------------------------------------------------------------

# 递归函数: 函数内部调用自己，且必须有出口,例子:
# def sum_n(n):
#     if n==1:
#         return 1
#     return n + sum_n(n-1)
# print(sum_n(10))

# -----------------------------------------------------------------

# lambda函数: 匿名函数,参数可有可无，能接受多个参数但是只能返回一个参数,参数设置与普通函数相同
# 不传入参数的使用方式:
# print((lambda :'不传入参数直接return')())
# 设置缺省函数:
# print((lambda country = 'China':f'您来自{country}')())
# print((lambda country = 'China':f'您来自{country}')('Britain'))

# g = lambda x:x+1
# print(g(1))
# g = lambda x:x==1
# print(g(3))
# print((lambda x:x==1)(1))

# lambda 中if-elif-if
# 一般情况下：
# def function():
#     if 条件1:
#         语句1
#     elif 条件2:
#         语句2
#     else:
#         语句3

# 但如果要使用lambda一行表示if多条件，则:
# lambda x: 语句1 if 条件1 else 语句2 if 条件2 else 语句3
# 实际上是下面这样表达
# lambda x: 语句1 if 条件1 else ( 语句2 if 条件2 else 语句3 )

# ---------------------------------------------
# 实例： 随机数为奇数则输出x，偶数则输出-x
# from random import randint
# a = lambda x:x if x%2 else -x
# b = randint(0,1000)
# print(b,a(b))


# ----------------------------------------------------------------------------------------------------------
                                                                                              # filter函数

# filter函数会将过滤条件函数依次作用于每一个待过滤序列的元素，返回符合要求的过滤值。函数不改变原对象值，只返回过滤值
# filter(过滤条件函数，可迭代对象)
# 过滤条件函数返回值为True则保留，返回值为False则舍弃
# --------------------------------------------
# 例子: 过滤能被3整除的数
# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# print(list(filter(lambda x: x % 3 == 0, foo)))
# print(foo)          # 不改变原list，而是返回一个新list
# --------------------------------------------
# 例子: 删除1-100的质数
# L=range(1,101)
# def not_prime_number(n):
#     flag=1
#     for i in range(2,n):
#         if n%i==0:
#             flag=0
#     if flag==0:
#         return n
# print(list(filter(not_prime_number,L)))


# ----------------------------------------------------------------------------------------------------------
                                                                                                # map函数

# map(function,iterable,...)是python内置函数，会根据提供的函数对指定的序列做映射
# 简单地说，就是把可迭代对象的每一个元素按设定函数处理一遍，然后返回一个新的可迭代对象
# -----------------------------------------------------------------------
# 例子: 把列表各元素乘3,乘2（lambda和普通方法）
# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
# def foo_x3(x):
#     return x*3
# print(list(map(foo_x3,foo)))
# print(list(map(lambda x: x * 2,foo)))
# print(foo)      # map不改变原list，而是返回一个新list
# -----------------------------------------------------------------------
# 规范名字格式，首字母大写，其余小写
# name_list={'tony','cHarLIE','rachAEl'}
# def format_name(name):
#     new_name=name[0].upper()+name[1:].lower()
#     return new_name
# print (list(map(format_name,name_list)))
# -----------------------------------------------------------------------
# 合并列表为元组、字典
# print(list(map(lambda x,y:(x,y),[2,4,6],[3,2,1])))
# print(list(map(lambda x,y:{x: y},[2,4,6],[3,2,1])))
# -----------------------------------------------------------------------
# 把字符串、字典的键转换成后面三者,列表、元组、集合的相互转换(转换后的元素可以是各种类型,除了字典)
# 也可把全部元素变成字符串
# print(list(map(int,'1234')))
# print(list(map(str,(1,2,3))))
# print(tuple(map(int,[1,2,3])))
# print(set(map(str,{1:11,3:33,5:55})))


# ----------------------------------------------------------------------------------------------------------
                                                                                            # sorted函数
# sorted() 函数对所有可迭代的对象进行排序操作
# sorted(iterable, cmp=None, key=None, reverse=False)
# 参数说明：
# iterable -- 可迭代对象。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
# -----------------------------------------------------------------------
# sorted函数返回的是一个列表
# tuple1 = (1,2,3,6,5,4,9,7,8)
# print(sorted(tuple1))
# dict1 = {'b':3,'a':2,'d':4,'c':1}
# print(sorted(dict1))
# set1 = {1,2,3,6,5,4,9,7,8}
# print(sorted(set1,reverse=True))
# a=[('b',3),('a',2),('d',4),('c',1)]
# print(sorted(a,key=lambda x:x[0]))      # 按元组第一个元素排序
# print(sorted(a,key=lambda x:x[1]))      # 按元组第二个元素排序

# ----------------------
# a = [
#     '@askziye',
#     '@fuumiisc',
#     '@yyish',
#     '@15nichi',
#     '@1919_decoy',
#     '@skskdi12z',
#     '@sakura_oriko',
#     '@abisswalker8',
#     '@gcmzi',
#     '@all_need_is',
#     '@korokoroudon',
#     '@0207_yuyuyuyu',
#     '@hamident83hami',
#     '@Lyytoaoitori（猫猫）',
#     '@iwa_to_mushi',
#     '@navigavi',
#     '@chicken_utk',
#     '@SuJ_0',
#     '@iki___runrun',
#     '@color_isnothing',
#     '@Rellakinoko',
#     '@9Jedit',
# ]
# a = sorted(a, key=lambda x: x[1])           # 单重排序效果
# b = sorted(a, key=lambda x: (x[1], x[2]))   # 多重排序效果
# for i in range(len(a)):
#     print(f'{a[i]}        {b[i]}')

# -----------------------------------------------------------------------
# 创建、打印一个元素为0-999随机整数的100个元素的列表，
# 并将偶数按顺序排序打印，奇数以倒序排序打印
# from random import randint
# list1 = []
# for i in range(100):
#     list1.append(randint(0, 999))
# print(list1)
# list2 = sorted(list(filter(lambda x:x%2==0,list1)))
# list3 = sorted(list(filter(lambda x:x%2,list1)),reverse=True)
# print(list2)
# print(list3)
# # 下面是读错题意的产物，可跳过
# list_t = sorted(list1,key=lambda x:-x if x%2 else x)
# list4 = list(filter(lambda x:x%2==0,list_t)) + list(filter(lambda x:x%2,list_t))
# print(list4)


# ----------------------------------------------------------------------------------------------------------
