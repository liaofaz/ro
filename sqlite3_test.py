# -*-  codeing = utf-8 -*-
# @Time : 2021/3/31 下午 1:06
# @Author : 漫天烟华
# @File : sqlite3_test.py
# @Software : PyCharm

import sqlite3

# 1.连接数据库
conn = sqlite3.connect("../test/new数据库.db")
print("database连接成功！")


# 2.创建数据表
# cur = conn.cursor()     # 获取游标
#
# sql = """
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char (50),
#         salary real);
# """
#
# cur.execute(sql)        # 执行sql语句
# conn.commit()           # 提交数据库操作
# conn.close()            # 关闭数据库
# print("数据表新建成功！")


# 3.增加/插入数据
# conn = sqlite3.connect("这是一个新的数据库.db")
# print("database连接成功！")
# cur = conn.cursor()  # 获取光标
#
# sql = '''
#     insert into company (id,name,age,address,salary)
#     values (1,'李明',25,'北京',9000);
# '''
#
# cur.execute(sql)    # 执行sql语句
# conn.commit()       # 提交数据库操作
# conn.close()        # 关闭数据库
# print("插入数据成功！")


# 4.查询数据
# conn = sqlite3.connect("这是一个新的数据库.db")
# print("database连接成功！")
# cur = conn.cursor()  # 获取光标
#
# sql = '''
#     select id,name,age,address,salary from company
# '''
#
# values = cur.execute(sql)    # 执行sql语句
# for i in values:
#     print(i)
#
# conn.close()        # 关闭数据库
# print("查询数据成功！")