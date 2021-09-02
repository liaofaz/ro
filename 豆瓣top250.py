# -*-  codeing = utf-8 -*-
# @Time : 2021/3/30 下午 5:02
# @Author : 漫天烟华
# @File : 豆瓣top250.py
# @Software : PyCharm


#import bs4     #网页解析，获取数据
from bs4 import BeautifulSoup
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error   #制定URL，获取网页数据
import xlwt     #进行Excel操作
import sqlite3  #进行SQLite数据库操作



def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    savepathDB = "movie250.db"

    # 3.保存数据
    saveData(datalist,savepath)
    saveDB(datalist,savepathDB)

# 名字
find_name = re.compile(r'<span class="title">(.*?)</span>')
# 其他名字
find_othername = re.compile('<span class="other">(.*?)</span>')
# 图片
find_img = re.compile(r'<img alt=".*?src="(.*?)" width="100"/>',re.S)
# 链接
find_link = re.compile(r'<a href="(.*?)">',re.S)
# 评分
find_ratingnum = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 评价数
find_evaluate = re.compile(r'<span>(.*?)人评价</span>')
# 概况
find_gaikuo = re.compile(r'<span class="inq">(.*?)</span>')
# 详情
find_details = re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):         # 循环十次
        url = baseurl + str(i*25)
        html = askURL(url)        # 保存获取到的网页源码

        #2.解析数据
        bs = BeautifulSoup(html, 'html.parser')
        for item in bs.find_all('div',class_="item"):
            # print(item)        # 全部item信息
            data = []
            item = str(item)                        # 注意：re.findall的参数2必须是字符串或字节！！
            name = re.findall(find_name,item)
            name1 = name[0]
            data.append(name1)                      #中文名
            if len(name) == 2:
                name2 = name[1].replace("\xa0/\xa0","")
            else:
                name2 = ""
            data.append(name2)                      #外文名
            othername = re.findall(find_othername,item)[0].replace("\xa0/\xa0","")
            data.append(othername)                  #其他名字
            img = re.findall(find_img, item)[0]
            data.append(img)                        # 图片
            link = re.findall(find_link,item)[0]
            data.append(link)                       #网址
            ratingnum = re.findall(find_ratingnum,item)[0]
            data.append(ratingnum)                  #评分
            evaluate = re.findall(find_evaluate,item)[0]
            data.append(evaluate)                   #评价数
            gaikuo = re.findall(find_gaikuo,item)
            if len(gaikuo) == 0:
                data.append("")
            else:
                gaikuo = gaikuo[0].replace("。","")
                data.append(gaikuo)                 #概况
            details = re.findall(find_details,item)[0]
            details = re.sub('[(\xa0\xa0\xa0)(\xa0/\xa0)(<br>\n)]',"",details)
            data.append(details.strip())            #详情
            datalist.append(data)
    # for i in datalist:
    #     print(i)
    return datalist

# 得到一个指定的URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 88.0.4324.182 Safari / 537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#保存数据
def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8")  # 创建文件
    worksheet = workbook.add_sheet("豆瓣电影top250")  # 创建工作表

    col = ['中文名','外文名','又名','图片','网址','评分','评价数','概况','信息']
    print("开始并保存爬取数据,进度：")
    for i in range(0,9):
        worksheet.write(0,i,col[i])
    for a in range(0,250):
        print("%d/250"%(a+1))
        write = datalist[a]
        for b in range(0,9):
            worksheet.write(a+1,b,write[b])
    workbook.save(savepath)


def foundDB(savepathDB):
    conn = sqlite3.connect(savepathDB)
    cur = conn.cursor()
    sql = '''
        create table movie250(
        id integer primary key autoincrement,
        cname varchar,
        ename varchar,
        oname varchar,
        pic_link text,
        info_link text,
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )
    '''
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("数据表新建成功！")



def saveDB(datalist,savepathDB):
    foundDB(savepathDB)
    conn = sqlite3.connect(savepathDB)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 5 or index == 6:
                continue
            data[index] = '"' + data[index] + '"'
        sql = 'insert into movie250(cname,ename,oname,pic_link,info_link,score,rated,instroduction,info)\
        values(%s)'%",".join(data)        #str.join() 把列表元素取出来以str连接成新字符串
        # print(sql)
        cur.execute(sql)
        conn.commit()
    conn.close()
    print("数据库已保存！")


#程序执行位置
if __name__ == '__main__':#当程序任务在当前文件运行时会被执行，被其他文件以模块形式import引入时不会执行
    main()