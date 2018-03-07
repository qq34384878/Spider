#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 16:29
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : demo1.py
# @Software: PyCharm
import re

import requests

url = 'https://chat.chushou.tv/chat/send.htm'
cs_url = 'http://httpbin.org/post'
login_url = 'https://github.com/login'
user = 'qq34384878'
password = 'qqfy19941027'
user_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'}


def github_login():
    session = requests.Session()
    response = session.get(login_url, headers=user_headers)
    print(response.content)
    str = bytes.decode(response.content)
    print(type(response.content))
    pattern = re.compile(
        r'<input name="authenticity_token" type="hidden" value="(.*)" />')

    authenticity_token = pattern.findall(str)

    login_data = {
        'commit': 'Sign in',
        'utf8': '%E2%9C%93',
        'authenticity_token': 'QD7Ii/voQA4irlDK6QLPpLf+XP9VHOTn0r52LCdnFNHNubarvuZyFDL3+A4cg+X7JXqkA7YZo340eLEPogfoOg==',
        'login': user,
        'password': password}

    session_url = 'https://github.com/session'

    response = requests.post(
        url=session_url,
        data=login_data,
        headers=user_headers)
    print(response.status_code)
    print(response.url)
    if response.status_code == 302:
        print('login success')


def post():
    # res = requests.post(url=url, )
    my_data = {
        'key1': 'value1',
        'key2': 'value2'
    }
    r = requests.post(url=cs_url, data=my_data)
    print(r.content)

# 用Requests下载并保存一张图片


def get_content():
    jpg_url = 'http://img2.niutuku.com/1312/0804/0804-niutuku.com-27840.jpg'

    content = requests.get(jpg_url).content

    with open('test.jpg', 'wb') as fp:
        fp.write(content)


if __name__ == '__main__':
    # github_login()
    get_content()
