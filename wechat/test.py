#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 10:54
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : test.py
# @Software: PyCharm
import requests

proxy_url = 'http://127.0.0.1:8088/random'

def get_proxy():
    response = requests.get(url=proxy_url, timeout=3)
    if response.status_code == 200:
        print(response.text)

get_proxy()