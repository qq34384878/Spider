#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 16:50
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : sinam.py
# @Software: PyCharm
import requests

BASE_URL = 'http://m.weibo.com/'
LOGIN_URL = 'https://passport.weibo.cn/sso/login'
SESSION = requests.session()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'}

# 确定重定向


def get_m_login():
    resp = requests.get(BASE_URL, headers=HEADERS)
    print(resp.text)
    print(resp.history)


#
def login_weibo(username, password):
    form = {
        'username': username,
        'password': password,
        'savestate': 1,
        'r': 'http://m.weibo.cn/',
        'ec': 0,
        'pagerefer': 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F',
        'entry': 'mweibo',
        'wentry': '',
        'loginfrom': '',
        'client_id': '',
        'code': '',
        'qq': '',
        'mainpageflag': 1,
        'hff': '',
        'hfp': '',
    }
    resp = SESSION.post(url=LOGIN_URL, data=form, headers=HEADERS)
    if resp.status_code == 200:
        print(resp.json())


if __name__ == '__main__':
    # get_m_login()
    login_weibo('18120440747','qqfy.326498')