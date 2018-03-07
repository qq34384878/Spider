#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/27 14:40
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider.py
# @Software: PyCharm
import requests


def get_cards_info():
    url = 'http://www.iyingdi.cn/web/tools/hearthstone/cards'
    post_url = 'http://www.iyingdi.cn/hearthstone/card/search/vertical'

    params = {
        'ignoreHero': 1,
        'statistic': 'total',
        'order': '',
        'token': '',
        'page': 0,
        'size': 1000,
    }
    response = requests.post(url=post_url, params=params)
    print(response.text)


if __name__ == '__main__':
    get_cards_info()