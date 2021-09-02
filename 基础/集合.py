# 集合（set）是一个无序的不重复元素序列。

# 特性：
# 无序,不能通过下标进行访问
# 去重,没有重复元素
# 元素只能是整型、字符串、元组，不可为列表、字典


# ↓新建集合、空集合
# set1 = {1,2,3,4,5}
# set2 = {1,1,2,2,3,3}
# set3 = set()
# print(set1)
# print(set2)
# print(set3)



# 集合元素的【新增】（add、update）
# set = {1,2,3,4,5,6}
# set.add(7)              # add方法添加单个元素,如果元素已存在，则不进行任何操作。
# print(set)
# set.update([9,7,8])     # update方法把元素集（列表、元组、集合、字典的键）的元素逐个添加到集合
# print(set)
# set.update({'姓名':'张三','年龄':'17'})
# print(set)



# 集合元素的【删除】（remove、discard、pop）
# set = {1,2,3,4,5,6}
# s = {'张三','李四','lisa','王健林'}
# set.remove(3)           # 将指定元素从集合中删除，如果集合中无该元素则会报错
# print(set)
# set.discard(9)          # 将指定元素从集合中删除，集合中无该元素也不会报错
# print(set)
# s.pop()
# set.pop()               # 从集合中随机删除一个元素
# print(set,s)
# # 清空集合
# set.clear()
# print(set)