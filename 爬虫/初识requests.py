# -*-  codeing = utf-8 -*-
# @Time : 2021/6/15 下午 7:29
# @Author : 漫天烟华
# @File : 初识requests.py
# @Software : PyCharm


import requests

# url = 'http://www.baidu.com'

# response = requests.get(url)
# print(type(response))   # 直接打印response只有一个响应码,类型是模块类型requests.models.Response

# ----------------------------------------------------------------------------------------------------------------

# 打印响应内容的方法

# ----------------------------------
# response.text

# print(type(response.text))  # 类型是字符串
# print(response.encoding)    # 解码类型是模块根据HTTP头部响应编码有根据的推测的文本编码
# print(response.text)        # 此时编码不准，有乱码，需要手动设置编码格式

# response.encoding = 'utf-8'
# print(response.text)            # 因为需要两行代码，一般推荐用.content而不用.text打印内容

# ----------------------------------
# response.content

# print(type(response.content))       # 类型是bytes（二进制格式）
# print(response.content.decode())    # 解码即可得到易阅读内容，decode（）默认以utf-8格式解码

# ----------------------------------------------------------------------------------------------------------------
# response 响应对象的其他常用属性及方法

# 响应的url
# print(response.url)                 # 有时候响应的url和请求的url并不一致

# 响应状态码
# print(response.status_code)

# 响应对应的请求头
# print(response.request.headers)

# 响应头
# print(response.headers)

# 响应的cookie（经过了set-cookie动作；返回cookieJar类型）
# print(response.cookies)

# print(response.request._cookies)  # 请求携带的cookie；返回cookieJar类型，没设置则为空cookieJar
# response.json()                   # 自动将json字符串类型的响应内容转换Python对象（dict or list）

# ----------------------------------------------------------------------------------------------------------------

# 发送带参数的请求（在url携带参数、通过params携带参数字典）
# 在使用百度搜索时，经常看到url地址中有一个?,问号后面的内容就是请求参数，又叫查询字符串
# tips: 通过删除url中的请求参数再回车重新进入，观察网页变化可快速找到关键的，有影响的参数

# ---------------------------------------------------------------
# 直接对含有参数的url发送请求（在url携带参数）

# url = 'https://www.baidu.com/s?wd=Python'
#
# headers = {
#         "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 88.0.4324.182 Safari / 537.36"
#     }
#
# response = requests.get(url, headers=headers)
# print(response.content.decode())

# ---------------------------------------------------------------
# 通过params携带参数字典
#   1.构建参数字典
#   2.发送请求的时候设置参数字典

# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
#         'Referer': 'https://www.baidu.com'
#     }
# url = 'https://www.baidu.com/s?'
#
# kw = {'wd': 'Python'}
#
# response = requests.get(url, headers=headers, params=kw)
# print(response.url)
# print(response.content.decode())

# ----------------------------------------------------------------------------------------------------------------
# 使用 verify 参数忽略CA证书

# url = 'http://sam.huat.edu.cn:8443/selfservice/'
#
# response = requests.get(url, verify=False, timeout=5)
# print(response.content.decode())

# ----------------------------------------------------------------------------------------------------------------

#

#


#                                                                                                             post请求
# ----------------------------------------------------------------------------------------------------------------
# post请求用途
# 1. 登陆注册时，web工程师看来post请求比get请求更安全，url地址中不会暴露用户的账号密码信息
# 2. 需要传输打文本内容的时候，因为post请求对长度没要求
# post请求需要一个字典格式的 data参数 ，其他参数与get请求一致

# url = 'https://fanyi.sogou.com/reventondc/suggV3'
#
# headers = {
#         "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 88.0.4324.182 Safari / 537.36",
#     }
# word = input('请输入您要翻译的内容:')
# data = {
#     'from': 'auto',
#     'to': 'en',
#     'client': 'wap',
#     'text': word,
#     'uuid': 'ac9370c9-5817-4a4c-b3df-ffb6c091ebd1',
#     'pid': 'sogou-dict-vr',
#     'addSugg': 'on',
# }
# response = requests.post(url, headers=headers, data=data)
#
# # print(type(response.content.decode()))  # 类型是字符串
# # print(response.content.decode())
#
# # print(type(response.json()))            # 类型是字典
# # print(response.json())
# print(response.json()['sugg'][0]['v'])

# --------------------------------
# post数据来源
#  1. 固定值           多次抓包不变化的值
#  2. 输入值           根据输入内容变化的值
#  3. 预设值-静态文件    需要提前从静态html中获取
#  4. 预设值-发请求      需要对指定地址发送请求获取数据
#  5. 在客户端生成的     分析js，模拟生成数据

# ----------------------------------------------------------------------------------------------------------------
# requests.session状态保持，原理: 自动处理发送请求获取响应过程中产生的cookie，进而保持状态
# 应用: 连续多次请求（登陆后操作）下一次请求会带上上一次的cookie
# session = requests.session() # 先实例化session对象，再用该对象进行get、post请求

# import re
# #   创建session对象
# session = requests.session()
# #   添加请求头
# session.headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
# #   访问登录页面获取部分data
# url1 = 'https://github.com/login'
# print(url1)
# html = session.get(url1, timeout=10).content.decode()
# #   正则提取data
# token = re.findall(r'<input type="hidden" name="authenticity_token" value="(.*?)" /', html, re.S)[0]
# timestamp = re.findall('name="timestamp" value="(\d*?)" class="form-control" />', html)[0]
# timestamp_s = re.findall('name="timestamp_secret" value="(.*?)" class="form-control" />', html)[0]
# #   print(token, timestamp, timestamp_s)
# #   发送post请求进行登陆
# url2 = 'https://github.com/session'
# login = input('请输入账号:')
# password = input('请输入密码:')
# data = {
#     'commit': 'Sign in',
#     'authenticity_token': token,
#     'login': login,
#     'password': password,
#     'trusted_device': '',
#     'webauthn-support': 'supported',
#     'webauthn-iuvpaa-support': 'unsupported',
#     'return_to': '',
#     'allow_signup': '',
#     'client_id': '',
#     'integration': '',
#     'required_field_510e': '',
#     'timestamp': timestamp,
#     'timestamp_secret': timestamp_s,
# }
# session.post(url2, data=data)
# #   验证是否登录成功
# response = session.get('https://github.com/liaofaz')
# title = re.findall('<title>.*?</title>', response.text)
# print(title)    # 标题如果有 · GitHub则没有登陆成功，纯用户名则成功

# ----------------------------------------------------------------------------------------------------------------


