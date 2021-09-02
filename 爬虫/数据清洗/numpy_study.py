# -*- codeing = utf-8 -*-
# @Time:    2021/8/12 上午 3:36
# @Author:  漫天烟华
# @Software: PyCharm
# @Version:  Python 3.9.4


# numpy 是一个开源的Python科学计算库，用于快速处理任意维度的数组
# 对于同样的数值计算任务，Numpy比直接使用Python要简洁得多
# numpy 使用ndarray对象来处理多维数组，该对象是一个快速而灵活的大数据容器

# ndarray(numpy存储对象)的优势
#   内存块风格   数据与数据的地址都是连续的，批量操作元素更快；但因为只能存储相同类型数据，通用性能不如原生list
#   支持并行化运算(向量化计算)
#   效率远高于纯Python代码  底层C语言编写，内部解除了GIL全局解释锁

import numpy as np
import matplotlib.pyplot as plt
import time
import random

# -----------------------------------------------------------------------
# 创建 ndarray

# alist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# blist = np.array(alist)
# print(type(alist))
# print(type(blist))
# print(blist)

# ------------------------------------------------
# ndarray 与 Python 原生list运算效率对比

# a = [random.random() for i in range(10000000)]
# s1_time = time.time()
# sum1 = sum(a)
# print(time.time() - s1_time)
# print(sum1)
#
# b = np.array(a)
# s2_time = time.time()
# sum2 = np.sum(b)
# print(time.time() - s2_time)
# print(sum2)

# ------------------------------------------------
# ndarray 的属性

# ndarray = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# # 1. 数组的形状,返回反映维度的元组(行列数)
# print(ndarray.shape)
# # 2. 数组维数
# print(ndarray.ndim)
# # 3. 数组中的元素数量
# print(ndarray.size)
# # 4. 一个数组元素的长度(字节),一个字节由8位二进制数字组成
# print(ndarray.itemsize)
# # 5. 数组元素的类型
# print(ndarray.dtype)

# ------------------------------------------------
# ndarray 的形状 (相同维度相邻,且同维度元素数量相同才能显示的样子)

# 一维数组
# ndarray1 = np.array([1, 2, 3])
# print(ndarray1)

# 二维数组
# ndarray2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(ndarray2)

# 三维数组
# ndarray3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [9, 9, 9]]])
# print(ndarray3)
# print(ndarray3.ndim)
# print(ndarray3.shape)

# 四维数组
# ndarray4 = np.array([[[[1], [2]], [[3], [4]]], [[[5], [6]], [[7], [8]]]])
# print(ndarray4)
# print(ndarray4.ndim)
# print(ndarray4.shape)

# ------------------------------------------------
# ndarray 的类型
# bool_	布尔型数据类型（True 或者 False）
# int_	默认的整数类型（类似于 C 语言中的 long，int32 或 int64）
# float_	float64 类型的简写
# complex_	complex128 类型的简写，即 128 位复数
# 更多不同位数的类型略...


# sarray = np.array(['a', 'b', 'c', 'd'])
# print(sarray)
# print(sarray.dtype)
# print(sarray.itemsize)
#
# iarray = np.array([1, 2, 3, 4], dtype=np.float_)
# print(iarray)
# print(iarray.dtype)
# print(iarray.itemsize)
# -----------------------------------------------------------------------


# 基本操作与应用
# -----------------------------------------------------------------------
# 生成 0 和 1 的数组
# np.ones, np.zeros 接收形状参数 shape(元组或列表)
# np.xx(shape[, dtype, order])
# np.ones_like, np.ones_like 接收数组参数 ndarray 或者一个有数组结构的列表
# np.xx_like(a[, dtype, order, subok])

ones = np.ones((4, 8))
# print(ones)
#
# zeros = np.zeros_like(ones)
# print(zeros)
# zeros = np.zeros_like([[1, 2], [3, 4]])
# print(zeros)

# ------------------------------------------------
# 从现有的数组生成
# 深拷贝 np.array(object[, dtype, copy, order, subok, ndmin])
#  引用  np.asarray(a[, dtype, order])

# a = np.array([[1, 2], [3, 4]])
# a1 = np.array(a)
# a2 = np.asarray(a)
#
# a[0][0] = 5
# print(a, id(a), id(a[0]))
# print(a1, id(a1), id(a1[0]))
# print(a2, id(a2), id(a2[0]))
# # print(a[0], id(a[0]))
# # print(a1[0], id(a1[0]))
# # print(a2[0], id(a2[0]))

# ------------------------------------------------
# 生成固定范围数组(从某段范围生成多少个元素的等差数组)
# np.linspace(start, stop, num=50[, endpoint=True, retstep=False, dtype=None])
# start 序列的初始值
# stop  序列的终止值
# num   要生成的等间隔样例数量，默认为50
# endpoint  序列中是否包含stop的值，默认为True
# retstep	如果为 True 时，生成的数组中会显示间距，默认不显示
# dtype	    ndarray 的数据类型

# linspace = np.linspace(0, 100, 11)
# print(linspace)

# ------------------------------------------------
# np.arange(start, stop, step, dtype)
# 根据 start 与 stop(不包含) 指定的范围以及 step 设定的步长，生成一个 ndarray
# 每隔多少生成数组，与range类似

# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# start	    序列的起始值为：base ** start
# stop	    序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
# endpoint	该值为 true 时，数列中中包含stop值，反之不包含，默认是True
# base	    对数 log 的底数
# dtype	    ndarray 的数据类型
# 生成10的n次幂的数据，次幂数等差

# print(np.arange(0, 11, 1))
# print(np.logspace(0, 2, 3))

# ---------------------------------------------------
# 生成随机数组
# ------------------------------------------------
# 均匀分布
# ----------------
# np.random.rand()
# 返回[0.0, 1.0)内的一组均匀分布的数

# print(np.random.rand())
# ----------------
# 浮点数
# np.random.uniform(low=0.0, high=1.0, size=None)
# 功能:  从一个均匀分布[low, high)中随机采样,左闭右开
# low:  采样上界，float类型，默认值是0.0
# high: 采样下界，float类型，默认值是1.0
# size: 输出样本数目，为int或元组(tuple)类型，如size=(x, y, z)，则生成shape为(x, y, z)的x*y*z个样本，
#       缺省时输出1个值

# print(np.random.uniform(1, 5, (2, 2, 3)))
# ----------------
# 整数
# np.random.randint(low, high=None, size=None, dtype=int)
# high为None时取值[0, low)，否则取值[low, high)，size参数同上

# print(np.random.randint(1, 10, size=(10, 10)))
# ----------------
# 上述方法分布情况为均匀分布
# 随机生成1亿个浮点数数组，并且分为1000个区间，查看频数分布情况
# 从直方图可以看出各区间频数在10万附近，呈均匀分布

# plt.figure()
# data = np.random.uniform(0, 1, 100000000)
#
# plt.hist(data, bins=1000)
# plt.grid(alpha=0.5)
# plt.show()
# ------------------------------------------------
# 正态分布
# ----------------
# 函数返回一个或一组样本，服从标准正态分布
# 标准正态分布又称为u分布，是以0为均值、以1为标准差的正态分布.相当于normal(0,1,size)
# print(np.random.randn(3, 3))
# ----------------
# normal(loc=0.0, scale=1.0, size=None)
# loc  :float 正态分布的均值，直方图的中心
# scale:float 正态分布的标准差，该值越大越矮胖，越小越瘦高
# size int/tuple

# x = np.random.normal(1.75, 0.5, 10000000)
# plt.figure()
# plt.hist(x, bins=1000)
# plt.grid(alpha=0.5)
# plt.show()

# ------------------------------------------------
# 数组索引、切片
# 可以同时切片出不同维度的元素
# 先对行进行索引，再对列进行索引

# a = np.random.normal(0, 1, (3, 4))
# print(a)
# print('-'*50)
# print(a[:, 0:2])


# 索引活用，筛选元素
a = np.array([[0, 1, 2, 3, 4, 5],
              [1, 2, 3, 4, 5, 6],
              [2, 3, 4, 5, 6, 7]])
b = np.array([[0, 1],
              [1, 2],
              [2, 3]])

# print(a > 4)
# print((a < 3) | (a > 4))    # 筛选返回一个True、False数组，多个条件用括号括起来|隔开
# print(a[a > 4])     # 根据True、False数组筛选元素，返回一个一维数组
# print(a[:, 2])
# print(a[a[:, 2] > 2])   # 根据下标为2的列筛选出符合的行
# a[a[:, 2] > 2] = 666    # 根据筛选结果修改数组元素的值
# print(a)

# ------------------------------------------------
# 形状修改
# reshape 和 resize的 新shape的乘积size必须与原来相同，否则会报错
# 1. ndarray.reshape(shape, order='C')
#   不进行行列互换，将数据按shape重新分组，返回新的数组
#   shape可以有一个未知维度值-1，函数会根据原数组size除得，但是-1以外的维度乘积必须是size的因数
#       简单来说就是可以只明确行数或者列数，另一个-1代替，函数会自动补全
# 2. ndarray.resize(new_shape, refcheck=True)
#   不进行行列互换，对对象原值进行修改，数据效果同上，无返回值
# 3. ndarray.T
#   行列互换，返回互换后的数组，原数组行数据与新数组列相同，列数据与新数组行数据相同

# ndarray = np.random.uniform(0, 1, (3, 6))
# print(ndarray)
# print(ndarray.reshape(9, 2))
# print(ndarray.reshape(-1, 3, 3))
# print(ndarray.reshape(9, -1))
# print(ndarray.reshape(-1, 9))
# print(ndarray.T)
# ndarray.resize((9, 2))
# print(ndarray)

# ------------------------------------------------
# 类型修改
# ndarray.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
#   返回 dtype 类型的元素的新数组
# ndarray.tobytes(order='C')
#   返回一个数组的bytes类型数据(一个二进制数据串)
#   与ndarray.tostring()相同，tostring逐渐被弃用

# ndarray = np.random.uniform(0, 10, (3, 3))
# print(ndarray)
# print(ndarray.astype(np.int64))
# print(ndarray.astype(np.string_))

# # print(ndarray.tostring())
# print(ndarray.tobytes())

# ------------------------------------------------
# 数组的去重
# np.unique(ndarray)
#   返回一个去重后的一维数组

# temp = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(np.unique(temp))

# ------------------------------------------------
# ndarray 运算
# 1. 逻辑运算
#   大于(>)、小于(<)、等于(==)直接进行判断
#   满足条件的直接赋值

# stock_change = np.random.normal(0, 1, (5, 5))
#
# # 逻辑判断的返回值，一个元素为布尔值的数组
# print(stock_change > 0.5)
# print(stock_change)
# # 通过条件切片
# print(stock_change[stock_change > 0.5])
# # 通过筛选条件切片修改数组的值
# stock_change[stock_change > 0.5] = 1
# print(stock_change)

# ------------------------------------------------
# 通用判断函数
# np.all()
#   数组里所有元素都满足条件就返回True，只有有一个不符合就返回False
# np.any()
#   有一个及以上符合条件返回True，全都不符合返回False

# t_f = np.random.normal(0, 1, (5, 3))
# print(t_f)
# print(np.all(t_f > 0))
# print(np.all(t_f))  # 非零即True
# print(np.any(t_f > 0))
# print(np.any(t_f))

# ------------------------------------------------
# 三元运算符 np.where()
#   参数1为条件，符合条件的元素值为参数2，不符合则值为参数3
#   不改变原数组，返回一个修改后的新数组
# 多个条件
#   np.logical_or
#   np.logical_and
#   np.logical_not

# temp = np.random.normal(0, 1, (5, 3))
#
# print(temp)
# print(np.where(temp > 0.5, 1, 0))
# print(np.where(np.logical_not(temp > 0),-1,0))
# # print(np.logical_or(temp > 0.5, temp < -0.5))
# # print(np.logical_and(temp > -0.5, temp < 0.5))

# ------------------------------------------------
# 统计指标
# axis参数为0或者1，表示按列或者按行匹配，不设则从全部元素匹配
# np.max()      最大值
# np.min()      最小值
# np.median()   中位数 按顺序排列的一组数据中居于中间位置的数.如有偶数个，通常取最中间的两个数值的平均数作为中位数
# np.mean()     算数平均值
# np.std()      标准差
# np.var()      方差
# 最大值，最小值的位置(下标)
#   np.argmax(axis=None, out=None)
#   np.argmin(axis=None, out=None)

# temp = np.random.normal(0, 1, (10, 5))
# print(temp)
# # 最大值
# print(np.max(temp))
# print(temp.argmax())
# print(temp.max(0))
# print(temp.argmax(0))
# # 最小值
# print(np.min(temp))
#
# print(np.median(temp))
# print(np.mean(temp))
# print(np.std(temp))
# print(np.var(temp))


# --------------------------------------------------------------------------------------
# 数学: 矩阵(Matrix)
# 矩阵和array的外观形状区别是，矩阵必须是2维的，但是array可以是多维的

# 向量
# 一种特殊矩阵，只有一列的矩阵即列向量
# -----------------------------
# 矩阵运算
# 矩阵与矩阵加法与数组同，矩阵不可与数字相加
# 矩阵与数字相乘，每个元素都相乘，得出新矩阵

# 矩阵向量乘法
# 矩阵列数需与向量行数相同
# 矩阵的每行的元素与向量的列对应相乘的总和，为新的矩阵每行的新元素(只有一列)

# 两矩阵相乘(A列数与B行数相等才有意义)
# 新矩阵取A矩阵的行数为行数，B矩阵的列数为列数，以此组成新的形状的矩阵
# 新矩阵元素为A对应的行数与B对应列数的对位的两个数积的总和
# 矩阵间的乘法不满足交换律:AxB ≠ BxA
# 矩阵间的乘法满足结合律:  Ax(BxC) = (AxB)XC

# 单位矩阵: 左上角到右下角的对角线上的元素均为1，其他元素为0的方阵(行列数相同)，一般用I或E表示

# 两个方阵相乘等于单位矩阵，那么两者互为逆矩阵

# 矩阵的转置
# 类似数组的行列互换(ndarray.T),原矩阵下标(行,列)的元素=转置矩阵下标(列,行)的元素
# [[1,2]    [[1,4,7]
#  [4,5]     [2,5,8]]
#  [7,8]]

# -----------------------------
# Python矩阵运算
# np.matmul()   矩阵乘法
# np.dot()      点乘
# 区别: 矩阵间乘法没区别，dot可以与数字相乘，matmul则会报错

# a = np.array([[80, 86],
# #               [82, 80],
# #               [85, 78],
# #               [90, 90],
# #               [86, 82],
# #               [82, 90],
# #               [78, 80],
# #               [92, 94]])
# # b = np.array([0.7, 0.3])
# #
# # print(np.matmul(a, b))
# # print(np.dot(a, b))

# ---------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------
# 数组间运算

# 普通数组算法运算
# 数组与数组运算(非向量)。两数组shape右对齐时，逐个数值比对，满足以下条件方可运算:
#   对应值相等
#   其中一个对应值为1
# 数组与数字的运算
#   数组所有元素都与数字运算一遍，然后返回结果数组

# matrix1 = np.random.randint(1, 10, (3, 3))
# matrix2 = np.random.randint(1, 10, (3, 3))
# print(matrix1)
# print(matrix2)
# print(matrix1 + matrix2)
# print(matrix1 + 2)
# print(matrix1 * matrix2)
# print(matrix1 * 2)

# -----------------------------
# 向量数组运算
# 注意:
#   列向量数组运算时需列数相同
#   行向量数组运算时需行数相同
#   分别为列列对应运算和行行对应运算

# temp = np.random.randint(1, 10, (2, 3))
# print(temp)
# # 列向量运算
# print(temp * [1, 2, 3])
# # 行向量运算
# a = np.array([1, 2]).reshape(2, 1)
# print(a)
# print(temp * a)
