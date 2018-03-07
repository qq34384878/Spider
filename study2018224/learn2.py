#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 15:16
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : learn2.py
# @Software: PyCharm

import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
}
proxy = {'http': '121.61.2.135:8888'}
response = requests.get(url="http://www.mzitu.com/", headers=headers)
print(response.content)