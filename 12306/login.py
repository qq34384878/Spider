#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 17:24
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : login.py
# @Software: PyCharm
import requests
from cons import station


BASE_URL = 'http://www.12306.cn/'
CODE_URL = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.4814448843254753'
CHECK_URL = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
LOGIN_URL = 'https://kyfw.12306.cn/passport/web/login'

SESSION = requests.session()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
}

stationDict = {}
for i in station.split('@')[1:]:
    stationList = i.split('|')
    stationDict[stationList[1]] = stationList[2]

# 出发时间
train_date = '2018-1-17'
# 出发城市
fromStation = '武汉'
from_station = stationDict[fromStation]
# 到达城市
toStation = '成都'
to_station = stationDict[toStation]


def login():
    form = {
        'answer': '125,45',
        'login_site': 'E',
        'rand': 'sjrand',
    }
    resp = requests.get(BASE_URL, headers=HEADERS)
    print(resp.text)
    print(resp.history)


class Train(object):
    """
    """
    driver_name = ''
    executable_path = ''
    # 用户名,密码
    username = u''
    password = u''
    # cookie值
    starts = u''
    ends = u''
    # 时间格式2018-01-19
    dtime = u'2018-01-19'
    # 车次
    order = 0
    # 乘客名
    users = [u'', u'']
    # 席位
    xb = u'二等座'
    pz = u'成人票'

    def __init__(self):
        self.driver_name = 'chrome'
        self.executable_path = 'C:\Program Files (x86)\Google\Chrome\Application'

    def login(self):
        pass
