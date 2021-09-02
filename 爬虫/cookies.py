# -*-  codeing = utf-8 -*-
# @Time : 2021/6/16 上午 8:40
# @Author : 漫天烟华
# @File : cookies.py
# @Software : PyCharm


import requests

# 网站经常利用请求头中的Cookie字段来做用户访问状态的保持，那么我们可以在headers参数中添加Cookie，来模拟用户请求

# ------------------------------------------------------------------------------------------------------------------
# 在 headers 参数中携带Cookie
# -----------------------------------------

# url = 'https://github.com/liaofaz'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
#     'cookie': '_octo=GH1.1.1372903998.1622991875; _device_id=9fcb7883acf974d7a6cca12c474f7673; user_session=H4sRthfQDf0r0OaWEc6FBy4fFYw2NttU1xtUm-oOU_YhaexI; __Host-user_session_same_site=H4sRthfQDf0r0OaWEc6FBy4fFYw2NttU1xtUm-oOU_YhaexI; logged_in=yes; dotcom_user=liaofaz; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai'
#     }
#
# response = requests.get(url, headers=headers, timeout=10)
# print(response.url)
# print(response.content.decode())

# -------------------------------------------------------------------------------------------------------------------
# 用requests.get里的cookies参数传入字典cookies
# -----------------------------------------

# url = 'https://github.com/liaofaz'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
# }
#
# temp = '_octo=GH1.1.1372903998.1622991875; _device_id=9fcb7883acf974d7a6cca12c474f7673; user_session=H4sRthfQDf0r0OaWEc6FBy4fFYw2NttU1xtUm-oOU_YhaexI; __Host-user_session_same_site=H4sRthfQDf0r0OaWEc6FBy4fFYw2NttU1xtUm-oOU_YhaexI; logged_in=yes; dotcom_user=liaofaz; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FShanghai'
#
# cookie = {i.split('=')[0]:i.split('=')[1] for i in temp.split('; ')}
# print(cookie)
# response = requests.get(url, headers=headers, cookies=cookie, timeout=10)
# print(response.url)
# print(response.content.decode())

# -------------------------------------------------------------------------------------------------------------------
# cookieJar 与 cookie 字典的相互转换
# 使用 requests 获取的response对象，具有cookie属性。response.cookie属于cookieJar类型，包含对方服务器设置在本地的cookie

# url = 'https://www.baidu.com/'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
# }
#
# response = requests.get(url, headers=headers)
#
# # 复杂的方法
# cookie_dict1 = requests.utils.dict_from_cookiejar(response.cookies)
# cookie_jar1 = requests.utils.cookiejar_from_dict(cookie_dict1)
# print(cookie_dict1)
# print(cookie_jar1)
#
# # 稍微简单的方法，从cookieJar 中提取 cookie 字典
# cookie_dict2 = response.cookies.get_dict()
# print(cookie_dict2)

# -------------------------------------------------------------------------------------------------------------------

# 超时参数 timeout 可在get请求或者post请求中设置，超出时间时直接抛出异常，避免过长等待

# -------------------------------------------------------------------------------------------------------------------

# 请求中的 proxy 参数指向的是正向代理服务器。知道服务器真实ip地址的为正向代理（如VPN），不知道的为反向（如nginx）

# 代理 ip 的分类
# -------------
# 根据代理ip的匿名度可分为三类
#  1. 透明代理: 虽然可以隐藏你的ip地址，但是还是可以间接查到ip

#  2. 匿名代理: 服务器知道使用了代理，但是不知道ip

#  3. 高匿代理: 让服务器无法你发现在使用代理

# 根据网站使用协议分类
#  1） http代理
#  2） https代理
#  3） socks隧道代理（如socks5代理）特点如下:
#       i.socks代理只是简单地传递数据包，不关心是何种应用协议（FTP、HTTP、HTTPS）
#       ii.socks代理比http、https代理耗时少
#       iii.socks代理可以转发http和https的请求

# -------------------------------------------------------------------------------------------------------------------

