# -*-  codeing = utf-8 -*-
# @Time : 2021/3/5 上午 5:45
# @Author : 漫天烟华
# @File : 练习.py
# @Software : PyCharm


# for循环有赋值功能
# for i in range(10):
#     pass
# print(i)


'''
for a in range(0,12,2) :              #for x in range(参数a，参数b，参数c)
    print(a)                          #表示[a,b)区间内每隔c个取一个（例：a，a+c，a+2c……），c可以为负数
for a in range(0,-12,-2) :
    print(a)
'''
#------------------------------------------

'''
name = 'China'
for b in name :
    print(b,end="\t")

'''
#------------------------------------------

'''
x = ["aa","bb","cc"]
for i in range(len(x)) :
    print(i,x[i])

'''







#------------------------------------------
'''       #whale循环求1~100的和
#------------------------------------------
sum = 0
n = 1
while n <= 100 :
    sum = sum + n
    n += 1
print("1~100的求和：%d"%sum)

'''
#------------------------------------------
'''        #for循环求1~100的和
#------------------------------------------
num = 0
for i in range(1,101):
    num = num + i
print("1~100的求和：%d"%num)
'''





'''
for i in "zoom":
    if i == "o":
        print("跳过")
        continue
    print(i)
'''
#------------------------------------------

#break:结束整个while循环     continue：结束本次循环（本次本命令后面的同层代码不予执行）




#使用for循环、while循环，打印九九乘法表：

#for循环：
# for a in range(1,10):
#     for b in range(1,10):
#         if a <= b:
#             print("%d*%d=%d"%(a,b,a*b),end="\t")
#     print("")

#while循环：
# a = 1
# b = 1
# while a <= 9:
#     while b <= 9:
#         if a <= b:
#             print("%d*%d=%d" % (a, b, a * b), end="\t")
#         b += 1
#     b = 1
#     a += 1
#     print("")

