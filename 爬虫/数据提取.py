# -*- codeing = utf-8 -*-
# @Time : 2021/6/23 上午 3:48
# @Author : 漫天烟华
# @File : 数据提取.py
# @Software : PyCharm


# 数据类型
# ----------------------
# 按响应分类（结构化、非结构化）
# ----------------------
# 结构化数据
# 1.json数据（常见）,提取数据方式:
#   json模块
#   re模块
#   jsonpath模块
# 2.xml数据（少见）,提取数据方式:
#   re模块
#   lxml模块
# ----------------------
# 非结构化数据
# html字符串,提取数据方式:
#   re模块
#   lxml模块          xpath语法
#   beautifulsoup    xpath、正则、css选择器
#   pyquery          css选择器
# -----------------------------------------------------------------------------------------------------------
# jsonpath 模块

# 在多层嵌套的复杂字典中，想要根据key和下标来批量提取value，是非常困难的且不高效的
# jsonpath 可以帮助我们用更高效简洁的方法实现目的

# 常用语法
# $     根节点（最外层的大括号）
# .     子节点
# ..    子孙节点（可以跳级，类似xpath的//）
#

import requests
import jsonpath

# 拉勾网城市接口
# url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
# response = requests.get(url, headers=headers)
# jsons = response.json()
#
# city_name = jsonpath.jsonpath(jsons, '$..G..name')
# city_code = jsonpath.jsonpath(jsons, '$..G..code')
# print(city_name)
# print(city_code)
# -----------------------------------------------------

bookstore = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}

# author = jsonpath.jsonpath(bookstore, '$..author')
# print(author)   # '$.store.book[*].author' 也可以找出该例子的作者
# price = jsonpath.jsonpath(bookstore, '$..price')
# print(price)
# test = jsonpath.jsonpath(bookstore, '$..book[?(@.price>10)]')
# print(test)


# -----------------------------------------------------------------------------------------------------------
# xpath 部分...略
