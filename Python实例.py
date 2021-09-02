
# 传球游戏，随机生成一个1以内的浮点数，规定四个区域，落在哪个区域就输出对应名字，相邻两次输出不可相同

# import random
# number = random.random()
# n = 'y'
# while n == 'y' or n =='Y':
#     print('number:',number)
#     if 0<=number<0.25:
#         print('A')
#         number = random.randrange(25,100)/100
#         n = str(input('输入Y继续，输入N退出：'))
#     elif 0.25<=number<0.5:
#         print('B')
#         n = random.choice([(0, 25), (50, 100)])
#         number = random.randrange(*n)/100
#         n = str(input('输入Y继续，输入N退出：'))
#     elif 0.5<=number<0.75:
#         print('D')
#         n = random.choice([(0, 50), (75, 100)])
#         number = random.randrange(*n)/100
#         n = str(input('输入Y继续，输入N退出：'))
#     elif 0.75<=number<1:
#         print('E')
#         number = random.randrange(0, 75)/100
#         n = str(input('输入Y继续，输入N退出：'))
# print('游戏结束！')


# -------------------------------------------------------------------------------------------------
# 现有数列: 2/1,3/2,5/3,8/5,13/8,21/13,34/21......x/y(每一项x是前一项x+y的和，y是前一项的x)，求数列前20项的和
# --------------------
# x = 2
# y = 1
# sum = 0
# for i in range(20):
#     print("第 %d 次遍历"%(i+1))
#     sum = sum + x/y
#     print("x = %d , y = %d" % (x, y))
#     print(f"x/y = :{x}/{y}")
#     print(f"sum = {sum}")
#     x,y = (x + y),x
#     print("-"*30)
# print(f"sum = {sum}")

# -------------------------------------------------------------------------------------------------
# 创建、打印一个元素为0-999随机整数的100个元素的列表，
# 并将偶数按顺序排序打印，奇数以倒序排序打印
# --------------------
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

# -------------------------------------------------------------------------------------------------
# 以字母开头，长度为6~18之间的包含字母数字下划线的密码。若符合规则则输出正确提示并展示密码，否则提示错误
# --------------------
# import re
# while True:
#     password = input("请输入6~18位以字母开头，只能包含字母数字和下划线'_'的密码:")
#     rule = re.findall('^[a-zA-Z]\w{5,17}$',password)
#     if len(rule) != 0:
#         print(f'输入正确，您的密码为{rule[0]}')
#         break
#     else:
#         print('您的输入有误，请重新输入！\n\n')

# -------------------------------------------------------------------------------------------------
# 24小时倒计时器
# --------------------
# import time
# for h in range(24)[::-1]:
#     for m in range(60)[::-1]:
#         for s in range(60)[::-1]:
#             print('\r%02d : %02d : %02d '%(h,m,s),end='')
#             time.sleep(1)
# -------------------------------------------------------------------------------------------------
# 任意输入一个正整数，通过函数不断运算直至值为1
# --------------------
# def collatz(number):
#     if number % 2 == 0:
#         number = number//2
#     else:
#         number = number*3+1
#     print(number)
#     return number
# number = int(input('Enter number:'))
# n = 0
# while number > 1:
#     number = collatz(number)
#     n += 1
# else:
#     print(f'运算了{n}次，number=1啦~')

# -------------------------------------------------------------------------------------------------
# 杨辉三角（简陋版）
# --------------------
# def yhsj(n):
#     l1 = [1]
#     for i in range(1,n+1):
#         l2 = [''] * i
#         l2[0] = 1
#         if i>1:
#             for j in range(1,i-1):
#                 l2[j] = l1[j-1] + l1[j]
#         l2[i-1] = 1
#         print(l2)
#         l1 = l2
# yhsj(10)
# -------------------------------------------------------------------------------------------------
# 题目一:
# 从字符串中选出一组相同字符数最多的字符及个数。
# 例如：
# “aaabbbbcdddddd” ‘d’-----6
# “aabbc” ‘a-’----2
# “ss445666gg7” ‘ 6’-----3
# --------------------

# a = 'aaabbbbcdddddd'
# b = 'aabbc'
# c = 'ss445666gg7'
# s = None
# s_most = 0
# n = a
# for i in n:
#     cou = n.count(i)
#     if cou > s_most:
#         s_most = cou
#         s = i
# print(s,s_most)
# -------------------------------------------------------------------------------------------------
# 奇数金字塔
# --------------------
# cs = 10  # 请输入层数
# r = 0
# for i in range(1, cs*2,2):
#     r += i
# r = (r+i+2)*2   # 最后一个数的值+1
# ku = [str(i) for i in range(1, r, 2)]
# # print(ku)
# ceng = []
# ceng.append(['1'])
# n = 0
# for i in range(1, cs*2-2, 2):
#     n += i
#     ceng.append(ku[n:n+i+2])
# l_m = len(' '.join(ceng[-1]))   # 最后一行占的位置数
# for i in ceng:
#     print(' '.join(i).center(l_m))

# -------------------------------------------------------------------------------------------------
# 报数问题: 有n个人顺时针围成一圈，编号为1~n（n<=100）。开始时，所有人都坐着，从1号开始，坐着的顺时针报数（1，2，3），
# 报到3的人站起来，问最后一个坐着的人编号是多少？
# ------------------------（方法一: 递归函数）
# def bs_g(list_n, i=2):
#     if len(list_n) == 1:
#         return
#     if i >= len(list_n):
#         i = i - len(list_n)
#         return bs_g(list_n, i)
#     list_n.pop(i)
#     i += 2
#     return bs_g(list_n, i)
#
#
# n = 100   # 这里输入初始人数
# list_n = [i for i in range(1, n+1)]
# print(list_n)
#
# bs_g(list_n)
# print(list_n)
# ------------------------（方法二: 循环）
# n = 100       # 初始人数
# list_n = [i for i in range(1, n+1)]
# print(list_n)
# i = p = 2     # 要除掉的号数-1
# while len(list_n) > 1:
#     if i >= len(list_n):
#         i = i - len(list_n)
#         if i >= len(list_n):
#             i = i - len(list_n)
#     list_n.pop(i)
#     i += p
#
# print(list_n)

# -------------------------------------------------------------------------------------------------
# 约翰想给总奖金$851给他的三个员工以公平地考虑他们的缺席的天数时所考虑的时期。员工 A 缺勤18天数、B15天数和 C12天数。
# 缺席越多，奖金越低......
# 每个员工应该得到多少？约翰认为 A 应该收到$230， B $276， C$345因为230 * 18 = 276 * 15 = 345 * 12且230 + 276 + 345 = 851。
# 任务：
# 给定一个数组arr（每个员工的缺勤天数）和一个数字s（总奖金），该函数bonus(arr, s)将按照 John 的方式返回所有员工的公平奖金数组，其顺序与缺勤天数相同。
# s并且 的所有元素arr都是正整数。
# 例子：
# bonus([18, 15, 12], 851) -> [230, 276, 345]
# --------------------

# def bonus(arr, s):
#     temp = []
#     for i in range(s * 31):
#         for j in arr:
#             if i % j:
#                 break
#         else:   # 若上面的循环无break操作则执行以下
#             temp.append(i)
#     for i in temp:
#         if sum([i//n for n in arr]) == s:
#             bs = [i//n for n in arr]
#             print(bs)
# bonus([18, 15, 12], 851)            # [230, 276, 345]
# bonus([30, 27, 8, 14, 7], 34067)    # [2772, 3080, 10395, 5940, 11880]
# ---------------------
# def bonus(arr, s):
#     s /= sum(1/i for i in arr)
#     print([round(s/i) for i in arr])
#     return [round(s/i) for i in arr]
# bonus([18, 15, 12], 851)            # [230, 276, 345]
# bonus([30, 27, 8, 14, 7], 34067)    # [2772, 3080, 10395, 5940, 11880]

# -------------------------------------------------------------------------------------------------
# for 循环删除多个元素的方法
# --------------------
# dat = [1, 0, 2, 3, 0, 0, 0]
# temp = []
# for i in range(len(dat)):
#     if dat[i] == 0:
#         temp.append(i)
# for i in temp[::-1]:
#     dat.pop(i)
# print(dat)

# -------------------------------------------------------------------------------------------------
# 规范化括号()
# --------------------
# s = '))jf(d)()d)JF(O(9IJ)OJ)((()('
# s = list(s)
#
# temp = []
# lt = []
# for i in range(len(s)):
#     if s[i] == '(':
#         lt.append(i)
#     elif s[i] == ')':
#         if lt == []:
#             temp.append(i)
#         else:
#             lt.pop()
# for i in temp[::-1]:
#     s.pop(i)
#
# l_index = []
# r_index = []
# for i in range(len(s)):
#     if s[i] == '(':
#         l_index.append(i)
#     if s[i] == ')':
#         r_index.append(i)
# while len(l_index) > len(r_index):
#     s.pop(l_index.pop())
# s = ''.join(s)
# print('s:', s)

# --------------------------------------------------------------------------------------------------
# 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
# 子数组 是数组的一段连续部分。
# 提示：
#     1 <= nums.length <= 3 * 104
#     nums[i] 不是 0 就是 1
#     0 <= goal <= nums.length
# --------------------
# def numSubarraysWithSum(nums: list[int], goal: int) -> int:
#     n = len(nums)
#     ans = l1 = l2 = s1 = s2 = 0
#     for r in range(n):
#         s1 += nums[r]
#         s2 += nums[r]
#         while s1 > goal:
#             s1 -= nums[l1]
#             l1 += 1
#         while l2 <= r and s2 >= goal:
#             s2 -= nums[l2]
#             l2 += 1
#         ans += l2 - l1
#     return ans
#
#
# print(numSubarraysWithSum([0, 0, 0, 1, 0], 0))

# --------------------------------------------------------------------------------------------------
# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合。
# --------------------
# def isValid(s: str) -> bool:
#     d_kh = []
#     brackets = {')': '(', ']': '[', '}': '{'}
#     for i in s:
#         if i in brackets.values():
#             d_kh.append(i)
#         else:
#             if (not d_kh) or (brackets[i] != d_kh[-1]):
#                 return False
#             else:
#                 d_kh.pop()
#     return False if d_kh else True
#
#
# print(isValid("()"))
# print(isValid("()]{}"))
# print(isValid("(]"))
# print(isValid('([)]'))
# print(isValid(']'))
# print(isValid('('))

# --------------------------------------------------------------------------------------------------
# 套娃字典的两种方式

# from functools import reduce
#
# a = ['aa', 'bb', 'cc', 'dd']
# b = dict()
# reduce(lambda x, y: x.setdefault(y, dict()), a, b)
# print(b)
#
# d = dict()
# print(d.setdefault('aa',dict()))
# print(d['aa'].setdefault('bb',dict()))
# print(d['aa']['bb'].setdefault('cc',dict()))
# print(d['aa']['bb']['cc'].setdefault('dd',dict()))
# print(d)

# --------------------------------------------------------------------------------------------------
