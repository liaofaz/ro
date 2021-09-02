# 推导式的作用:简化代码
# 在Python中，推导式适用于列表、字典、集合（可变类型，元祖不可变）


# ----------------------------------------------------------------------------
# 列表推导式: 用一个表达式来 创建 或 控制 一个有规律的列表

# 例子:创建一个0-10的列表
# 1、用while循环实现
# list1 = []
# n = 0
# while n<=10:
#     list1.append(n)
#     n+=1
# print('list1 = ',list1)
# ----------------------------
# 2、用for循环实现
# list2 = []
# for i in range(11):
#     list2.append(i)
# print('list2 = ',list2)
# ----------------------------
# 3、用列表推导式实现
# list3 = [i for i in range(11)]
# print('list3 = ',list3)


# 例子二:创建一个0-10的偶数列表
# list4 = [i for i in range(0,11) if i%2 == 0]
# print('list4 = ',list4)

# ----------------------------------------------------------------------------

# 字典推导式: 快速合并列表为字典，或提取字典中的目标数据

# 用普通方法合并两个列表为字典
# list1 = ['name','age','gender']
# list2 = ['Albert','26','man']
# dict1 = {}
# for i in list1:
#     for j in list2:
#         dict1[i] = j
# print('dict1 = ',dict1)

# 用字典推导式合并两个列表
# 如果两个列表元素个数不一致，使用元素多的列表下标会报错，所以增加判断以使用元素少的列表的下标
# list1 = ['name','age','gender']
# list2 = ['Albert','26','man']
# if len(list1) <= len(list2):
#     x = range(len(list1))
# else:
#     x = range(len(list2))
# dict2 = { list1[i]:list2[i] for i in x}
# print('dict2 = ',dict2)

# 例子二: 创建一个字典，要求key为1-5的数字，value为key的2次方
# dict3 = {i:i**2 for i in range(1,6)}
# print(dict3)

# 例子三: 提取字典中的目标数据(提取值大于200的数据)
# counts = {'MBP':268,'HP':125,'DELL':201,'Lenovo':199,'acer':99}
# count1 = {key:value for key, value in counts.items() if value > 200}
# print(count1)

# ----------------------------------------------------------------------------

# 集合推导式
# 例:创建一个元素为列表元素平方的集合
# list_set = [1,1,2,3]
# set1 = {i**2 for i in list_set}
# print(set1)



