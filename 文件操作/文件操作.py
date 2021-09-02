# -*-  codeing = utf-8 -*-
# @Time : 2021/5/20 19:53
# @Author : 漫天烟华
# @File : 文件操作.py
# @Software : PyCharm


import os           # 导入os模块

# os模块的文件操作（重命名、删除）
# f = open('os.txt','w')
# f.close()
# os.rename('os.txt','os_new.txt')    # 文件重命名
# os.remove('os.txt')                 # 删除文件

# os模块的文件夹操作(新建、重命名、删除)
# os.mkdir('new文件夹')                    # 新建文件夹
# os.rename('new文件夹','re_new文件夹')     # 修改文件夹名字
# os.rmdir('renew文件夹')                  # 删除文件夹

# 获取返回当前py文件的路径
# print(os.getcwd())

# 改变默认目录chdir（）
# 在当前目录aa文件夹内创建bb文件夹，然后在bb内创建cc文件夹
# os.mkdir('aa')
# os.chdir('aa')                  # 在当前路径下切换默认文件夹
# os.mkdir('bb')
# os.chdir(os.getcwd()+'\\bb')    # 绝对路径下切换默认文件夹
# os.mkdir('cc')
# print(os.getcwd())

# 获取目录列表os.listdir('目录名,可省略')
# print(os.listdir)           # 以列表形式返回当前py文件的目录列表（也就是所有文件夹名以及文件名）
# print(os.listdir('aa'))     # 以列表形式返回指定文件夹下的目录列表


# 批量重命名
while True:
    n = int(input('请输入1（增加字符串）或0（删除字符串）:'))
    # 批量增加字符串（Python_原名）
    if n == 1:
        filenames = os.listdir()
        print(filenames)
        for i in filenames:
            newname = 'Python_' + i     # 重构文件名
            os.rename(i,newname)        # 重命名文件
        break
    # 批量删除字符串（删除文件名前面的'Python_'）
    elif n == 0:
        filenames = os.listdir()
        print(filenames)
        for i in filenames:
            newname = i[7:]     # 重构文件名
            os.rename(i,newname)        # 重命名文件
        break
    else:
        print('您的输入有误，请重新输入！')