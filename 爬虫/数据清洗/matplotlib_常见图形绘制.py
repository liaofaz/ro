# -*- codeing = utf-8 -*-
# @Author : 漫天烟华
# @Software : pycharm
# @Version: Python 3.9.4

from matplotlib import pyplot as plt
import numpy as np

# plt.rc('font', family='SimHei', size=15) # 不知道有没有用
# 设置字体为黑体(显示中文)，显示负号'-'
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1.折线图 -- plt.plot(x, y)
#   变化
# 2.散点图 -- plt.scatter(x, y)
#   分布规律
# 3.柱状图 -- plt.bar(x, width, align='center', **kwargs)
#   统计、对比
# 4.直方图 -- plt.hist(x, bins=None)
#   统计、分布
# 5.饼状图 -- plt.pie(x, labels=, autopct, colors)
#   占比

# -------------------------------------------------------------------
# 散点图

# x = [225.98, 247.07, 253.14, 457.85, 241.58, 301.01, 20.67, 288.64,
#         163.56, 120.06, 207.83, 342.75, 147.9, 53.06, 224.72, 29.51,
#         21.61, 483.21, 245.25, 399.25, 343.35]
# y = [196.63, 203.88, 210.75, 372.74, 202.41, 247.61, 24.9, 239.34,
#         140.32, 104.15, 176.84, 288.23, 128.79, 49.64, 191.74, 33.1,
#         30.74, 400.02, 205.34, 330.64, 283.45]
#
# plt.figure(figsize=(20, 8), dpi=100)
#
# plt.scatter(x, y)
#
# plt.show()

# -------------------------------------------------------------------
# 柱状图

# x = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim']
# y = [5, 20, 15, 25, 10]
#
# plt.bar(range(len(x)), y)
# plt.xticks(range(len(x)), x, fontsize=15)
# plt.yticks(y, fontsize=15)
# plt.title('岁数')
# plt.grid(linestyle='--', alpha=0.5)
#
# plt.show()
# --------------
# 堆叠柱状图

# label_list = ['2014', '2015', '2016', '2017']
# num_list1 = [20, 30, 15, 35]
# num_list2 = [15, 30, 40, 20]
# x = range(len(num_list1))
# rects1 = plt.bar(x, height=num_list1, width=0.45, alpha=0.8, color='red', label="一部门")
# rects2 = plt.bar(x, height=num_list2, width=0.45, color='green', label="二部门", bottom=num_list1)
# plt.ylim(0, 80)
# plt.ylabel("数量")
# plt.xticks(x, label_list)
# plt.xlabel("年份")
# plt.title("某某公司")
# plt.legend()
# plt.show()
# -------------------------------------------------------------------
# 直方图
# 绘制直方图
# data: 必选参数，绘图数据
# bins: 直方图的长条形数目，可选项，默认为10
# normed:    是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率(出现次数/总数)
# facecolor: 长条形的颜色
# edgecolor: 长条形边框的颜色
# alpha:     透明度

# x = np.random.randn(10000)
#
# plt.figure()
# plt.hist(x, 50)
# plt.grid(alpha=0.1)
#
# plt.show()

# -------------------------------------------------------------------
# 饼状图
# explode：设置各部分突出
# labels:设置各部分标签
# labeldistance:设置标签文本距圆心位置，1.1表示1.1倍半径
# autopct：设置圆里面文本
# shadow：设置是否有阴影
# startangle：起始角度，默认从0开始逆时针转
# pctdistance：设置圆内文本距圆心距离
# 返回值
# l_text：圆内部文本，matplotlib.text.Text object
# p_text：圆外部文本


# label_list = ["第一部分", "第二部分", "第三部分"]    # 各部分标签
# size = [55, 35, 10]    # 各部分大小
# color = ["red", "green", "blue"]     # 各部分颜色
# explode = [0.05, 0, 0]   # 各部分突出值
#
# patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
# plt.axis("equal")    # 设置横轴和纵轴大小相等，这样饼才是圆的
# plt.legend()
# plt.show()
