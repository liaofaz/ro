# -*-  codeing = utf-8 -*-
# @Time : 2021/3/11 上午 8:34
# @Author : 漫天烟华
# @File : 异常处理.py
# @Software : PyCharm


# 例子：写入古诗，复制古诗。

# def xie_gushi(name,content):
#     try:
#         gushi = open(name,"w")
#         shiju = gushi.write(content)
#
#     except Exception as result:
#         print("发生异常:%s" % result)
#     finally:
#         gushi.close()
#
# def copy_gushi(name1,name2):
#     try:
#         gushi = open(name1, "r")
#         content = gushi.readlines()
#         gushi.close()
#         copy = open(name2, "w")
#         for i in content:
#             copy.write(i)
#         print("复制完毕")
#     except Exception as result:
#         print("发生异常:%s"%result)
#     finally:
#         copy.close()
#
# xie_gushi("gushi.txt",'''九州生气恃风雷，
# 万马齐喑究可哀。
# 我劝天公重抖擞，
# 不拘一格降人才。''')
# copy_gushi("gushi.txt","copy.txt")


#---------------------------------------------------------------

# 忽略报错的方法

# try:
    #代码段
# except （错误类型名称）：
    #发生错误的操作
# finally：
    #无论有没有错误都必须执行的操作

'''
常用错误类型：

IOError ：输入、输出异常
Exception ：可以捕获除与程序退出sys.exit()相关之外的所有异常
            except Exception as result:
                print(result)
            #通过返回参数，打印发生的错误

'''



'''
#引入traceback模块，打印详细异常信息

import traceback
try:
    1 + 'a'
except Exception:
    print(traceback.format_exc())

'''


# 自定义异常
# class MyError(Exception):
#     def __str__(self):
#         return '错了错了~'
#
#
# try:
#     raise MyError
# except Exception as result:
#     print(f'MyError: {result}')
