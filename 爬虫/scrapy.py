# -*- codeing = utf-8 -*-
# @Time : 2021/7/26 下午 8:54
# @Author : 漫天烟华
# @File : scrapy.py
# @Software : PyCharm


# scrapy 是一个Python编写的开源网络爬虫框架，它是一个被设计用于爬取网络数据、提取结构性的框架
#   Scrapy 使用了Twisted['twɪstɪd]异步网络框架，可以加快下载速度
#   作用: 少量的代码，就能够完成快速的抓取


# scrapy 的工作流程（spiders爬虫、引擎、调度器、下载器、管道）
#   1. 爬虫 根据其实url构造(实例化)request对象 --> 爬虫中间件 --> 引擎 --> 调度器
#   2. 调度器根据队列传递request --> 引擎 --> 下载中间件 --> 下载器
#   3. 下载器发送请求获取响应 --> 下载中间件 --> 引擎 --> 爬虫中间件 --> 爬虫
#   4. 爬虫提取新url，构造请求对象 --> 爬虫中间件 --> 引擎 --> 调度器（回到步骤2）
#   5. 爬虫提取数据 --> 引擎 --> 管道处理和保存数据

# scrapy的三个内置对象
# request  请求对象: 由url method post_data headers等构成
# response 响应对象: 由url body status headers等构成
# item 数据对象: 本质上是个字典

# scrapy 开发(编写)流程
#   1. 创建项目
#     scrapy startproject mySpider(项目名字)
#     在items.py文件中进行建模(字段非常少就可省略)
#       1）在items
#   2. 生成一个爬虫
#     scrapy genspider example example.cn
#   3. 提取数据
#     根据网络结构在spider中实现采集相关内容
#     从spiders文件夹中找到对应的爬虫文件，完善爬虫
#       1）修改起始的url
#       2）检查修改允许的域名allowed_domains
#       3）在parse方法中实现爬取逻辑
#   4. 保存数据
#     使用pipelines进行数据后续处理和保存#     在pipelines.py文件中写入对数据的操作代码
#       1）定义管道类
#       2）重写管道类的process_item方法
#       3）process_item方法处理完数据后必须把item返回给引擎
#     在settings.py文件中配置启动管道
#       ITEM_PIPELINES = {
#           'myscrapy.pipelines.MyscrapyPipeline': 299,
#           'myscrapy.pipelines.MyscrapyPipeline2': 300,
#       }
#       键: 管道类路径(用.连接)，第一个是项目目录，第二个是设置文件，第三个是定义的管道类
#       值: 管道的使用顺序，数值越小越优先执行，一般设置在1000以内
#   5. 运行爬虫(在终端的项目路径下)
#     scrapy crawl spider(爬虫名，免后缀)


# 爬虫文件的三个参数
#   name
#   allowed_domains
#   start_urls          设置初始url
# ------------
# 爬虫文件的parse方法
# parse()推荐使用yield返回数据. 解析函数yield能够传递的对象只能是BaseItem,Request,dict,None
#   解析起始url的方法
#   response响应对象的常用属性
#     response.url              当前响应的url地址
#     response.request.url      当前响应对应的请求的url地址
#     response.headers          响应头
#     response.request.headers 当前响应的请求头
#     response.body             响应体，也就是html代码，byte类型
#     response.status           响应状态码


# scrapy.Requests的参数
# scrapy.Requests(url[, callbacks, method='GET', headers, body, cookies, meta, dont_filter=False])
#   callback    表示当前的url的响应交给哪个函数去处理
#   meta    实现数据在不同的解析函数中传递，meta默认带有部分数据，比如下载延迟、请求深度等
#   dont_filter 默认为False，会过滤请求的url地址，即请求过的url地址不会继续被请求，对需要重复请求的url地址
#               可以把它设置为True，比如贴吧的翻页请求，页面的数据总是在变化；start_urls中的地址会被重复请求，
#               否则程序不会启动
#   method  指定POST或者GET请求
#   headers 接受一个字典，其中不包括cookies
#   cookies 接受一个字典，专门放置cookies
#   body    接受一个json字符串，为POST的数据，发送payload_post请求时使用


# scrapy 模拟登陆
# 1.携带cookies直接访问获取需要登陆后的页面
#   cookies过期时间过长，常见于一些不规范的网站
#   能在cookies过期之前把所有的数据拿到
#   配合其他程序使用，比如先使用selenium拿到登陆后的cookies存入本地，scrapy访问前先读取本地cookies
# 2.scrapy 发送post请求
# 虽然可以用scrapy.Request()指定method、body参数来发送post请求
# 通常更推荐使用scrapy.FormRequest()来发送post请求
#   scrapy.FormRequest()能够发送表单和ajax请求
#   在settings.py中通过设置COOKIES_DEBUG=TRUE运行爬虫时可以在终端看到cookie的传递过程


# scrapy 管道使用
#   process_item(self, item, spider) 实现对item数据的处理
# ----------------------------
#   open_spider(self, spider)     能够在爬虫开启时执行一次
#   close_spider(self, spider)    能够在爬虫关闭时执行一次
#   类似于__init__和__del__ 但因为有参数spider，可以通过spider.name过滤爬虫
#   也用于爬虫和数据库的交互，爬虫开启时建立连接，爬虫关闭时断开连接


# crawlspider
# 自动根据规则提取链接并且发送引擎
# 创建crawlspider爬虫
#   scrapy genspider -t crawl name(爬虫名字) example.cn(域名)


# scrapy 中间件
# 根据位置分为
#   下载器中间件
#   爬虫中间件
# 作用
#   对header以及cookie进行更换和处理
#   使用代理ip
#   对请求进行定制化操作
# 两种默认都在middlewares.py文件中，通常只编写下载器中间件
# ------------------
# 中间件使用方法
# 1.在middlewares.py中定义中间件类
# 2.在中间件类中，重写处理请求或者响应的方法
# process_request(self, request, spider)
#   当request通过下载器中间件时，该方法被调用
#   None    将request传递给其他权重低的process_response方法，全为None则交给下载器
#   request 通过引擎把request对象交给调度器，不通过其他process_response方法
#   response交给爬虫
# process_response(self, request, response, spider)
#   当下载器完成http请求，传递响应给引擎时调用
#   request 通过引擎交给调度器继续请求，不通过其他process_response方法
#   response通过引擎交给爬虫或者其他权重低的process_response处理
# 3.在settings.py文件中开启中间件的使用(与管道开启类似)
