# -*- codeing = utf-8 -*-
# @Time:    2021/8/29 上午 8:07
# @Author:  漫天烟华
# @Software: PyCharm
# @Version:  Python 3.9.4


# 分布式
# 不同的节点(服务器、ip)共同完成一个任务

# scrapy_redis
# scrapy框架基于redis的分布式组件
# 通过持久化的请求队列和请求的指纹集合实现
#   断点续爬
#   分布式快速抓取

# git clone http://github.com/rolando/scrapy-redis.git

# 报错: redis.exceptions.ResponseError: DENIED Redis is running(处理方法如下)
# 取消保护模式，在CMD的redis-cli后执行    config set protected-mode “no”

# 以下设置未知效果...先记下来(把set改成get并且去掉no即可查询状态)
# 在配置文件redis.windows.conf中的 bind 127.0.0.1 前面加#注释掉
# Redis默认不是以守护进程的方式运行，可以通过该配置项修改，使用yes启用守护进程，设置为no
#   config set daemonize no
