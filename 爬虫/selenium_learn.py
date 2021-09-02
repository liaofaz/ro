# -*- codeing = utf-8 -*-
# @Time : 2021/7/12 下午 7:22
# @Author : 漫天烟华
# @File : selenium_learn.py
# @Software : PyCharm


# ------------------------------------------------------------------------------------

# selenium 是一个Web的自动化测试工具,可以调用主流浏览器，让其加载页面获取需要的数据，甚至页面截图
# selenium 可以大幅降低爬虫编写难度，但同时也大幅降低性能、效率，非必要不建议使用
# 开发用有头(界面)浏览器，部署服务器时用无头(界面)浏览器.(有界面易于纠正错误)

# 原理:
#   通过代码调用 webdriver 操作浏览器
#   不同的浏览器有不同的 driver

# ------------------------------------------------------------------------------------
# selenium 的使用
# --------------
# 1. 创建浏览器对象(xxx为浏览器名称，如Chrome)
# driver = webdriver.xxx(executable_path='./xxx')
# executable_path 参数可以指定浏览器驱动的路径，设置了环境变量的可省略

# 2. 发送请求
# driver.get(url)

# ----------------------------------------------

# driver 对象的常用属性和方法
# 1. driver.page_source     当前标签页渲染之后的网页源代码
# 2. driver.current_url     当前标签页的url
# 3. driver.close()         关闭当前标签页，如果只有一个标签页则关闭整个浏览器
# 4. driver.quit()          关闭浏览器
# 5. driver.forward()       页面前进
# 6. driver.back()          页面后退
# 7. driver.save_screenshot('图片.png')   页面截图

# ----------------------------------------------
# driver 标签元素定位的方法(xpath、css选择器这两种最常用)
# driver.find_element_by_xpath()
# driver.find_element_by_css_selector()

# driver.find_element_by_id()           # 通过 id 属性定位
# driver.find_element_by_class_name()   # 通过 classname 属性定位
# driver.find_element_by_name()         # 通过 name 属性定位
# driver.find_element_by_link_text()            # 通过超链接文本定位(如果不全名匹配，无法找到)
# driver.find_element_by_partial_link_text()    # 通过超链接文本的部分来定位(包含即可找到)
# driver.find_element_by_tag_name()     # 通过标签名定位，因为同名标签概率大，不推荐
# ------
# driver.find_element(by,value)     # 使用与上面同理，不过把by的方式以字符串写进了括号内
# ------
# find_element_* 和 find_elements_* 的区别
#   没s的返回一个对象(有多个的返回第一个),没有找到就会报错;
#   有s的返回一个列表,没有找到就返回一个空列表

# 定位到元素之后的方法
# element.clear                     对input元素已有的text进行清空，即初始化
# element.send_key(str)             在元素内输入字符串
# element.click()                   点击元素
# element.text                      获取标签对象的文本内容
# element.get_attribute('属性名')    通过属性名获取对象属性值
# ----------------------------------------------
# selenium 的其他使用方法
# -------------
# 窗口标签页的切换
#   获取所有标签页的窗口句柄(driver.window_handles返回一个句柄列表)
#   利用窗口句柄字切换到句柄指向的标签页
#   driver.switch_to.window(driver.window_handles[-1])
# -------------
# frame窗口切换
# iframe 是html中一种常用的技术，即在一个页面中嵌套了另一个网页，selenium默认是访问不了 frame 中的内容的，
# 需要通过 switch_to 切换到 frame 标签中
#   driver.switch_to.frame(iframe标签id属性)
#   driver.switch_to.frame(iframe标签对象)
# -------------
# selenium 对 cookies 的处理
# driver.get_cookies() 可返回一个列表，包含完整的cookie信息
# 也可以进行删除cookie操作
#     driver.delete_cookie(CookieName)
#     driver.delete_all_cookies()
# -------------
# selenium 控制浏览器执行 js 代码
#   driver.execute_script('scrollTo(x,y)')
#       滚动浏览器滚轮，x为水平移动，y为垂直移动
# -------------
# 页面等待
# 页面加载需要时间，避免元素还没加载出来就开始定位，需要进行页面等待
#   强制等待(了解即可)
#     time.sleep()
#   隐式等待
#     针对的是元素定位，设置时间内定位成功则停止等待，否则超时加载错误
#     driver.implicitly_wait(10)   # 隐式等待，最长等20秒
#   显式等待(了解即可)
#     明确等待某一个元素
#     略...
# -------------
# 配置 driver 对象
#   selenium开启无界面模式
#     绝大多数服务器是没有界面的，selenium控制的Chrome对象也是存在无界面模式的(即无头模式)
#     1. 实例化配置对象
#       options = webdriver.ChromeOptions()
#     2. 给配置对象添加开启无界面模式的命令
#       options.add_argument('--headless')
#     2. 给配置对象添加禁用gpu的命令
#       options.add_argument('--disable-gpu')
#     3. 实例化带有配置对象的driver对象
#       driver = webdriver.Chrome(chrome_options=options)

#  使用代理IP,因为设置代理在实例化driver对象之前，更换代理ip需要重新启动浏览器
#     给配置对象添加代理ip(其他步骤同上)
#     options.add_argument('--proxy-server=http://47.108.155.96:80')
#  修改user-agent(其他步骤同上)
#     options.add_argument('--user-agent=Mozilla/5.0 python')

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# 实战区↓
# ------------------------------------------------------------------------------------

# driver 常用属性方法

import time
from selenium import webdriver


# driver = webdriver.Chrome()
# driver.get('https://douban.com/movie')
# time.sleep(3)
# driver.get('http://www.baidu.com')

# print(driver.page_source)
# print(driver.current_url)
# driver.back()
# time.sleep(3)
# driver.forward()
# driver.save_screenshot('图片.png')
# time.sleep(3)
# driver.close()

# driver.get('https://baike.baidu.com/item/%E6%AD%BB%E5%BF%83%E7%9C%BC/2108219?fr=aladdin')
# print(driver.find_element('xpath','/html/body/div[3]/div[2]/div/div[1]/div[4]/div').text)
# driver.quit()

# ------------------------------------------------
# 元素定位

# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')

# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# driver.find_element_by_css_selector('#kw').send_keys('python')
# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_class_name('s_ipt').send_keys('python')
# driver.find_element_by_name('wd').send_keys('python')

# driver.find_element('id', 'kw').send_keys('python')
# driver.find_element_by_id('su').click()

# driver.find_element_by_link_text('hao123').click()
# driver.find_element_by_partial_link_text('hao').click()
# print(driver.find_element_by_tag_name('title'))

# time.sleep(3)
# driver.quit()

# ------------------------------------------------------------------------------------
# 其他使用方法的练习
# --------------------------
# 切换标签页

# driver = webdriver.Chrome()
# driver.get('https://www.douban.com/')
#
# driver.find_element_by_xpath('//ul/li[2]/a').click()
#
# current = driver.window_handles
# print(current)
#
# driver.switch_to.window(current[-1])
#
# print(driver.find_element_by_xpath('//table/tbody').text)
# driver.quit()
# --------------------------
# 切换到框架标签(qq空间、163邮箱)

# driver = webdriver.Chrome()

# # driver.get('https://i.qq.com/')
# driver.get('https://qzone.qq.com/')
# # ↓ 切换到 iframe 标签 ↓
# driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="login_frame"]'))
# driver.find_element_by_xpath('//*[@id="bottom_qlogin"]').click()
# driver.find_element_by_id('u').send_keys('QQ号')
# driver.find_element_by_id('p').send_keys('密码')
# driver.find_element_by_id('login_button').click()

# driver.get('https://mail.163.com/')
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]"))
# driver.find_element_by_xpath('//*[@name="email"]').send_keys('liaofaz@163.com')
# driver.find_element_by_xpath('//input[@name="password"]').send_keys(input('请输入邮箱密码:'))
# driver.find_element_by_xpath('//*[@id="dologin"]').click()

# --------------------------
# cookies 操作

# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
#
# cookie_list = driver.get_cookies()
# print(cookie_list)  # 获取标签页的cookies信息列表
# print('-'*100)
# cookies = {i['name']: i['value'] for i in cookie_list}
# print(cookies)      # 从列表中提取cookie字典
# driver.delete_all_cookies()
# print(driver.get_cookies())
#
# driver.quit()

# --------------------------
# 执行 js 代码

# driver = webdriver.Chrome()
#
# driver.get('https://lianjia.com/')

# 直接定位点击无法找到
# driver.find_element_by_xpath('/html/body/div[11]/div/div[1]/div[1]/ul/li[1]/a').click()

# driver.execute_script('scrollTo(0,document.body.scrollHeight)')
# driver.find_element_by_xpath('/html/body/div[11]/div/div[1]/div[1]/ul/li[1]/a').click()

# --------------------------
# 配置 driver 对象

# url = 'http://www.baidu.com'
# # url = 'http://www.whatismyip.com.tw/'

# options = webdriver.ChromeOptions()

# Chrome 无头模式
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# 使用代理IP,因为设置代理在实例化driver对象之前，更换代理ip需要重新启动浏览器
# options.add_argument('--proxy-server=http://47.108.155.96:80')
# 修改user-agent
# options.add_argument('--user-agent=Mozilla/5.0 python')

# driver = webdriver.Chrome(chrome_options=options)

# driver.get(url)
# print(driver.page_source)
# driver.quit()
