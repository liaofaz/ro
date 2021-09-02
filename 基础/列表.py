# -*-  codeing = utf-8 -*-
# @Time : 2021/3/6 上午 6:02
# @Author : 漫天烟华
# @File : 列表.py
# @Software : PyCharm

#------【增加】列表元素的三种方法（append、extend、insert）-----

'''       #用【append】增加列表元素

name = ["小赵","小钱","小孙","小李"]
print("---------增加前列表：---------")
print(name)

list1.append(input("请输入一个名字："))      #list.append()  在列表末尾追加一个元素，这个元素甚至可以是列表，
print("---------增加后的列表：---------")
print(name)
'''



'''      #用【extend】增加列表元素
a = [1,2]
b = [3,4]
a.append(b)      #将列表b当做一个元素，加入a列表末尾中

print(a)

a.extend(b)      #将列表b中的元素，逐个追加到a列表末尾中
print(a)

'''

#
#
# #用【insert】增加列表元素
#
# a = [1,2,3]
# a.insert(1,[1,2,3])     #第一个变量表示下标，第二个变量表示元素（对象）
# print(a)                #insert(参数1,参数2)作用：给指定下标位置的前面插入元素
#
#





#------【删除】列表元素的三种方法（del、pop、remove）-----
'''

day = [ "星期一" , "星期二" , "星期三" , "星期四" , "星期五" ]
print("---------删除前工作日列表：---------")
print(day)

#del day[2]           #del 删除指定下标位置中的元素
#day.pop()            #弹出（删除）末尾的最后一个元素
#day.remove("星期四")   #直接删除指定内容的元素（如果有多个同名元素，只删除第一个）

print("---------删除后的工作日列表：---------")
print(day)

'''



#------【修改】列表元素的方法-----
'''
name = [ "小赵" , "小钱" , "小孙" , "小李" ]
print("---------修改前名字列表：---------")
print(name)

name[1] = "小朱"         #修改指定下标的元素内容

print("---------修改后的名字列表：---------")
print(name)
'''



#------【查找】列表元素的方法-----
'''
name = [ "小赵" , "小钱" , "小孙" , "小李" ]
if input("请输入您要查找的人的名字：") in name :
    print(" ✓ 您查找的人已找到")
else :
    print(" X 没有找到您查找的人")

'''
#【index】查找目标元素在指定下标范围的哪个位置（找不到会报错）
'''
x = ["a","b","c","a","d"]
print(x.index("a",2,4))       #在指定下标范围内查找指定元素，并返回其对应下标值。左边例子的下标范围为[2,4)
'''

'''
x = ["a","b","c","a","d"]
print(x.count("a"))            #查找元素在列表出现得到次数，【统计】目标元素的数量
print(x.count("c"))
'''


# -------------------------------------------------------

# copy()函数的作用: 用来备份列表
# 因为列表是可变类型，两者共同一个id，如果直接传递，修改其中一个两个都会改变

# list1 = [1,2,3,4,5]
# list2 = list1
# list1.append(7)
# print(list1)
# print(list2)
#
# list1 = [1,2,3,4,5]
# list2 = list1.copy()
# list1.append(6)
# print(list1)
# print(list2)


# -------------------------------------------------------


# 【列表的反转及排序】  (reverse , sort )
'''
a = [1,2,4,3,5]
print(a)

a.reverse()          #反转：将列表所有元素按倒序排序
print(a)

a.sort()             #将列表按【升序】排序
print(a)

a.sort(reverse=1)    #将列表按【降序】排序
print(a)

'''


#  将8位人随机分配到3个办公室的例子
'''
import random

offices = [[],[],[]]
teachers = ["a","b","c","d","e","f","g","h"]

for teacher in teachers :
    office = offices[random.randint(0, 2)]
    office.append(teacher)

n = 1
for office in offices :
    print("办公室%d的人数为%d，成员如下：" % (n,len(office)))
    n += 1
    for name in office :
        print(name,end="\t")
    print()
    print("-"*50)

'''


'''
#  【打印商品列表】

print("-----    商品列表    -----")

products = [["iphone",6888],["MacPro",14800],["小米6", 2499],["Coffee",31],["Book",60],["Nike",699]]

n = 0

for product in products :
    print(n,end="\t")
    n += 1
    for shangpin in product :
        print(shangpin,end="\t"*2)
    print()
'''




#
# #  打印购物清单
# shopping_Cart = []
# numbers = []
#
# while True:
#     print("-----    商品列表    -----")
#     products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
#     n = 0
#     for product in products:
#         print(n, end="\t")
#         n += 1
#         for shangpin in product:
#             print(shangpin, end="\t" * 2)
#         print()
#     print("如已挑选完毕，请输入q结束")
#     buy = input("请输入您想要购买的商品编号（0~5）：")
#     a_list = ["0","1","2","3","4","5","q"]
#     if buy not in a_list :
#         print("您输入有误，请正确输入！可输入内容有：0，1，2，3，4，5，q")
#         continue
#     numbers.append(buy)
#     if "q" in numbers :
#         break
# numbers.remove("q")
# numbers.sort()
#
# for number in numbers :
#     shopping_Cart.append(products[int(number)])
#
# n = 0
# print("---  你购买的商品清单如下  ---")
# for shangpin in shopping_Cart :
#     print(n,end="\t")
#     n += 1
#     for i in shangpin :
#         print(i,end="\t"*2)
#     print()
#
# sum = 0
# for i in shopping_Cart :
#     sum = sum + i[1]
# print("您购买的商品数量为%d，总价为%d"%(len(shopping_Cart),sum))


