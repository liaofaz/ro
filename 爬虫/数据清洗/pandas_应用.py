# -*- codeing = utf-8 -*-
# @Time:    2021/8/16 上午 8:20
# @Author:  漫天烟华
# @Software: PyCharm
# @Version:  Python 3.9.4


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. 显示所有行、列
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', None)

# dataframe = pd.read_excel('history_A_stock_k_data.xlsx', index_col='date')
# dataframe = dataframe.drop(['code', 'adjustflag', 'tradestatus', 'isST', 'amount'], axis=1)
# print(dataframe)
# # 2. 把 dataframe 以字符串形式输出，比起上面的方法，不会把显示不了的列换行，缺点是会显示全部数据(不省略)
# print(dataframe.to_string())

dataframe = pd.read_csv('stock_day.csv')

# -------------------------------------------------------------
# 自定义运算(求列或行数据的某个自定义值时使用)
# apply(func, axis=0)
#   func: 自定义函数
#   axis: 默认值为0，按列运算；axis=1则按行运算

# print(dataframe[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0))

# -------------------------------------------------------------
# Pandas 画图
# dataframe.plot(x=None, y=None, kind='line')
#   x 标签或者位置
#   y 标签或位置，或它们的列表
#   kind: str
#       'line'  折线图
#       'bar'   条形图
#       'barh'  横向条形图
#       'hist'  直方图
#       'pie'   饼状图
#     'scatter' 散点图
#
# dataframe.plot()
# plt.show()

# ---------------------------------------------------------------------------------
# 文件读取与存储
# 类型         读取            存储
# CSV       read_csv        to_csv
# JSON      read_json       to_json
# HDF5      read_hdf        to_hdf
# HTML      read_html       to_html
# MS Excel  read_excel      to_excel
# SQL       read_sql        to_sql
# .......

# 读取与存储 CSV 文档数据
#   pd.read_csv(filepath_or_buffer, sep=',', usecols=None)
#       filepath_or_buffer  文件路径
#       usecols     指定读取的列名，列表形式
#   DataFrame.to_csv(path_or_buf=None, sep=', ’, columns=None, header=True, index=True, mode='w', encoding=None)
#       path_or_buf     字符串或文件句柄, 默认值 None
#       sep             分割方式, 默认','
#       columns         需要写入的列名列表
#       mode            'w'：重写, 'a' 追加
#       index           是否写进 行索引
#       encoding        编码格式
#       header          布尔类型或字符串列表, 默认 True,是否写进列索引值


# data = pd.read_csv('stock_day.csv', usecols=['open', 'close'])
# print(data.head())
# dataframe[:10].to_csv("test.csv", columns=['open'])

# -------------------------------
# 读取与存储 hdf5文件 数据
# pandas.read_hdf(path_or_buf，key =None，** kwargs)
# DataFrame.to_hdf(path_or_buf, key, *\kwargs*)
#   path_or_buffer  文件路径
#   key             读取的键
#   return          Theselected object

# # #安装不了模块，跳过
# # day_eps_ttm = pd.read_hdf("day_eps_ttm.h5")
# # print(day_eps_ttm)
# # day_eps_ttm.to_hdf("test.h5", key="day_eps_ttm")
# # #再次读取的时候, 需要指定键的名字
# # new_eps = pd.read_hdf("test.h5", key="day_eps_ttm")
# -------------
# 优先选择使用HDF5文件存储(用到再说...版本高pytable模块不兼容)
#   HDF5在存储的时候支持压缩，使用的方式是blosc，这个是速度最快的也是pandas默认支持的
#   使用压缩可以提磁盘利用率，节省空间
#   HDF5还是跨平台的，可以轻松迁移到hadoop 上面
# -------------------------------
# 读取、存储 json文档 数据
# pandas.read_json(path_or_buf=None, orient=None, typ='frame', lines=False)
#   将JSON格式准换成默认的Pandas DataFrame格式
#   orient  输入字符串，表示预期的JSON字符串格式，根据json文件内容选择
#       'split'     {index: [index], columns: [columns], data: [values]}
#                   将索引总结到索引，列名到列名，数据到数据。将三部分都分开了
#       'records'   以{columns:values},{column:value}的形式输出
#       'index'     以index:{columns：values},...的形式输出
#       'columns'   以columns:{index:values}的形式输出,默认该格式
#       'values'    values 直接输出值
#   lines   按照每行读取json对象,布尔值,默认 False(只能在orient为records时使用)
#   typ : 默认frame,指定转换成的对象类型series或者dataframe

# data = pd.read_json('Sarcasm_Headlines_Dataset.json', orient='records', lines=True)
# print(data)
# dataframe.to_json('test.json', orient='records', lines=True)

# ---------------------------------------------------------------------------------

# Pandas 高级处理

# ---------------------------------------------------------------------------------
# 缺失值处理


# 缺失值的类型为 float
# print(type(np.NaN))

# 缺失值的处理
# 1.判断数据是否为NaN
#   np.any(dataframe.isnull())
#   np.all(dataframe.notnull())
# 2.缺失值 NaN 处理
#   删除 NaN 缺失值
#     dataframe.dropna(axis=0, inplace=False, how=None)
#   替换缺失值 NaN (暂时发现只能一列列替换)
#     dataframe[columns].fillna(value=None,method=None,axis=None,inplace=False,limit=None,downcast=None)
# 3.非 NaN 缺失值处理
#   先替换为NaN,再进行步骤二
#   dataframe.replace(to_replace=None,value=None,inplace=False)
#       to_replace  替换前的值
#       value       替换后的值(可填np.nan)

# ---------------------------------------------------
movie = pd.read_csv('IMDB-Movie-Data.csv')

# 删除缺失值 NaN
# print(np.any(movie.isnull()))
# # print(np.all(movie.notnull()))
# movie.dropna(inplace=True)
# print(np.any(movie.isnull()))

# 替换缺失值 NaN
# for i in movie.columns:
#     if np.any(movie[i].isnull()):
#         print(i)
#         movie[i].fillna(movie[i].mean(), inplace=True)
# print(movie)
# print(np.any(movie.isnull()))

# ---------------------------------------------------------------------------------
# 数据离散化
# 1.等距(宽)划分区间
# pandas.cut(x,bins,right=True,labels=None,retbins=False,precision=3,include_lowest=False,duplicates="raise",ordered=True)
#   对数据从最大值到最小值进行等距划分
# 2.等频划分区间
# pandas.qcut(x,q,labels=None,retbins=False,precision=3,duplicates='raise')
#    按照数据出现频率百分比划分
#    x         输入待cut的一维数组
#   bins       cut的段数，一般为整型，但也可以为序列向量。
#    q         qcut的段数，一般为整型，但也可以为百分比序列
#   right      布尔值，确定右区间是否开闭，默认取True时右区间闭合
#   labels     数组或布尔值，默认为None，用来标识分后的bins，长度必须与结果bins相等，返回值为整数或者对bins的标识
#   retbins    布尔值，可选。是否返回数值所在分组，Ture则返回
#   precision  整型，bins小数精度，也就是数据以几位小数显示
#   include_lowest 布尔类型，是否包含左区间
#   duplicates  如果箱子边缘不是唯一的，则 'raise' ValueError或'drop'删除非唯一性
# pd.value_counts(dataframe)    统计分组次数

p_change = dataframe['p_change']

cut = pd.cut(p_change, bins=5)
# print(pd.value_counts(cut))
#
qcut = pd.qcut(p_change, q=5)
# print(pd.value_counts(qcut))

# bins = [-15, -7, -3, 0, 3, 7, 15]
# q = [0, 0.25, 0.5, 0.75, 1]
# print(pd.cut(p_change, bins=bins))
# print(pd.qcut(p_change, q=q))

# -----------------------------------
# one-hot 编码(哑编码,热独编码)
# 0,1 统计类型，把每个类别生成一个布尔列，这些列中只有一列可以为这个样本取值为1，其他为0
# pandas.get_dummies(data, prefix=None)
#   data    array-like, Series,或者 DataFrame
#   prefix  分组名字

# print(pd.get_dummies(cut).head())

# ---------------------------------------------------------------------------------
# 合并

# pd.concat(objs, axis=0)
#   函数可以沿着指定的轴将多个 DataFrame 或者 series 拼接到一起
#   axis默认值0按列拼接(共用列索引)，1为按行拼接(共用行索引)

# print(pd.concat([p_change, cut], axis=1))


# pd.merge(left, right, how="inner", on=None, left_on=None, right_on=None)
#   left    左表(DataFrame object)
#   right   右表(DataFrame object)
#   how     拼接方式
#        比对左右表on内的键，inner内连接取交集，outer外连接取并集
#       'inner' 左右表键值相同就合并行，如右边依然有相同就继续合并，不相同则左表下一行继续比对，直到左表尽头
#       'left'  大体同inner，但是左右找不到相同时，保留左表而右边部分继承列索引然后NaN填充
#       'right' 左右表键值相同就合并，多条相同分别合并，左表没有的用NaN填充
#       'outer' 相当于left，right结合版，键值相同分别合并，没有找到同的各自填充NaN成新行
#   on      指定键
#   left_on=None, right_on=None：指定左右键

# left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
#                      'key2': ['K0', 'K1', 'K0', 'K1'],
#                      'A': ['A0', 'A1', 'A2', 'A3'],
#                      'B': ['B0', 'B1', 'B2', 'B3']})
# right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
#                       'key2': ['K0', 'K0', 'K0', 'K0'],
#                       'C': ['C0', 'C1', 'C2', 'C3'],
#                       'D': ['D0', 'D1', 'D2', 'D3']})

#    key1 key2  A   B  |    key1 key2  C   D
# 0   K0   K0  A0  B0  |  0   K0   K0  C0  D0
# 1   K0   K1  A1  B1  |  1   K1   K0  C1  D1
# 2   K1   K0  A2  B2  |  2   K1   K0  C2  D2
# 3   K2   K1  A3  B3  |  3   K2   K0  C3  D3
# print(pd.merge(left, right, on=['key1', 'key2']))
# print(pd.merge(left, right, on=['key1', 'key2'], how='left'))
# print(pd.merge(left, right, on=['key1', 'key2'], how='right'))
# print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))

# ---------------------------------------------------------------------------------
# 交叉表和透视表
# 探索两列数据之间的关系
# 1.交叉表
# pandas.crosstab(dataframe[key1], dataframe[key2])
#   返回具体数量，key1、key2是列索引值
# 2.透视表
# dataframe.pivot_table([values], index=index)
#   同值行索引计算平均值，如果数据只有0和1的话，就相当于计算1出现的数量在总数的占比
# pandas.pivot_table(data, values=None, index=None)
#   data    透视表的对象
#   index   新的行索引(填入原表的列名)，可填多个形成多个行索引的透视表(按主次，但是好像只能整理数字数据)
#   values  对数据筛选，其实就是新表展示哪些列
#   行索引出现多个相同值时，默认参数aggfunc='mean'计算均值，合并为一个


# 提取行索引日期，转化为星期几
# print(dataframe.index)
date = pd.to_datetime(dataframe.index).weekday
dataframe['week'] = date

# 根据p_change的值新建p_n列，大于0的赋值1，否则0
dataframe['p_n'] = np.where(dataframe['p_change'] > 0, 1, 0)
# print(dataframe)

# 根据数值生成交叉表
# cou = pd.crosstab(dataframe['week'], dataframe['p_n'])
# print(cou)
# 对每行数据求和
# sum_ = cou.sum(axis=1)
# print(sum_)
# 每列数据除以所在行的和得出比值
# pro = cou.div(sum_, axis=0)
# print(pro)
# 根据数据绘制堆叠柱状图
# pro.plot(kind='bar', stacked=True)
# plt.show()

# 计算week列中各同行名索引值的总和的平均值(间接求得1在0+1总数的占比)
# print(dataframe.pivot_table('p_n', index='week'))

# ---------------------------------------------------------------------------------
# 分组与聚合
col = pd.DataFrame({'color': ['white', 'red', 'green', 'red', 'green'],
                    'object': ['pen', 'pencil', 'pencil', 'ashtray', 'pen'],
                    'price1': [5.56, 4.20, 1.30, 0.56, 2.75],
                    'price2': [4.75, 4.12, 1.60, 0.75, 3.15]})

# 分组的两种方法(得到的是一个分组对象，一般还需要聚合操作)
# 1. DataFrame.groupby(key, as_index=False)
# 2. DataFrame[columns].groupby(DataFrame[key])
#   key      分组的列数据，可以多个
#  as_index  是否把key列设为行索引，默认True，为False时保留key列数值

# print(col.groupby('color')['price1'].mean())
# print(col['price1'].groupby(col['color']).mean())
# print(col.groupby('color', as_index=False).mean())


starbucks = pd.read_csv('directory.csv')
starbucks['count_'] = 0    # 建一个列专门显示数据

# 星巴克世界各国门店总数 top20
# count_ = starbucks.groupby('Country').count()[['count_']]
# top20 = count_.sort_values('count_', ascending=False)[:20]
# # print(top20)
# top20.plot(kind='bar')
# plt.show()

# count_2 = starbucks.groupby(['Country', 'State/Province']).count()[['count_']]
# province = count_2.sort_values(['Country', 'count_'])
# print(province)

# ---------------------------------------------------------------------------------
# 电影案例数据分析实战

rating = movie['Rating']
runtime = movie["Runtime (Minutes)"]
# print(rating.mean())    # 评分平均分
# print(movie['Director'].unique().size)  # 导演总数


# # Rating，Runtime (Minutes)的分布情况

# plt.rc('font', family='SimHei', size=15)
# fig, axes = plt.subplots(nrows=2, ncols=1)
# axes[0].hist(rating.values, bins=20)
# axes[1].hist(runtime.values, bins=20)
# xticks1 = np.linspace(rating.min(), rating.max(), 21)
# xticks2 = np.linspace(runtime.min(), runtime.max(), 21)
# axes[0].set_xticks(xticks1)
# axes[1].set_xticks(xticks2)
# axes[0].set_xlabel('评分', fontsize=20)
# axes[1].set_xlabel('电影时长（分钟）', fontsize=20)
# axes[0].grid(linestyle='--', alpha=0.5)
# axes[1].grid(linestyle='--', alpha=0.5)
# plt.show()


# 电影分类统计

# 1. 自编取巧型
# g_list = []
# for i in movie['Genre']:
#     g_list.extend(i.split(','))
# # print(g_list)
# data = pd.DataFrame(g_list)
# print(data.value_counts())
# data.value_counts().plot(kind='bar', figsize=(20, 8))
# plt.show()

# 2. 黑马教程方法
# # 1）对数据分列处理得到电影类型列表temp_list
# temp_list = [i.split(',') for i in movie['Genre']]
# # 2）对电影类型去重，得到类型列表genre_list
# genre_list = pd.unique([j for i in temp_list for j in i])
# # 3) 以类型列表为列索引，建一个与原表行长度相等的dataframe(数据全为0)
# data = pd.DataFrame(np.zeros((movie.shape[0], genre_list.size)), columns=genre_list)
# # 4）把每行电影类型列表temp_list对应的值变为1
# for i in range(movie.shape[0]):
#     data.loc[i, temp_list[i]] = 1
# # 5）求和得到每个类型的数量，然后绘图
# print(data.sum().sort_index())
# data.sum().sort_index().plot(kind='bar', figsize=(20, 8), fontsize=18)
# plt.show()
