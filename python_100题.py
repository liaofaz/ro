# Python 100题
# ------------------

# 第一题: 有数字 1、2、3、4 ，能组成多少个互不相同且无重复数字的三位数？都是多少？

# num_set=set()
# cou=0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             for l in range(1,5):
#                 if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
#                     res=i*1000+j*100+k*10+l
#                     num_set.add(res)
#                     cou+=1
# print(sorted(list(num_set)), f'共有{cou}个')

# ------------------
# 给定两个整数n和k，返回[1,n]范围内的k个数字的所有可能组合，其中1<=n<=30,1<=k<=n
# 例: n=3,k=2    返回[1,3]范围内所有可能的2个数字组合，[1,3],[1,2],[2,3]

# def nk(n=5, k=3):
#     lt = list(range(1, n + 1))
#     if k <= 1:
#         return [[i] for i in lt]
#     elif k == n:
#         return [lt]
#     result = []
#     temp = lt[:k]
#     while temp[0] <= n - k + 1:
#         num_l = lt.index(temp[-1])
#         for i in lt[num_l:]:
#             temp[-1] = i
#             result.append(temp[:])
#         else:
#             u = 0
#             while k - u - 1 >= 0:
#                 index = k - u - 1   # 开始是最后那个元素
#                 if temp[index] < n - u:
#                     temp[index] += 1
#                     while u > 0:
#                         u -= 1
#                         temp[k - u - 1] = temp[k - u - 2] + 1
#                     break
#                 elif index < 0:
#                     break
#                 else:
#                     u += 1
#             else:
#                 return result
#
#
# print(nk(7, 5))
# print(nk(6, 4))
# print(nk(6, 3))
# print(nk(5, 2))
# print(nk(5, 1))
# print(nk(5, 5))

# ----------------------------------------------------------------------------------------------------------------------

# 第二题: 企业发放的奖金根据利润提成。利润 (I) ：
# 低于或等于 10 万元时，奖金可提 10%；
# 高于 10 万元，低于 20 万元时，低于 10 万元的部分按 10%提成，高于 10万元的部分，可提成 7.5%；
# 20 万到 40 万之间时，高于 20 万元的部分，可提成 5%；
# 40 万到 60 万之间时，高于 40 万元的部分，可提成 3%；
# 60 万到 100 万之间时，高于 60 万元的部分，可提成 1.5%，
# 高于 100 万元时，超过 100 万元的部分按 1%提成，
# 从键盘输入当月利润 I ，求应发放奖金总数？

# I = eval(input('请输入利润:'))
# bonus = 0
#
# a = 100000 * 10/100
# b = 100000 * 7.5/100
# c = 200000 * 5/100
# d = 200000 * 3/100
# e = 400000 * 1.5/100
#
# if I <=100000:
#     bonus = I * 10/100
# elif 100000 < I <=200000:
#     bonus = (I - 100000) * 7.5/100 + a
# elif 200000 < I <= 400000:
#     bonus = (I - 200000) * 5/100 + a + b
# elif 400000 < I <= 600000:
#     bonus = (I - 400000) * 3/100 + a + b + c
# elif 600000 < I <= 1000000:
#     bonus = (I - 600000) * 1.5/100 + a + b + c + d
# elif I > 1000000:
#     bonus = (I - 1000000) * 1/100 + a + b + c + d + e
# else:
#     print('请输入正确的利润数字！！')
# print('应发奖金为:%.2f元'%bonus)

# ----------------------------------------------------------------------------------------------------------------------

# 第三题: 一个整数，它加上 100 后是一个完全平方数，再加上 168 又是一个完全平方数，请问该数是多少？

# n = 0
# for i in range(100):
#     n = i * i
#     if n > 100:
#         for j in range(i,100):
#             m = j * j
#             if m == n + 168:
#                 print('该数为:',n-100)

# ----------------------------------------------------------------------------------------------------------------------

# 第四题: 输入某年某月某日，判断这一天是这一年的第几天？

# def is_leap_year(year):         # 网上抄的，不是自己做的~~
#     """
#     判断指定的年份是不是闰年
#     :param year: 年份
#     :return: 闰年返回True平年返回False
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# def which_day(year, month, date):
#     """
#     计算传入的日期是这一年的第几天
#     :param year: 年
#     :param month: 月
#     :param date: 日
#     :return: 第几天
#     """
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date
#
#
# today = which_day(2021, 6, 8)
# print(f'这是当年的第{today}天')

# ----------------------------------------------------------------------------------------------------------------------

# 第五题: 输入三个整数 x，y，z，请把这三个数由小到大输出

# while True:
#     ns = input('请输入三个数，以英文逗号隔开:')
#     ns = ns.split(",")
#     if len(ns) == 3:
#         try:
#             ns = [int(i) for i in ns]
#             ns.sort()
#             for i in ns:
#                 print(i,end='\t')
#             break
#         except ValueError:
#             print('请输入3个数！！')
#     else:
#         print('输入不对呀,检查一下~')

# ----------------------------------------------------------------------------------------------------------------------

# 第六题: 用 *号输出字母 C的图案

# c = '''
#
#        ****
#    ***       **
#  **
# **
# **
#  **
#    ***       **
#        ****
# '''
# print(c)

# ----------------------------------------------------------------------------------------------------------------------

# 第七题: 输出特殊图案，请在 c 环境中运行，看一看， Very Beautiful!

# ----------------------------------------------------------------------------------------------------------------------

# 第八题: 输出 9*9 口诀表

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}=',j*i,end='\t')
#     print()

# ----------------------------------------------------------------------------------------------------------------------

# 第九题: 要求输出国际象棋棋盘

# for i in range(4):
#     print('  oo  oo  oo  oo')
#     print('oo  oo  oo  oo  ')

# ----------------------------------------------------------------------------------------------------------------------

# 第十题: 打印楼梯，同时在楼梯上方打印两个笑脸

# ----------------------------------------------------------------------------------------------------------------------

# 第十一题: 古典问题：有一对兔子，从出生后第 3 个月起每个月都生一对兔子，小兔子长到
# 第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？(斐波那契数列)

# def fibs(n=10):
#     n1 = 0
#     n2 = 1
#     c = 0
#     while True:
#         c += 1
#         n1, n2 = n2, n1+n2
#         if c > n:
#             break
#         yield n1
# for i in fibs():
#     print(i)

# ----------------------------------------------------------------------------------------------------------------------

# 第十二题: 判断 101-200 之间有多少个素数，并输出所有素数

# n = 0
# for i in range(101,201):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         elif i % j > 0 and j == (i - 1):
#             print(i)
#             n += 1
# print(f'共{n}个')

# ----------------------------------------------------------------------------------------------------------------------

# 第十三题: 打印出所有的“水仙花数” ，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
# 例如： 153 是一个“水仙花数” ，因为 153 = 1^3 ＋ 5^3 ＋ 3^3

# for i in range(100,1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i % 10
#     if i == a**3 + b**3 + c**3:
#         print(i)

# ----------------------------------------------------------------------------------------------------------------------

# 第十四题: 将一个正整数分解质因数。例如：输入 90, 打印出 90=2*3*3*5

# def pf(n):
#     n = n
#     list_n = []
#     len_l = 0
#     while len_l == len(list_n):
#         for i in range(2, n):
#             if n % i == 0:
#                 list_n.append(i)
#                 n = n // i
#                 break
#         len_l += 1
#     list_n.append(n)
#     string = ' * '.join([str(i) for i in list_n])
#     return string
#
#
# while True:
#     try:
#         n = eval(input('请输入一个大于2的正整数:'))
#         if type(n) == int and n > 2:
#             print(f'{n} = {pf(n)}')
#             break
#         else:
#             print('你肯定没按我给的范围输入，快点重新输入！')
#     except ValueError:
#         print('再不按规矩输入就打爆你狗头！')

# ----------------------------------------------------------------------------------------------------------------------

# 第十五题: 利用条件运算符的嵌套来完成此题,学习成绩>=90分的同学用A表示,60-89分之间的用B表示,60分以下的用C表示。

# n = int(input('请输入分数:'))
# if n >= 90:
#     print('A')
# elif 60 <= n <= 89:
#     print('B')
# else:
#     print('C')

# ----------------------------------------------------------------------------------------------------------------------

# 第十六题: 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数


# ----------------------------------------------------------------------------------------------------------------------


# 第十七题: 求 s=a + aa + aaa + aaaa + aa...a的值,其中a是一个数字.
# 例如 2+22+222+2222+22222(此时,共有5个数相加)，几个数相加有键盘控制

# ----------------------------------------------------------------------------------------------------------------------

# 第十八题: 一个数如果恰好等于它的因子之和，这个数就称为“完数” 。例如 6=1＋2＋3。编程找出 1000以内的所有完数

# ----------------------------------------------------------------------------------------------------------------------

# 第十九题: 一球从 100 米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
# 第 10 次落地时，共经过多少米？第 10 次反弹多高？

# ----------------------------------------------------------------------------------------------------------------------

# 第二十题:猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，
# 又多吃了一个。 以后每天早上都吃了前一天剩下的一半多一个。到第 10 天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少

# ----------------------------------------------------------------------------------------------------------------------

# 第二十一题: 两个乒乓球队进行比赛，各出三人。甲队为 a,b,c 三人，乙队为 x,y,z 三人。已抽签决定比赛名单。
# 有人向队员打听比赛的名单。 a 说他不和 x 比，c 说他不和 x,z 比，请编程序找出三队赛手的名单

# ----------------------------------------------------------------------------------------------------------------------

# 第二十二题: 有一分数序列： 2/1 ，3/2 ，5/3 ，8/5 ，13/8 ，21/13... 求出这个数列的前20项之和

# ----------------------------------------------------------------------------------------------------------------------

# 第二十三题: 求1+2!+3!+...+20! 的和

# ----------------------------------------------------------------------------------------------------------------------

# 第二十四题: 利用递归方法求 5!

# ----------------------------------------------------------------------------------------------------------------------

# 第二十五题: 利用递归函数调用方式，将所输入的 5 个字符，以相反顺序打印出来

# ----------------------------------------------------------------------------------------------------------------------
# 第二十六题: 有 5 个人坐在一起，问第五个人多少岁？他说比第 4 个人大 2 岁。问第 4 个人岁数，他说比第 3 个人大 2 岁。
# 问第三个人，又说比第 2 人大两岁。问第 2 个人，说比第一个人大两岁。最后问第一个人，他说是 10 岁。请问第五个人多大？
# ----------------------------------------------------------------------------------------------------------------------
# 第二十七题: 给一个不多于 5 位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
# ----------------------------------------------------------------------------------------------------------------------
# 第二十八题: 一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同
# ----------------------------------------------------------------------------------------------------------------------
# 第二十九题: 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
# ----------------------------------------------------------------------------------------------------------------------
# 第三十题: Press any key to change color, do you want to try it. Please hurry up!
# ----------------------------------------------------------------------------------------------------------------------
# 第三十一题: 学习 gotoxy() 与 clrscr() 函数
# ----------------------------------------------------------------------------------------------------------------------
# 第三十二题: 文本颜色设置
# ----------------------------------------------------------------------------------------------------------------------
# 第三十三题: 求 100 之内的素数
# ----------------------------------------------------------------------------------------------------------------------
# 第三十四题: 对 10 个数进行排序
# ----------------------------------------------------------------------------------------------------------------------
# 第三十五题: 求一个 3*3 矩阵对角线元素之和
# ----------------------------------------------------------------------------------------------------------------------
# 第三十六题: 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中
# ----------------------------------------------------------------------------------------------------------------------
# 第三十七题: 将一个数组逆序输出
# ----------------------------------------------------------------------------------------------------------------------
# 第三十八题: 学习 static 定义静态变量的用法
# ----------------------------------------------------------------------------------------------------------------------
# 第三十九题: 学习使用 auto 定义变量的用法
# ----------------------------------------------------------------------------------------------------------------------
# 第四十题: 学习使用 static 的另一用法
# ----------------------------------------------------------------------------------------------------------------------
# 第四十一题: 学习使用 external 的用法
# ----------------------------------------------------------------------------------------------------------------------
# 第四十二题: 学习使用 register 定义变量的方法
# ----------------------------------------------------------------------------------------------------------------------
# 第四十三题: 宏 #define 命令练习 (1)
# ----------------------------------------------------------------------------------------------------------------------
# 第四十四题: 学习使用按位与 &
# ----------------------------------------------------------------------------------------------------------------------
# 第四十五题: 学习使用按位或 |
# ----------------------------------------------------------------------------------------------------------------------
# 第四十六题: 学习使用按位异或 ^
# ----------------------------------------------------------------------------------------------------------------------
# 第四十七题: 取一个整数 a 从右端开始的 4～7位
# ----------------------------------------------------------------------------------------------------------------------
# 第四十八题: 学习使用按位取反 ~
# ----------------------------------------------------------------------------------------------------------------------
# 第四十九题: 画图，学用 circle 画圆形
# ----------------------------------------------------------------------------------------------------------------------
# 第五十题: 画图，学用 line 画直线
# ----------------------------------------------------------------------------------------------------------------------
# 第五十一题: 画图，学用 rectangle 画方形
# ----------------------------------------------------------------------------------------------------------------------
# 第五十二题: 画椭圆 ellipse
# ----------------------------------------------------------------------------------------------------------------------
# 第五十三题: 利用 ellipse and rectangle 画图
# ----------------------------------------------------------------------------------------------------------------------
# 第五十四题: 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
# ----------------------------------------------------------------------------------------------------------------------
# 第五十五题: 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m个数变成最前面的 m个数
# ----------------------------------------------------------------------------------------------------------------------
# 第五十六题: 有 n 个人围成一圈，顺序排号。从第一个人开始报数（从 1 到 3 报数），凡报到 3
# 的人退出圈子，问最后留下的是原来第几号的那位
# ----------------------------------------------------------------------------------------------------------------------
# 第五十七题: 写一个函数， 求一个字符串的长度， 在 main 函数中输入字符串， 并输出其长度
# ----------------------------------------------------------------------------------------------------------------------
# 第五十八题: 编写 input() 和 output() 函数输入，输出 5 个学生的数据记录
# ----------------------------------------------------------------------------------------------------------------------
# 第五十九题: 创建一个链表
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
