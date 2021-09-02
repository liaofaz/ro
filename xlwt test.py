# -*-  codeing = utf-8 -*-
# @Time : 2021/3/29 下午 6:36
# @Author : 漫天烟华
# @File : xwlt doubanxls.py
# @Software : PyCharm


import xlwt
workbook = xlwt.Workbook(encoding="utf-8")      #创建文件
worksheet = workbook.add_sheet("九九乘法表")              #创建工作表

for b in range(0,9):
    for a in range(0,b+1):
        worksheet.write(b,a,"%d * %d = %d "%(a+1,b+1,(a+1)*(b+1)))
        print("%d * %d = %d "%(a+1,b+1,(a+1)*(b+1)),end="\t")
    print()
workbook.save("九九乘法表.xls")