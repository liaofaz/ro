# -*- codeing = utf-8 -*-
# @Time:    2021/8/9 下午 8:32
# @Author:  漫天烟华
# @Software: PyCharm
# @Version:  Python 3.9.4


# pandas 是基于NumPy 的一种工具，该工具是为解决数据分析任务而创建的Python数据分析模块

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
#   data    一组数据(ndarray、series, map, lists, dict 等类型)
#   index   行索引，默认(0~行数m-1)
#   columns 列索引，默认(0~列数n-1)
#   dtype   数据类型
#   copy    拷贝数据，默认为 False


stock = np.random.normal(0, 1, (10, 5))

stock_code = [f'股票{i + 1}' for i in range(stock.shape[0])]
stock_date = pd.date_range('2021-8-1', periods=stock.shape[1], freq='B')
df = pd.DataFrame(stock, index=stock_code, columns=stock_date)
# print(df)
# ----------------------------
# 生成一个固定频率的DatetimeIndex时间索引
# pd.date_range(start=None, end=None, periods=None, freq='D', tz=None, normalize=False, name=None, closed=None, **kwargs)
# 该函数主要用于生成一个固定频率的时间索引，在调用构造方法时，必须指定start、end、periods中的两个参数值
#   periods：固定时期，取值为整数或None
#   freq：日期偏移量，取值为string或DateOffset，默认为'D'，可改为'B'跳过周末
#   normalize：若参数为True表示将start、end参数值正则化到午夜时间戳(点数归零)
#   name：生成时间索引对象的名称，取值为string或None
#   closed：选择是否包含开始和结束时间，left包含开始时间，不包含结束时间，right与之相反，默认包含开始和结束时间

# date = pd.date_range('2018.8.1',periods=5)
# print(date)

# -----------------------------------------------------------------------------------
# DataFrame 的属性方法

#   shape   形状
#   index   行索引列表
#   columns 列索引列表
#   values  值(数组)
#     T     转置(行列互换)

#   head(n) 显示前n行，默认5行
#   tail(n) 显示前n行，默认5行

# --------------------------------------------
# DataFrame 索引设置


# 获取行索引值、列索引值、数据值
# print(df.index)
# print(df.columns)
# print(df.values)

# 修改行列索引值，必须整体修改

# df.index = [i for i in range(0, stock.shape[0] * 10, 10)]
# df.columns = [i for i in range(0, stock.shape[1] * 10, 10)]
# print(df)
# ------------------------
# 重设行索引
# df.reset_index(drop=False)
#   drop 默认为False，重置行索引，原来的索引保留且变为普通列
#   drop = True时，删除原行索引行
#   level   控制了具体要还原的那个等级的索引
#   inplace 输入布尔值，表示当前操作是否对原数据生效，默认为False

# print(df.reset_index())
# print(df.reset_index(drop=True))
# ------------------------
# 将 DataFrame 中的列转化为行索引
# df.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)
#   key     列索引名称或者列索引名称的列表
#   drop    默认为True，删除用作新索引的列，为False时则保留
#   append  是否将列附加到现有索引，默认为False(True则保留原索引，也就是双索引)
#   inplace 输入布尔值，表示当前操作是否对原数据生效，默认为False
#   verify_integrity    默认为false，检查新索引的副本

# df = pd.DataFrame({'date': ['周一', '周二', '周三', '周四', '周五'],
#                    'name': ['Albert', 'John', 'Lin', 'Tom', 'Jack'],
#                    'age': [17, 18, 25, 31, 20]}, index=range(1, 6))
# print(df)
# print(df.set_index('date'))
# print(df.set_index('age', drop=False))

# -----------------------------------------------------------------------------------
# pandas 基本数据操作
# -----------------------------------------------------------------------------------
# 索引操作

# 切片
# 1. 直接对对象进行行切片
# 2. 只显示所选列，需要两个中括号，然后填入要显示的列名
# print(df)
# print(df[3:6])
# print(df[['2021-08-02', '2021-08-06']])

# 直接使用行列索引(先列后行)，方括号内为索引值，且只能填一个值，不可切片
# df = pd.DataFrame({'date': ['周一', '周二', '周三', '周四', '周五'],
#                    'name': ['Albert', 'John', 'Lin', 'Tom', 'Jack'],
#                    'age': [17, 18, 25, 31, 20]}, index=range(1, 6))
# #
# print(df['name'][2])

# ----------------------------
# 结合loc或者iloc使用索引(先行后列)
#   loc     只能指定行列索引的名字
#   iloc    索引的下标值获取

# print(df)
# print(df.loc['股票1':'股票3', '2021-08-03'])
# print(df.iloc[:3, :4])

# 混合索引值与索引下标的索引方法(columns也有get_indexer方法)
# print(df.loc[df.index[:4], ['2021-08-02', '2021-08-03']])
# print(df.iloc[df.index.get_indexer(['股票1', '股票2', '股票3', '股票4']), :2])

# -------------------------------------------------
# 赋值操作(通过上面的索引方法，对选中目标进行赋值)

# df.columns = ['a', 'b', 'c_C', 'd1', 'e']
# print(df)
# df['a'] = 0
# df['c_C']['股票5'] = 99999
# print(df)
# # ↓列名符合Python命名规范的，可以通过类似属性的方式访问赋值(特别用法)
# df.c_C = 100
# df.d1 = 200
# df.iloc[:3, :4] = 0
# print(df)

# -------------------------------------------------
# df.sort_values(by, ascending=True, inplace=False)
#   按索引值排序
# df.sort_index(axis=0, ascending=True, inplace=False)
#   按索引排序
#   axis        默认为0按行索引排序，1是按列索引排序
#   ascending   是否升序，False为倒序
#   inplace     是否对原数组修改，默认不修改

# df.columns = ['a', 'b', 'c', 'e', 'd']
# print(df)

# 按某一列或者多列内容进行排序，by参数为列表时，前面的排序优先级更高(前面的值相等时启用)
# print(df.sort_values(by=['c', 'd'], ascending=True))
# print(df.sort_index())
# # print(df.sort_index(axis=1))

# -------------------------------------------------------------------------
# Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型
# pandas.Series(data=None, index=None, dtype=None, name=None, copy=False)
#   data    一组数据(ndarray 类型)
#   index   数据索引标签，如果不指定，默认从 0 开始
#   dtype   数据类型，默认会自己判断
#   name    设置名称
#   copy    拷贝数据，默认为 False

# series 排序
# series = pd.Series(['c', 'a', 'f', 'b', 'e', 'd'], index=[6, 3, 2, 4, 1, 5])
# print(series)
# print(series.sort_index())
# print(series.sort_values())

# -------------------------------------------------------------------------

dataframe = pd.read_csv('stock_day.csv').drop(['ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20'], axis=1)

# -------------------------------------------------------------------------
# DataFrame 运算

# -----------------------------------------------
# 算术运算

# add() 相加，sub() 相减.....
# 也可以直接用符号
# 有返回值，不修改原值

# print(dataframe)
# print(dataframe.iloc[:, 1:4].add(100))
# print(dataframe['close'].sub(5))
# dataframe['high'] += 10
# print(dataframe)

# -----------------------------------------------
# 逻辑运算(>,<,|,&)
# | 相当于or, & 相当于and，使用时注意优先级，酌情加括号

# print(dataframe['p_change'] > 2)
# print(dataframe[dataframe['p_change'] > 2])
# print(dataframe[(dataframe['p_change'] > 2) & (dataframe['open'] > 15)])
# print(dataframe[(dataframe['p_change'] < 1) | (dataframe['open'] < 15)])

# -----------------
# 逻辑运算函数(query, isin)
# -----------------
# query(expr, inplace=False)
#   直接放条件即可，比上面更简单
#   返回dataframe对象

# print(dataframe.query("p_change > 2 & open > 15").head())
# -----------------
# isin(values)
#   筛选出某列含有某个值的数据，可以填一个值或者多个值的列表

# print(dataframe[dataframe['turnover'].isin([4.19, 2.39])].to_string())

# ---------------------------------------------------------------------
# 统计运算

# dataframe.describe()
#   综合分析，能够直接得出很多统计结果，count、mean、max、min、std

# print(dataframe)
# print(dataframe.describe())

# 单个方法
#   sum()   求和
#   mean()  算术平均值
#   median()中位数
#   max()   最大值
#   mix()   最小值
#   mode()  众数
#   abs()   绝对值
#   prod()  乘积
#   std()   标准差
#   var()   方差
#   idxmax() 最大值索引值(是标题，不是下标)
#   idxmin() 最小值索引值(是标题，不是下标)

# print(dataframe.sum())
# print(dataframe[:10].prod())
# print(dataframe.idxmax())
# print(dataframe.std())

# ---------------------------------------------------------------------
# 累计统计函数
# cumsum()  累计求和，每项数值是包含自己在内的前面所有数的累加和
# cummax()  累计最大值，类上
# cummin()  累计最小值
# cumprod() 累计乘积


# print(dataframe.cumsum())
# print(dataframe.cummax())
# print(dataframe.cummin())
# print(dataframe.cumprod())


# data = dataframe['p_change'].cumsum()
# data.plot()
# plt.show()

