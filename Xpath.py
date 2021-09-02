# -*- codeing = utf-8 -*-

#  xpath用法

# nodename  选取次节点的所有子节点             div     选取div下的所有标签(子标签，不包括text()和孙标签)
#   //      从全局节点中选择节点，任意位置均可   //div   选取整个HTML页面的div标签
#   /       选取某个节点下的节点        //head/title  选取head标签下的title标签
#   /@       选取带某个属性的节点         //div[@id]   选择带有id属性的div标签
#  ./        当前节点下其他标签           ./span      选择当前节点下的所有span标签[.]
#  /..       当前节点的父节点
# /[n]                   第n个标签
# /[last()]              最后一个标签，[last()-1]表示倒数第二个标签
# /[position()<n]        前n-1个标签(也可以>取后面的)
#  /*                满足前面条件的所有标签
# /[@*]              选择所有拥有属性的某标签
# /node()            匹配任何类型的节点（文本、标签等等...）
#   |               或，只要满足得都取出来
# /@属性              把标签的属性取出来
# /following::*      该标签之后的所有标签
# /preceding::*      该标签之前的所有标签
# /following-sibling::*      该标签之后的所有同级（兄弟）标签
# /preceding-sibling::*      该标签之前的所有同级（兄弟）标签
# [contains()]         包含某个字符的节点，例如//div[contains(@class,“a”)]、//a[contains(text(),“百度搜索”)]



from lxml import etree

# 通过读取str字符串，生成html及etree
with open('job.html') as h:
    html = h.read()
html = etree.HTML(html)
# h1 = etree.tostring(html,encoding='utf-8').decode('utf-8')
# print(h1)


# 通过读取html文件，得到etree (不推荐)
# parser = etree.HTMLParser(encoding='gbk')         # 需要自定义解析器
# html_2 = etree.parse(r'job.html',parser = parser) # 然后用自定义解析器解析
# h2 = etree.tostring(html_2,encoding='gbk').decode('gbk')
# print(h2)

# --------------------------------------------------------------------------------------------------------


# 打印全部div标签
# divs = html.xpath('//div')
# print(divs)
# for div in divs:
#     d = etree.tostring(div,encoding='utf-8').decode('utf8')
#     print(d)
#     print('-'*100)
# -------------------------------------------------------------
# 打印某个标签（div）
# div_cn = html.xpath(r'//div[@class="cn"]')
# for div in div_cn:
#     d = etree.tostring(div,encoding='utf-8').decode('utf8')
#     print(d)
#     print('-'*100)
# -------------------------------------------------------------
# 打印某个标签的某个属性(id、href)
# div_id = html.xpath(r'//div/@id')
# print(div_id)
# a_href = html.xpath('//a/@href')
# print(a_href)
# -------------------------------------------------------------
# 取文本
# div_job = html.xpath('//div[@class="bmsg job_msg inbox"]/*/text()')
# print(div_job)
