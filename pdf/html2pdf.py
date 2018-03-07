#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 10:41
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : html2pdf.py
# @Software: PyCharm

import pdfkit
import os

import time
from lxml import etree
from bs4 import BeautifulSoup

import requests

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

home_url = 'https://germey.gitbooks.io/python3webspider/content/'

options = {
    'page-size': 'Letter',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ]
}

header = {
    "accept-Encoding": "gzip, deflate, br",
    "accept-Language": "zh-CN,zh;q=0.9",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "cache-control": "max-age=0",
    "Connection": "keep-alive",
    "cookie": "_ga=GA1.2.1158381078.1517970329; _gid=GA1.2.821648601.1517970329; gitbook:sess=eyJ2YXJpYW50IjowLCJhbm9ueW1vdXNJZCI6ImEyNDAwOTFiLTZlMmMtNGJiYy1iMjMxLTc5NDJmNmYxNTRlMyJ9; gitbook:sess.sig=UhnPH1-RKDjoykqnOdeTrsyvNic",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}


def get_content_url():
    response = requests.get(url=home_url, headers=header)
    print(response.content)
    url_list = []
    if response.status_code == 200:
        xml = etree.HTML(response.content)
        print(response.text)
        # 取章节title name
        name_list = xml.xpath('//li[@class="chapter "]/a/text()')
        print(type(name_list))
        for name in name_list:
            name = str(name)
            name = name.strip()
            print(name)
        print(len(name_list))
        data_path = xml.xpath('//li/a/@href')
        print(data_path)
        main_url = data_path.pop(0)
        print(main_url)
        print(len(data_path))
        del data_path[0]
        print(len(data_path))
        for url in data_path:
            url = str(url)
            if url == 'VIP.html':
                break
            url = home_url + url
            print(url)
            get_url_info(url)
            time.sleep(1)

        # url = home_url +


def get_url_info(url):
    response = requests.get(url=url, headers=header)
    # print(response.content)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    # content = soup.find_all(class_="search-noresults")[0]
    print(soup)


def html2pdt_test():
    pdfkit.from_file(
        'demo.html',
        'demo.pdf')
    print("ok")


# url = 'https://germey.gitbooks.io/python3webspider/content/0-%E7%9B%AE%E5%BD%95.html'
if __name__ == '__main__':
    # html2pdt_test()
    get_content_url()
