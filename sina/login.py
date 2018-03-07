#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 16:42
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : login.py
# @Software: PyCharm
import requests


class Userlogin:
    def userlogin(self, username, password, pagecount):
        session = requests.Session()
        url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.5)&_=1364875106625'
        url_login = ''