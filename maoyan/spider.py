#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/10 17:02
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider.py
# @Software: PyCharm

import requests
import time

HEADER = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Host': 'box.maoyan.com',
    'Origin': 'http://piaofang.maoyan.com',
    'Referer': 'http://piaofang.maoyan.com/dashboard',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0'
}


def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)


def get_maoyan_monitor():
    response = requests.get(
        url='https://box.maoyan.com/promovie/api/box/second.json',
        headers=HEADER)
    if response.status_code == 200:
        print(response.json())
        time.sleep(4)
    else:
        print('爬取失败')


if __name__ == '__main__':
    main()
