# -*-  codeing = utf-8 -*-
# @Time : 2021/3/17 下午 2:28
# @Author : 漫天烟华
# @File : url.py
# @Software : PyCharm


import urllib.request

#获取一个get请求（整个网页的源码）
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))   #对获取到的网页源码进行utf-8解码



#获取一个post请求(模拟用户真实登录的时候，模拟浏览器真实发出的请求，用data以字节的形式封装数据（用户名、密码）)
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))



# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=3)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!!")


# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.status)             #状态码
# print(response.getheaders())       #头部信息（响应头）
# print(response.getheader('Date'))  #获取特定的响应头




#模仿浏览器访问

# url = "http://httpbin.org/post"
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# req = urllib.request.Request(url=url,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


# url = "http://douban.com"
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
# }
# req = urllib.request.Request(url=url,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
