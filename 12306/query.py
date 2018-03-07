#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 10:06
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : query.py
# @Software: PyCharm
import requests

URL = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
train_date = '2018-01-18'
from_station = 'WHN'
to_station = 'CDW'
QUERY_DATA = {
    'leftTicketDTO.train_date': train_date,
    'leftTicketDTO.from_station': from_station,
    'leftTicketDTO.to_station': to_station,
    'purpose_codes': 'ADULT',
}


def query():
    resp = requests.get(URL, params=QUERY_DATA)
    print(resp.json())
    result = resp.json().get('data').get('result')
    print(result)


if __name__ == '__main__':
    # query()
    # u = u'中文'
    # print(type(u))
    # str = u.encode('gbk')
    # print(type(u))
    # str1 = str.decode('gb2312')
    # print(type(u))

    resp = requests.post(url='https://candy.one/check_msg', params={'phone':1233})