#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/9 15:39
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider.py
# @Software: PyCharm
import requests

HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'completeuinfo:2219444=%7B%22type%22%3A0%2C%22time%22%3A1518161888%7D; imooc_uuid=606cac48-e4ac-48c6-bf1e-8121eef6eb14; imooc_isnew_ct=1513840447; imooc_isnew=2; Hm_lvt_f0cfcccd7b1393990c78efdeebff3968=1516783726,1518161859; IMCDNS=0; loginstate=1; apsid=I3Y2RhZTYzNTBkOWRhNWY1Yjc5NTA0MjJjOWJlZWEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjIxOTQ0NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABmYW55dV93aEAxNjMuY29tAAAAAAAAAAAAAAAAAAAAADY3YzAxZDEwMjk5ZjY3NGRmMmQ3ZmUxN2E0ZTM3OTgxzk99Wm2zmVY%3DNj; last_login_username=fanyu_wh%40163.com; Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968=1518161881; Hm_lvt_76783e78c7e55cc7eae7861a979dd444=1518161894; Hm_lpvt_76783e78c7e55cc7eae7861a979dd444=1518161899; cvde=5a684862ec580-30',
    'Host': 'class.imooc.com',
    'Referer': 'https://class.imooc.com/sc/23',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# 目标网站url
url = 'https://class.imooc.com/sc/23/learn'


def get_home():
    response = requests.get(url, headers=HEADER)
    print(response.text)


if __name__ == '__main__':
    get_home()
