#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/6 10:50
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : login2.py
# @Software: PyCharm

import requests
import base64
import re
import urllib
import urllib.parse
import rsa
import json
import binascii
from bs4 import BeautifulSoup



def userlogin(username, password):
    session = requests.Session()
    url_prelogin = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=NDU1NQ%3D%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_=1517885837362'
    url_login = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'

    resp = session.get(url_prelogin)
    json_data = re.findall(r'(?<=\().*(?=\))', resp.text)[0]
    data = json.loads(json_data)

    servertime = data['servertime']
    nonce = data['nonce']
    pubkey = data['pubkey']
    rsakv = data['rsakv']

    print(urllib.parse.quote(username))
    su = base64.b64encode(username.encode(encoding="utf-8"))

    rsaPublicKey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublicKey, 65537)
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
    sp = binascii.b2a_hex(
        rsa.encrypt(
            message.encode(
                encoding='utf-8'),
            key))
    postdata = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'qrcode_flag': 'false',
        'userticket': '1',
        'pagerefer': 'https://www.google.com.hk/',
        'vsnf': '1',
        'su': su,
        'service': 'miniblog',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'rsakv': rsakv,
        'sp': sp,
        'sr': '1920*1080',
        'encoding': 'UTF-8',
        'prelt': '33',
        'url': 'https://www.weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'TEXT',

    }
    resp = session.post(url_login, data=postdata)
    login_url = re.findall(r'http://weibo.*&retcode=0', resp.text)
    print(login_url)

    print(resp.content.decode('gbk'))
    # print(resp.text.encode('utf-8').decode())


if __name__ == '__main__':
    userlogin('18120440747', 'qqfy.326498')
