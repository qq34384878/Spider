#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 15:45
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : talk.py
# @Software: PyCharm

import requests
import json


def talk(content, userid):
    result = ''
    url = 'http://www.tuling123.com/openapi/api'
    s = requests.session()
    d = {"key": "7159f3e34c864911ae660501f13a6f37", "info": content, "userid": userid}  # 填写自己申请的key
    data = json.dumps(d)
    r = s.post(url, data=data)
    text = json.loads(r.text)
    code = text["code"]
    if code == 100000:
        result = text["text"]
    elif code == 200000:
        result = text["text"] + '\n' + text["url"]
    elif code == 302000:
        result = text["text"] + '\n' + \
            text["list"][0]["article"] + text["list"][0]["detailurl"]
    elif code == 308000:
        result = text["text"] + '\n' + \
            text["list"][0]["info"] + text["list"][0]["detailurl"]
    print(result)
    return result
