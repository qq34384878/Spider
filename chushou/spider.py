#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 14:28
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider.py
# @Software: PyCharm
import requests
import time


# cookie = {
#     'Cookie': '_i7=894e9a6b560046428892011fc9fb43b5; Hm_lvt_c0d39162b8644bbf06f351695f6297ea=1515749184,1516009122,1516947727; _a2="Vvzto5uGvPLwz9ZIuII3xQubPq2DFmUjyUmQiEIngVGw9Xd2JWSwZ9PZ45im51EbiBesEeAYml0skBdD+YEpEg=="; Hm_lpvt_c0d39162b8644bbf06f351695f6297ea=1516956109; smidV2=201801261422061853bf7331f6326ed732815d892a757b002a282c2fbfc8c40'
# }

# 模拟浏览器
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'https://kascdn.kascend.com/jellyfish/liveplayer/v/liveplayer.swf?v1/[[DYNAMIC]]/1',
    'Origin': 'https://kascdn.kascend.com',
    'Cookie': '_i7=894e9a6b560046428892011fc9fb43b5; Hm_lvt_c0d39162b8644bbf06f351695f6297ea=1515749184,1516009122,1516947727; _a2="Vvzto5uGvPLwz9ZIuII3xQubPq2DFmUjyUmQiEIngVGw9Xd2JWSwZ9PZ45im51EbiBesEeAYml0skBdD+YEpEg=="; Hm_lpvt_c0d39162b8644bbf06f351695f6297ea=1516956109; smidV2=201801261422061853bf7331f6326ed732815d892a757b002a282c2fbfc8c40',
    'Content-Length': '529',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
}


def send_danmu():
    url = 'https://chat.chushou.tv/chat/send.htm'
    form_data = {
        # 'deviceId': 'WHJMrwNw1k/HN2xav6V7JHxvvxK1pWxeK1Ohy/ojTO3Mz9igj6T3ciHg/1L+caYGxVmyL5NE56cuIHA1g1OdLTg/lrgI4N7p1T5YDlG8ndzIvWiH5uWWtOZSD3EmPbcN1b2GXgZ5AQVKMXAh6wd/Dd8P4Q7ORb24hXlteanFzTbhkhoMiJ81hY8XGXUjeh6qHyw74jIGEpERiNVCcw5ywKPxS/ZF5rz8fCOGQBzardLXTOS2rohpIUJ85iiRWOzmbR/t9WW/jIrAFA4nOgFtsiIsUjFtjkIWK1487582755342',
        'deviceId': 'WHJMrwNw1k/HN2xav6V7JHxvvxK1pWxeK1Ohy/ojTO3Mz9igj6T3ciHg/1L+caYGxVmyL5NE56cuIHA1g1OdLTg/lrgI4N7p146JzmLwmgmgZfhPZ1E/fJJSD3EmPbcN1b2GXgZ5AQVKPwtMHJl0PIda+pudYHMXWr+cKLjzCAKgTJrGzzeI4ggo8GQJ2iunlq7R4LdREhEPNtAKvckCXn9P3JfIO6ex/REuhSDExo/VK/001zw+71twuOXG+4ocFQ2C5nbwxLKYXXT+s9g2g3A==1487582755342',
        'token': 'dc8ff83c32cf20ebg5023eb15',
        'content': '45test',
        '_appkey': 'CSWeb',
        '_identifier': '894e9a6b560046428892011fc9fb43b5',
        'roomId': 38109769,
        '_t': str(int(time.time()*1000)),
        '_appVersion': 316,
        '_sign': -1976670550
    }

    resp = requests.post(url=url, data=form_data, headers=header)
    if resp.status_code == 200:
        print(resp.json())


if __name__ == '__main__':
    send_danmu()
