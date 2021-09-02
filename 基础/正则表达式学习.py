# -*-  codeing = utf-8 -*-
# @Time : 2021/3/27 下午 1:33
# @Author : 漫天烟华
# @File : 正则表达式学习.py
# @Software : PyCharm


# 正则表达式：字符串模式（判断字符串是否符合一定的标准）


# 修饰符	    描述
# re.I	    使匹配对大小写不敏感
# re.L	    做本地化识别（locale-aware）匹配
# re.M	    多行匹配，影响 ^ 和 $
# re.S	    使 . 匹配包括换行在内的所有字符
# re.U	    根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。


import re

# 输出为必须有一个数字的，包括大小写字母和数字的长度超过8的密码
# password = input("请输入密码:")
# key = r"(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[A-Za-z0-9]{8,}"
# print(re.findall(key,password))

