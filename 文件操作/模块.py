# -*-  codeing = utf-8 -*-
# @Time : 2021/6/7 5:58
# @Author : 漫天烟华
# @File : 模块.py
# @Software : PyCharm


# 模块只会在默认搜索路径的列表里寻找添加
# 通过sys模块，可对导入路径进行添加修改，从而改变导入模块的范围

import sys

# print(sys.path)             # 默认的搜索路径
# sys.path.append('D:\\')     # 添加所有路径
# print(sys.path)             # 添加后的搜索路径


# from package import *
# 从包中导入所有模块时，可导入的模块由__init__.py模块中的__all__属性决定*可导入的模块
# __all__ = [] 列表里填入允许导入的模块名字的字符串
# 如果不用*而是import具体模块名则不受此限

