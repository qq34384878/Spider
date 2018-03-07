#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 14:34
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : bilibili.py
# @Software: PyCharm


import requests
import time
import random


class SendLiveRoll():

    def __init__(self, roomid):

        # 直播的房间号
        self.roomid = str(roomid)

        # 该网址用于获取数据
        self.url_1 = 'https://api.live.bilibili.com/ajax/msg'

        # 用于发弹幕的地址
        self.url_2 = 'https://api.live.bilibili.com/msg/send'

        # 模拟浏览器
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

        # 账号信息
        self.cookie = {'Cookie': 'l=v; fts=150'}

        # 直播间信息
        self.form_1 = {
            'csrf_token': '',
            'roomid': self.roomid,
            'token': ''
        }

        self.timestamp = str(int(time.time()))

    def DanMuSend(self):
        while True:
            # 请求弹幕信息, 服务器会返回弹幕
            html_1 = requests.post(
                self.url_1,
                data=self.form_1,
                headers=self.header)

            # 提取弹幕信息, 每个text_1里面有10条弹幕
            text_1 = list(map(lambda ii: html_1.json()[
                          'data']['room'][ii]['text'], range(10)))

            # 复制别人的弹幕, 一般复制最后几个, 目的是避免重复, 采用随机方式
            message = text_1[random.randint(7, 9)]
            print(message)

            # 需要提交的数据, 提交给服务器
            form_2 = {
                'color': '16777215',    # 颜色可以改变
                'fontsize': '25',
                'mode': '1',
                'msg': message,
                'rnd': self.timestamp,  # 每次刷新网页的时间/可以不变
                'roomid': self.roomid,  # 改变roomid可以改变不同主播的房间
            }

            # 发射弹幕post方法
            requests.post(
                self.url_2,
                data=form_2,
                headers=self.header,
                cookies=self.cookie)

            # 弹幕每隔5秒才能继续, bilibili规定
            time.sleep(random.randint(6, 10))
