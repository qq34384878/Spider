#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/25 17:38
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider.py
# @Software: PyCharm

# 设置列表页URL的固定部分
import pandas as pd
import requests
import time

from bs4 import BeautifulSoup

url = 'http://wh.lianjia.com/ershoufang/'
# 设置页面页的可变部分
page = ('pg')
# 设置请求头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip',
    'Connection': 'close',
    'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
}

# 循环抓取列表页信息
for i in range(1, 100):
    if i == 1:
        i = str(i)
        a = (url+page+i+'/')
        r = requests.get(url=a, headers=headers)
        html = r.content
    else:
        i = str(i)
        a = (url+page+i+'/')
        r = requests.get(url=a, headers=headers)
        html2 = r.content
        html = html + html2
    # 每次间隔0.5秒
    time.sleep(0.5)


# 解析抓取的页面内容
lj = BeautifulSoup(html, 'html.parser')

# 提取房源总价
price = lj.find_all('div', attrs={'class': 'priceInFo'})
tp = []
for a in price:
    totalPrice = a.span.string
    tp.append(totalPrice)

# 提取房源信息
houseInfo = lj.find_all('div', attrs={'class': 'houseInfo'})
hi = []
for b in houseInfo:
    house = b.get_text()
    hi.append(house)

# 提取房源关注度
followInfo = lj.find_all('div', attrs={'class': 'followInfo'})
fi = []
for c in followInfo:
    follow = c.get_text()
    fi.append(follow)

# 创建数据表
house=pd.DataFrame({'totalprice':tp,'houseinfo':hi,'followinfo':fi})

# 查看数据表的内容
house.head()