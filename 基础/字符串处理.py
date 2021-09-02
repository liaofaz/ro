# -*-  codeing = utf-8 -*-
# @Time : 2021/4/28 上午 4:55
# @Author : 漫天烟华
# @File : 字符串处理.py
# @Software : PyCharm


# 中文字符从 '一' 开始，到 '龥'(yu) 结束
# 直接print会根据 unicode 解码，打印出对应的字符
# ord()函数   返回对应的 ASCII 数值，或者 Unicode 数值
# chr()函数   根据数值返回对应的解码后的 ASCII字符 或者 Unicode字符
# 一个汉字字符 在 utf8 编码下用3个字节表示，在 gbk 编码下用2个字节表示

# print('\u4e00')
# print('\u9fa5')
# print(ord('\u4e00'), chr(ord('\u4e00')))
# print(ord('\u9fa5'), chr(ord('\u9fa5')))
# print('\u4e00'.encode('utf8'))
# print('\u4e00'.encode('gbk'))
# -------------------------------------------------------------


# string1 = 'abc2def2ght2111'
# string2 = 'abc|def|ght2111'

# 字符串截取(截取下标n到m-1的字符)
# a = string1[4:7]
# print(a)
# 分隔、分列（以'2' '|' 等字符参数作为断点将字符串拆分成列表）
# b = string1.split('2')
# c = string2.split('|')
# print(b,c)
# 替换
# d = string1.replace('2','-')
# e = string2.replace('|',' ')
# print(d,e)

# 去除前后空格
# string = '   America   '
# f = string.strip()
# print(f)


# 占位符%s的用法
# print('Hello %s , welcome to %s !'%('Jone','china'))

# string = "good"
# print("|string = %s|" %string)          # 直接使用
# print("|string = %3s|" %string)         # 数字3的意思是：字符串的长度为3。当字符串的长度大于3时，按照字符串的长度打印出结果
# print("|string = %6s|" %string)         # 当字符串的长度小于6时，在字符串的左侧填补空格，使得字符串的长度为6
# print("|string = %-6s|" %string)        # 当字符串的长度小于6时，在字符串的右侧填补空格，使得字符串的长度为6
# print("|string = %.3s|" %string)        # 截取字符串的前3个字符，当截取字符串的字符长度大于字符串时，输出的结果是整个字符串
# print("|string = %6.3s|" %string)       # 先根据小数点后面的数字3截取字符串，当截取长度小于6时，需要在字符串的左侧填补空格，使得字符串的长度6
# print("|string = %*.*s|" %(6,2,string)) # 与上例效果一致，不过用*占位代替了数字，然后把数字写在外头
# print("只有%就不用转义","|%s%%|"%100)      # 如果使用占位符且需要打印%号时，用两个%%转义表示不用占位
