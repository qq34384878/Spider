# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Leo'
import urllib2
import urllib
import ssl
import cookielib
from user import user, pwd
from codes import codes
from json import loads
from cons import station
from time import sleep
import re

stationDict = {}
for i in station.split('@')[1:]:
    stationList = i.split('|')
    stationDict[stationList[1]] = stationList[2]

# print stationDict

c = cookielib.LWPCookieJar()  # 生成一个存储cookie的对象
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)  # 把这个村粗器绑定到opener对象当中
urllib2.install_opener(opener)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
}

ssl._create_default_https_context = ssl._create_unverified_context

# 出发时间
train_date = '2018-1-1'
# 出发城市
fromStation = '武汉'
from_station = stationDict[fromStation]
# 到达城市
toStation = '成都'
to_station = stationDict[toStation]


def login():
    print '正在获取验证码'
    req = urllib2.Request(
        'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.623924012750033')
    req.headers = headers
    imgCode = opener.open(req).read()
    with open('code.png', 'wb') as fn:
        fn.write(imgCode)

    req = urllib2.Request(
        'https://kyfw.12306.cn/passport/captcha/captcha-check')
    req.headers = headers
    #code = raw_input('请输入验证码:')
    print '正在识别验证码'
    code = codes('code.png', 287)
    print code
    data = {
        'answer': code,
        'login_site': 'E',
        'rand': 'sjrand'
    }
    data = urllib.urlencode(data)
    html = opener.open(req, data).read()
    req = urllib2.Request('https://kyfw.12306.cn/passport/web/login')
    req.headers = headers
    data = {
        'username': user,
        'password': pwd,
        'appid': 'otn'
    }
    data = urllib.urlencode(data)
    print '正在登录'
    html = opener.open(req, data).read()
    result = loads(html)
    if result['result_code'] == 0:
        print '登录成功'
        req = urllib2.Request('https://kyfw.12306.cn/otn/login/userLogin')
        req.headers = headers
        data = {
            '_json_att': ''
        }
        data = urllib.urlencode(data)
        html = opener.open(req, data=data)
        req = urllib2.Request(
            'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin')
        req.headers = headers
        html = opener.open(req)
        print html.geturl()
        req = urllib2.Request('https://kyfw.12306.cn/passport/web/auth/uamtk')
        req.headers = headers
        data = {
            'appid': 'otn'
        }
        data = urllib.urlencode(data)
        html = opener.open(req, data=data).read()
        print html
        result = loads(html)
        tk = result['newapptk']
        req = urllib2.Request('https://kyfw.12306.cn/otn/uamauthclient')
        req.headers = headers
        data = {
            'tk': tk
        }
        data = urllib.urlencode(data)
        html = opener.open(req, data=data).read()
        print html
        req = urllib2.Request('https://kyfw.12306.cn/otn/index/initMy12306')
        req.headers = headers
        html = opener.open(req).read()
        print html
        return True
    print '登录失败，正在重新登录'
    sleep(5)
    login()


login()


def check():
    req = urllib2.Request(
        'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %
        (train_date, from_station, to_station))
    req.headers = headers
    html = opener.open(req).read()
    reslut = loads(html)
    return reslut['data']['result']


index = 0
'''
[3] = 车次
[8] = 出发时间
[9] = 到达时间
[10] = 历时
[23] = 软卧
[28] = 硬卧
'''
for i in check():
    tmpList = i.split('|')
    # print tmpList
    # for n in tmpList:
    #     print index,n
    #     index += 1
    try:
        if tmpList[23] == u'有' or int(tmpList[23]) > 0:  # -- 无
            print u'''
            该车次有票：
            车次:%s
            出发时间:%s
            到达时间:%s
            历时:%s
            余票:%s
            ''' % (tmpList[3], tmpList[8], tmpList[9], tmpList[10], tmpList[23])
            break

    except BaseException:
        continue

# 下单


def buyTickets():
    req = urllib2.Request('https://kyfw.12306.cn/otn/index/initMy12306')
    req.headers = headers
    html = opener.open(req).read()
    # 第一个请求
    # for i in c:
    #     print i
    req = urllib2.Request('https://kyfw.12306.cn/otn/login/checkUser')
    req.headers = headers
    data = {
        '_json_att': ''
    }
    data = urllib.urlencode(data)
    html = opener.open(req, data=data).read()
    # print 10001,html
    # 第二个请求

    req = urllib2.Request(
        'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest')
    req.headers = headers
    print tmpList
    print train_date
    data = {
        'secretStr': urllib.unquote(tmpList[0]),
        'train_date': train_date,
        'back_train_date': '2018-1-2',
        'tour_flag': 'dc',
        'purpose_codes': 'ADULT',
        'query_from_station_name': fromStation,
        'query_to_station_name': toStation,
        'undefined': '',
    }
    data = urllib.urlencode(data)
    html = opener.open(req, data=data).read()
    # data   a=1&b=2&c=3  查询字符串
    print 10002, html
    # 第三个请求
    req = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/initDc')
    req.headers = headers
    data = {
        '_json_att': ''
    }
    data = urllib.urlencode(data)
    html = opener.open(req, data).read()
    print html
    globalRepeatSubmitToken = re.findall(
        r"globalRepeatSubmitToken = '(.*?)'", html)[0]
    key_check_isChange = re.findall(r"'key_check_isChange':'(.*?)'", html)[0]
    print 10003, globalRepeatSubmitToken
    # 第四个请求
    req = urllib2.Request(
        'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs')
    req.headers = headers
    data = {
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': globalRepeatSubmitToken
    }
    data = urllib.urlencode(data)
    html = opener.open(req, data).read()
    print 10004, html
    req = urllib2.Request(
        'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo')
    req.headers = headers
    data = {
        'cancel_flag': '2',
        'bed_level_order_num': '000000000000000000000000000000',
        'passengerTicketStr': '3,0,1,方煜,1,510321199004116190,18173119351,N',
        'oldPassengerStr': '方煜,1,510321199004116190,1_',
        'tour_flag': 'dc',
        'randCode': '',
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': globalRepeatSubmitToken,
    }
    print data
    data = urllib.urlencode(data)
    # for i in c:
    #     print i
    html = opener.open(req, data).read()
    print 10005, html
    req = urllib2.Request(
        'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingle')
    req.headers = headers
    data = {
        'passengerTicketStr': '3,0,1,方煜,1,510321199004116190,18173119351,N',
        'oldPassengerStr': '方煜,1,510321199004116190,1_',
        'tour_flag': 'dc',
        'randCode': '',
        'purpose_codes': '00',
        'key_check_isChange': key_check_isChange,
        'train_location': 'Q9',
        'choose_seats': '',
        'seatDetailType': '000',
        'roomType': '00',
        'dwAll': 'N',
        '_json_att': '',
        'REPEAT_SUBMIT_TOKEN': globalRepeatSubmitToken,
    }
    data = urllib.urlencode(data)
    html = opener.open(req, data).read()
    print html


buyTickets()
