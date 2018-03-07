#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 10:35
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : HSSpider.py
# @Software: PyCharm
import csv
import time

import requests

URL = 'http://hs.blizzard.cn/action/cards/query'

now = time.time()
FORM_DATA = {
    'cardClass': 'druid',
    'p': 2,
    'standard': 1,
    'keywords': '',
    't': now,
}


def Spider(url):
    print('start')
    card_data = requests.post(url=url, data=FORM_DATA)
    print(card_data.json())
    return card_data.json()


def parse_data(json_data):
    if json_data:
        cards = json_data.get('cards')
        print(cards)
        for card_info in cards:
            print(card_info.keys())
            # dict = None
            list = None
            for key in card_info.keys():
                dict = card_info[key]
                print(dict)
                print(type(dict))
                if dict != None:
                    list.append(dict)
            out = open('22.csv', 'a', newline='')
            csv_write = csv.writer(out, dialect='excel')
            csv_write.writerow(list)
        print('write over')


if __name__ == '__main__':
    data = Spider(url=URL)
    parse_data(data)
