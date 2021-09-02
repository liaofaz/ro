# -*- codeing = utf-8 -*-
# @Time : 2021/8/9 下午 8:10
# @Author : 漫天烟华
# @Software : VScode
# @Version: Python 3.9.4


# Matplotlib
#   专门用于开发2D图表（包括3D图表）
#   使用简单
#   以渐进、交互式方式实现数据可视化

# matplotlib 三层结构
#   容器层
#    | Canvas     最底层的系统层，相当于画板，即放置Figure的工具
#    | Figure     Canvas的上一层，也是需要用户操作设置的应用层第一层，相当于画布
#    | Axes       应用层第二层，在Figure之上，相当于绘图区
#   辅助显示层
#    | Axes区域内的除了图像(层)以外的内容，主要包括Axes外观(facecolor)、边框线(spines)、坐标轴(axis)、坐标轴名称(axis label)、坐标轴刻度(tick)、坐标轴刻度标签(tick label)、网格线(grid)、图例(legend)、标题(title)等
#   图像层
#    | Axes内通过plot(折线图)、scatter(散点图)、bar(柱状图)、histogram(直方图)、pie(饼状图)等函数根据数据绘制出的图像


# 折线图基础绘图流程
# 1.创建画布
#   plt.figure()
# 2.绘制图像
#   plt.plot()
# 3.显示图例
#   plt.legend()
#   需要plot里设置了label参数才可用,参数(loc)默认值为0或者'best'
# 4.添加x、y轴刻度
#   plt.xticks()
#   plt.yticks()
#   注:第一个参数必须为数字，如需求不是数字请添加第二参数实现替换功能
# 5.添加网格
#   plt.grid()
#   参数如下:
#     linestyle 网格样式,与图形绘制样式同
#     alpha     透明度(推荐0.5,0.7)
# 6.添加描述信息
#   plt.xlabel()
#   plt.ylabel()
#   plt.title()
#   可选参数:fontsize 调节字体大小
# 7.保存图像
#   plt.savefig()
#   参数为路径(文件名.png)
#   图像保存要放在show前面，否则会保存空白图片
# 8.显示图像
#   plt.show()
# 9.多个坐标系图像显示
#   fig, axes = plt.subplots()
#       nrows -- 坐标系行数
#       ncols -- 坐标系列数
#       其他参数与单个坐标系同
#   除了创建画布不同，其他设置需要对axes切片之后设置，有些方法需要在前面加'set_'

# 拓展
# plt.plot()除了画折线图，还可以用于各种数学函数图像


# -------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import random

# 绘制简单折线图
# plt.figure(figsize=(20, 8), dpi=100)

# x = [1, 2, 3]
# y = [4, 5, 6]

# plt.plot(x, y)

# plt.savefig('plot.png')

# plt.show()

# -------------------------------------------------------------------------------------------
# 绘制基础的折线图

# 创建画布
# plt.figure()

# # 设置字体为黑体
# plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False    #用来正常显示负号
# #有中文出现的情况，需要u'内容'

# # 生成数据
# x = range(60)
# y_beijing = [random.uniform(15,25) for i in x]
# y_guangzhou = [random.uniform(25,35) for i in x]

# # 绘制图形
# plt.plot(x,y_beijing,label='北京',color='b',linestyle='-.')
# plt.plot(x,y_guangzhou,label='广州')
# # 绘制图形颜色设置
#     # color参数设置，可选值r(红色),g(绿色),b(蓝色),w(白色),c(青色),m(洋红),y(黄色),k(黑色)
# # 绘制图形样式设置
#     # linestyle参数来设置，可选值有'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
# # 显示图例(需要plot里设置了label参数才可用),参数默认为0或者'best'
# plt.legend(loc='best')

# # 添加x,y轴刻度
# x_ticks_label = [f'12h:{i}min' for i in x]
# y_ticks_label = range(10,30)
# plt.xticks(x[::5],x_ticks_label[::5])
# plt.yticks(y_ticks_label)
# # ps:参数一的元素为数字，否则报错

# # 添加网格
# plt.grid(True,linestyle='--',alpha=1)

# # 添加描述
# plt.xlabel('时间',fontsize=20)
# plt.ylabel('温度',fontsize=20)
# plt.title('一小时温度变化图',fontsize=40)

# # 图像保存
# # plt.savefig('plot.png')

# # 图像展示
# plt.show()

# -------------------------------------------------------------------------------------------
# 多个坐标系显示图像

# 设置字体为黑体(显示中文)，显示负号'-'
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False

# # 创建画布
# fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(20,8), dpi=100)

# # 生成数据
# x = range(60)
# y_beijing = [random.uniform(15,25) for i in x]
# y_guangzhou = [random.uniform(25,35) for i in x]

# # 图像绘制,显示图例
# axes[0].plot(x, y_beijing, label='北京', color='b', linestyle='-')
# axes[1].plot(x, y_guangzhou, label='广州', color='r', linestyle='-.')
# axes[0].legend()
# axes[1].legend()

# # 添加x,y轴刻度
# axes[0].set_xticks(x[::5])
# axes[0].set_xticklabels([f'12:{i:02}' for i in x][::5])
# axes[0].set_yticks(range(41)[::5])
# axes[1].set_xticks(x[::5])
# axes[1].set_xticklabels([f'12:{i:02}' for i in x][::5])
# axes[1].set_yticks(range(41)[::5])

# # 添加网格显示
# axes[0].grid(True, linestyle='--', alpha=0.5)
# axes[1].grid(True, linestyle='--', alpha=0.5)

# # 添加刻度描述
# axes[0].set_xlabel('时间', fontsize=20)
# axes[0].set_ylabel('温度°C', fontsize=20)
# axes[1].set_xlabel('时间', fontsize=20)
# axes[1].set_ylabel('温度°C', fontsize=20)
# axes[0].set_title('北京1小时气温', fontsize=40)
# axes[1].set_title('广州1小时气温', fontsize=40)

# # 图像展示
# plt.show()

# -------------------------------------------------------------------------------------------
# 绘制函数函数图像

# import numpy as np

# plt.figure(figsize=(20, 8), dpi=100)

# x = np.linspace(-10, 10, 100)
# y = np.sin(x)
# # y = x**2

# plt.plot(x, y)


# plt.grid()

# plt.show()
