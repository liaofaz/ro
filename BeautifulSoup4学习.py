# -*-  codeing = utf-8 -*-
# @Time : 2021/3/19 上午 2:52
# @Author : 漫天烟华
# @File : BeautifulSoup4练习.py
# @Software : PyCharm


'''
BeautifulSoup4 : 将复杂的html文档转换成复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种 ：
1 - Tag              （标签）
2 - NavigableSting   （导航）
3 - BeautifulSoup    （整齐集合）
4 - Comment          （评论）
'''


from bs4 import BeautifulSoup
import re
file = open("../test/baidu.html", "rb")
html = file.read().decode("utf-8")
file.close()
bs = BeautifulSoup(html,"html.parser")

#--------------------------------------------------------------------
# 1 tag 打印标签及其内容,拿到它所找到的第一个内容
# print(bs.title)
# print(bs.a)


# 2 NavigableSting 只打印标签里的内容（字符串）
# print(bs.a.string)

# 打印标签里的属性
# print(bs.a.attrs)     #以字典的方式保存


# 3 BeautifulSoup 表示整个文档
# print(bs.name)
# print(bs)


# 4 Comment  是一个特殊的NavigableSting，输出的内容不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))
#------------------------------------------------------------------



# 文档的遍历，遍历文档树(利用位置来搜索信息)
'''
# 例：contents 获取Tag的所有子节点，返回一个list
# print(bs.head.contents)
# print(bs.head.contents[3])

# 例： children 获取所有Tag的子节点，返回一个生成器（或者叫迭代器，直接打印不显示内容，遍历时内容与contents一致）
# print(bs.head.children)   
# for child in bs.head.children:
#     print(child)

# 更多方法，自行了解
'''





# 文档的搜索

# 方法（1） ： find_all()                             通过【标签】搜索的三种用法

# （1）字符串过滤，会查找与字符串完全匹配的标签内容
# t_list = bs.find_all("a")
# print(t_list)

# （2）使用正则表达式搜索   用search（）方法来匹配内容
# import re
# t_list = bs.find_all(re.compile("a"))
# for i in t_list:             # 搜索所有标签名称含有"a"的标签内容
#     print(i)

# （3）定义并传入一个函数，根据函数的要求来搜索
# 例 ：搜索包含name属性的标签内容
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
# for i in t_list:
#     print(i)



# 方法（2）kwargs 参数                                      通过【属性】搜索

# t_list = bs.find_all(id = "u1")
# for i in t_list:
#     print(i)        #搜索指定id标签内容

# t_list = bs.find_all(class_= True)
# for i in t_list:
#     print(i)        #搜索含有class属性的标签内容

# 搜索指定属性的内容，有时候需要加下划线，有时候搜不到
# t_list = bs.find_all(class_="mnav")
# for i in t_list:
#     print(i)
# print("-"*80)
# t_list = bs.find_all(href="http://map.baidu.com")
# for i in t_list:
#     print(i)



# 方法（3） text参数，把完全对应的参数找出来                         通过【内容】搜索
# t_list = bs.find_all(text=["hao123","地图","贴吧","新"])
# for i in t_list:
#     print(i)        # "新"没有完全匹配的，所以没有打印出来

# 用正则表达式来查找包含特定文本的内容（标签里的字符串）
# t_list = bs.find_all(text = re.compile("吧"))
# print(t_list)
# t_list = bs.find_all(text = re.compile("\d"))
# print(t_list)       # 字符串中含有数字的内容



# 方法（4） limit 参数,只打印指定个数个标签及内容                 通过【标签】搜索指定【数量】条内容
# t_list = bs.find_all("a",limit=4)
# for i in t_list:
#     print(i)










# CSS选择器

#通过【标签】来查找
# t_list = bs.select("meta")
# for i in t_list:
#     print(i)

#通过【类名class】来查找
# t_list = bs.select(".mnav")
# for i in t_list:
#     print(i)

#通过【id】来查找
# t_list = bs.select("#u1")
# for i in t_list:
#     print(i)

#通过【属性】来查找
# t_list = bs.select("a[name='tj_trmap']")
# for i in t_list:
#     print(i)

#通过【子标签】来查找
# t_list = bs.select("head > title ")
# for i in t_list:
#     print(i)

#……………更多内容自行了解……………