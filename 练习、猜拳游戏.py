# -*-  codeing = utf-8 -*-
# @Time : 2021/3/3 上午 4:53
# @Author : 漫天烟华
# @File : 练习.py
# @Software : PyCharm

'''
age = 1
while age < 20 :
    print("我的年龄是：%d" % age)
    age += 1

print("任务结束")
print("www","baidu","com",sep= ".")
'''





'''

    password = int(input("请输入五位数的密码："))

    if password == 12593:
        print("密码正确")                                          #未完成，回来看！！
        break
    else:
        print("请重新输入！")

'''




"""                   #【猜拳游戏】
try:
    import random

    number = int(input("请输入你要出的东西对应的数字，剪刀（0)、石头（1）、布（2）："))
    number2 = random.randint(0, 2)
    print("随机生成的数字是：", number2)
    if number >= 0 and number <= 2:
        if number == number2:
            print("哼，这把平局！")
        elif (number - number2 == 1) or (number - number2 == -2):
            print("切，侥幸让你赢了！")
        elif (number - number2 == -1) or (number - number2 == 2):        #此处可以直接用else以省略条件
            print("哈哈，你输了！")

    else:
        print("你输的数字不对！不跟你玩了！")

except:
    print("你犯规，游戏结束！")

"""

while True :
    try:
        import random
        print("我们来玩石头剪刀布的游戏，剪刀（0)、石头（1）、布（2）。如果不想玩了，就输入8 结束游戏")
        number = int(input("请输入0~2的整数："))
        number2 = random.randint(0, 2)
        print("随机生成的数字是：", number2)
        if number >= 0 and number <= 2 or number == 8 :
            if number == number2:
                print("哼，这把平局！")
            elif (number - number2 == 1) or (number - number2 == -2):
                print("切，侥幸让你赢了！")
            elif number == 8 :
                print("下次再玩~~")
                break
            elif (number - number2 == -1) or (number - number2 == 2):  # 此处可以直接用else以省略条件
                print("哈哈，你输了！")

        else:
            print("你没按规矩来！这把不算！")

    except:
        print("你犯规，重来！")
    print("-"*50)
