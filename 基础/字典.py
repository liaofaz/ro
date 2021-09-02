# -*-  codeing = utf-8 -*-
# @Time : 2021/3/9 下午 1:44
# @Author : 漫天烟华
# @File : 字典.py
# @Software : PyCharm


# 字典使用键访问值

# # ↓通过键，直接访问
# dict_1 = {"姓名":"张三","年龄":27,"性别":"男","籍贯":"北京"}
# print(dict_1["年龄"])           #通过键直接访问，如果键不存在（未定义）会报错
# # 结果：27
#
# # ↓dict.get（key,default）方法访问，get方法不改变字典本身
# print(dict_1.get("职业"))       #通过get方法，若没有设置预设值，没找到对应键会返回默认预设值None
# # 结果：None
# print(dict_1.get("职业","无"))  #如设定了预设值Default，找不到键值对时返回预设值，找到时返回对应值
# # 结果：无
# # ↓通过dict.setdefault（key,default）方法访问，setdefault方法可能改变字典
# print(dict_1.setdefault('年龄',18))        # 若键存在，则返回对应值，而非预设值
# print(dict_1.setdefault('职业','教师'))     # 若键不存在，则把查询的键与预设值添加到字典末尾
# print(dict_1)


# 字典元素的【增加】

'''
dict_1 = {"键":"值","姓名":"张三","年龄":27,"性别":"男","籍贯":"北京"}
dict_1["学历"] = "博士"
print(dict_1["学历"])
# 博士
'''

# 字典元素的【删除】的两种方法（del ， clean ）

# del 删除
# dict_1 = {"键":"值","姓名":"张三","年龄":27,"性别":"男","籍贯":"北京"}
# del dict_1["键"]
# print(dict_1)

# pop 删除,弹出键所对应的键值对，并返回对应值，若没有该键会报错
# print(dict_1.pop("性别"))
# print(dict_1)

# clean 清空
# dict_1.clear()       #清空字典内容，得到一个空的字典
# print(dict_1)


# 字典元素的【修改】
'''
dict_1 = {"键":"值","姓名":"张三","年龄":27,"性别":"男","籍贯":"北京"}
dict_1["姓名"] = "李四"             #通过重新对键赋值来修改值
print(dict_1["姓名"])
# 李四
'''
# ---------------------------------------------------------------------------------------
# dict.fromkeys() 传入一个序列和一个值，返回一个键为序列元素且值相同的字典
# dict.update()   更新，传入一个字典或者有字典特征的序列，相同键名则替换值，没有则添加键值对

# salary = dict.fromkeys(['张三', '李四', '王五', '赵六'], 5000)
# print(salary)
# salary['王五'] -= 1000
# salary['赵六'] -= 1000
# salary.update({'张三': 6000, '李四': 6000})
# print(salary)

# ---------------------------------------------------------------------------------------
# 字典元素的查找（遍历）
'''
dict_1 = {"键":"值","姓名":"张三","年龄":27,"性别":"男","籍贯":"北京"}

print(dict_1.keys())                    # 提取所有键，结果以迭代器形式呈现
#dict_keys(['键', '姓名', '年龄', '性别', '籍贯'])
print(dict_1.values())                  # 提取所有值
#dict_values(['值', '张三', 27, '男', '北京'])
print(dict_1.items())                   # 提取所有项【列表】，元素为由键值对组成的元组
#dict_items([('键', '值'), ('姓名', '张三'), ('年龄', 27), ('性别', '男'), ('籍贯', '北京')])


for key in dict_1.keys():                       # 遍历所有的键
    print(key)
    
for value in dict_1.values():                   # 遍历所有的值
    print(value)
    
for key,value in dict_1.items():
    print("key = %s,value = %s"%(key,value))    # 遍历所有键值对
'''

# enumerate 枚举函数提取列表的下标及元素内容
# list = ["a","b","c","d","e"]
# for a,b in enumerate(list) :
#     print(a,b)

# dict_1 = {"键":"值","姓名":"张三","年龄":27,"性别":"男","籍贯":"北京"}
# for key,value in dict_1.items():
#     #print("key = %s,value = %s"%(key,value))
#     print(key, value)
