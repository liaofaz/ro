# -*-  codeing = utf-8 -*-
# @Time : 2021/3/11 上午 7:31
# @Author : 漫天烟华
# @File : 文件读写与备份.py
# @Software : PyCharm


# quq = open("test.txt","w")
# quq.write("床前明月光，/n疑是地上霜。/n举头望明月，/n低头思故乡。")
# quq.close()       #关闭文件

# read（num） 方法，读取指定长度字符，每次打开开始时定位到文件开头，之后每次执行都在前一次的末尾处开始，关闭后重置
# 如没有括号内不指定参数，即read（）则表示读取文件中指针后的全部内容，返回一个字符串（\t、\n等转义字符算一个字符）

# quq = open("test.txt","r")
# content = quq.read(4)
# print(content)
# content = quq.read(3)
# print(content)
# quq.close()

# quq = open("test.txt", "r")
# content = quq.readline()            # 读一行的内容
# print(content)
# content = quq.readlines()           # 读出来的是一个列表，每行对应一个字符串元素
# print(content)
#
# i = 1
# for temp in content :
#     print("%d : %s"%(i,temp),end="")
#     i += 1
# quq.close()

# -----------------------------------------------------------------------------------------------
# 2021/5/20 4:17 重新学习

# 'r'访问模式: open（）的默认模式，可省略。只读不写，文件不存在会报错。

# f = open('new.txt','r')   # 用'r'模式打开一个不存在的文件会报错
# f.close()

# f = open('test.txt','r')
# f.write('abcdefg')        # 在'r'模式下写入也会报错，证明该模式只读
# f.close()

# ----------------------------------------------------------------

# 'w'访问模式: 只写不读，文件不存在会新建文件，文件已存在则覆盖原有内容写入新内容。如在文件关闭前在写入会追加而不是覆盖

# f = open('write.txt','w')
# f.readlines()           # 读取会报错
# f.close()

# f = open('write.txt','w')
# f.write('abc123')
# f.write('ABC456\n')
# f.close()

# ----------------------------------------------------------------

# a访问模式 : 追加写入模式，没有文件则新建，有则在文件数据末尾追加写入内容
# f = open('write.txt','a')
# f.write('BBC_News')
# f.close()

# ----------------------------------------------------------------
# r+、w+、a+（进行读取操作后，指针位置会变更为操作位置末尾，直到下一次打开重置）

# 打开时指针在开头，可以读取也可以写入
# f = open('rwa.txt','r+')
# # BBC = f.read()          # 刚打开时指针在开头，所以能打印全文，读取完成指针会在数据后（若前面进行过读写操作则无法读取）
# f.write('BBC_News\t')   # 执行写入时，如没有读取指针会在前面覆盖式写入（只覆盖新内容所占位置不会覆盖后面内容）
# # print(BBC)              # 若前面有执行过read相关指令，因为指针在末尾，相当于追加写入
# f.close()


# f = open('rwa.txt','w+')
# BBC = f.read()              # 因为全覆盖式打开，内容为空
# print(BBC)
# f.write('BBC_News\t')
# f.close()


# f = open('rwa.txt','a+')
# f.write('BBC_News\t')
# BBC = f.read()
# print(BBC)                  # 指针在末尾，无法读取显示前面的内容
# f.close()

# ----------------------------------------------------------------------------
# seek（）函数:  用来移动文件指针                                        改变指针位置
# 文件对象.seek（偏移量[，起始位置(默认值为0)]）
# 起始位置参数: 0(文件开头)   1(当前位置)   2(文件结尾)

# tell() 函数 返回当前指针距离开头的位置
# 用法: print(f.tell())
# ---------------------------
# 例子: 通过改变指针使得a模式、w模式可以读取内容

# f = open('rwa.txt','a+')
# f.write('CNN_News\t')       # 追加写入内容
# print(f.tell())
# f.seek(0, 0)
# print(f.tell())
# BBC = f.read()              # 调整指针，读取以前内容以及刚刚写入内容
# print(BBC)
# f.close()

# f = open('rwa.txt','w+')
# f.write('BBC_News\t')       # 覆盖式写入
# f.seek(0,0)
# BBC = f.read()              # 调整指针，读取刚刚写入内容
# print(BBC)
# f.close()

# ----------------------------------------------------------------

# 文件备份
# while True:
#     old_fname = input("请输入您要备份的文件名（带后缀）:")
#     print(f"旧文件名为: {old_fname}")
#     find_index = old_fname.rfind(".")
#     if find_index<=0 or len(old_fname[find_index:])==1:
#         print("您的输入有误，请重新输入！")
#         continue
#     temp_f = old_fname.split(".")
#     new_fname = "(备份).".join(temp_f)
#     print(f"新文件名为: {new_fname}")
#     try:
#         old_f = open(old_fname,"rb")
#     except FileNotFoundError as e:
#         print(e)
#         print("文件不存在！请重新输入！")
#         continue
#     new_f = open(new_fname,'wb')
#     while True:
#         data = old_f.read(2048)         # 每次最多读取2048字符每次读写，防止文件过大
#         if len(data) == 0:
#             break
#         new_f.write(data)
#     print("文件备份成功！")
#     old_f.close()
#     new_f.close()
#     break

