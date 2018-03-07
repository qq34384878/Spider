#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 14:56
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : send_danmu.py
# @Software: PyCharm


import requests
import time
import random
import configparser

# 读取文件的对象
target = configparser.ConfigParser()

# 读取文件
target.read(r'C:\Users\double\PycharmProjects\Spider\chushou\sgg.ini', encoding='utf-8')

# target.sections() # 返回ini里面[]里面的东西

# post的地址
url = 'https://api.live.bilibili.com/msg/send'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

cookie = {
    # 'Cookie': 'fts=1509871117; sid=lby2w6id; buvid3=57853144-D300-4F7A-8BDB-E37E61BE830344992infoc; LIVE_BUVID=4202770db9e6733776d8817ff4fe6ff1;'
    # 'Cookie': 'l=v; LIVE_BUVID=4202770db9e6733776d8817ff4fe6ff1; LIVE_BUVID__ckMd5=e779acfbfb82c3a0; sid=cr01r137; buvid3=57853144-D300-4F7A-8BDB-E37E61BE830344992infoc; finger=edc6ecda; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516950833; DedeUserID=22636113; DedeUserID__ckMd5=9e9940c499d60dc4; SESSDATA=2494bdc2%2C1519542851%2C85ae6ac7; bili_jct=f975ea10fdfcb7ca1e8233d05e5ddcd9; _dfcaptcha=732cfeaed6ec746fd78a526611ddb8be; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516950895'
    'Cookie': 'l=v; LIVE_BUVID=4202770db9e6733776d8817ff4fe6ff1; LIVE_BUVID__ckMd5=e779acfbfb82c3a0; sid=cr01r137; buvid3=57853144-D300-4F7A-8BDB-E37E61BE830344992infoc; finger=edc6ecda; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516950833; DedeUserID=22636113; DedeUserID__ckMd5=9e9940c499d60dc4; SESSDATA=2494bdc2%2C1519542851%2C85ae6ac7; bili_jct=f975ea10fdfcb7ca1e8233d05e5ddcd9; purl_token=bilibili_1516952276; UM_distinctid=1613167034dcd-00312a6906c5f1-393d5f0e-1fa400-1613167034e1c5; fts=1516952290; pgv_pvi=8584450048; pgv_si=s9778998272; _dfcaptcha=7a21f23fb1d3d2463df2ede73b424db3; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516955945'
}

while True:

    # 提取弹幕以及弹幕颜色
    message = target['我的弹幕'][str(random.randint(1, 8))] # 1<=n<=8
    # color = target['弹幕颜色'][str(random.randint(1, 8))] # 1<=n<=7

    # 需要提交的数据
    form = {
        'color': '16777215',    # 颜色可以改变
        'fontsize': '25',
        'mode': 1,
        'msg': message,
        'rnd': str(int(time.time())),
        'roomid': '5096'    # 改变roomid可以改变不同主播的房间
    }

    response = requests.post(url=url, data=form, headers=header, cookies=cookie)
    if response.status_code == 200:
        print('弹幕发送成功', message)
        print(response.json())
    time.sleep(5.5)


