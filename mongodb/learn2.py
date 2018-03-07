#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 10:50
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : learn2.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
from lxml import etree

Headers = {
    # 'Referer': 'http://bj.xiaozhu.com/',
    'User-Agent': 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
}

url = 'http://bj.xiaozhu.com/'
Seesion = requests.session()

response = Seesion.get(url, headers=Headers)
print(response.content)
with open('response.txt', 'w') as f:
    f.write(response.text)
soup = BeautifulSoup(response.content, 'lxml')
# selector = etree.HTML(response.content)
titles = soup.select('span.result_title.hiddenTxt')
prices = soup.select('span.result_price > i')
print(titles)
print(prices)
