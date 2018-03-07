#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 12:13
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : login.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://github.com/login'
LOGIN_URL = 'https://github.com/session'
SESSION = requests.session()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
}


def get_authenticity_token():
    response = SESSION.get(BASE_URL, headers=HEADERS)
    if response.status_code != 200:
        # 也许你的IP被拒绝或你的网络不正常
        raise Exception('Maybe your ip is denied or your network is unnormal')
    soup = BeautifulSoup(response.text)
    token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
    return token


def login(username, password, token):
    form = {
        'login': username,
        'password': password,
        'commit': 'Sign in',
        'authenticity_token': token,
        'utf8': '%E2%9C%93'
    }

    SESSION.post(url=LOGIN_URL, data=form, headers=HEADERS)


if __name__ == '__main__':
    check_url = 'https://github.com/'
    login_name = 'qq34384878'
    login_pass = 'qqfy19941027'
    authenticity_token = get_authenticity_token()
    login(login_name, login_pass, authenticity_token)
    resp = SESSION.get(check_url, headers=HEADERS)
    # 如果Sign out在返回的text中,则登录失败，请检查
    assert 'Sign out' in resp.text, "login failed, please check your name and password"
    print('login succeeded')
