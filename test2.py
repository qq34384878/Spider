#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/5 17:18
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : test2.py
# @Software: PyCharm
import re
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def get_test1():
    response = requests.get(url='http://www.nhfpc.gov.cn/zhuz/bottom/bottom2.shtml?MmEwMD=12uGUH_g2MawLb4bx8gPm.GaAJrdTGzSgqk5vHh9bxuJ1eKMmpYk_EGhxO2xe73F04eoRF2nzVlzeDQx2GlqjgL_jRPsyaN2u1g8Ci0gZx0w5Yef_rX5J4Ilu0fpXYfWBnN3gYLXP1njW_J3G4wZqmnc2hyD3bzPGsXNJFlX6CBYaIDFL9z8yH4NRVTdPDotuWBO4KgnDj_DUWUpIHnBjfk55TKnA15CqO8OxZFW3Pv0qbOXT.JD05.wcaqMSlc1OZOIBbj9x1FAGwhhQiPWPgiHw3_QvlTL1U83TAUN_SjJkleWrh.zjGrgn4p7GlG1tPS32wqpfxAqEeGf7k2x5BlcG9kw35.2Wkwuw.szbYHhbGa11h0Vvd1qfeGZNlf4lnRpBjoJf6Awfog')
    print(response.url)
    print(response.status_code)
    print(response.content)


def bs_test():
    test_html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div>
<span class="basic-data-title">生产厂商: </span>
<span title="海康">海康</span>
</div>
</body>
</html>
    '''
    soup = BeautifulSoup(test_html, 'html.parser')
    tags = soup.find_all('span')
    t = soup.div.span
    # print(t.name)
    print(t)
    print(tags[1].contents)
    for tag in tags:
        c = tag.contents
        print(c)
        print(type(c))


def re_test():
    re_str = '''
    <a title="技术工程师" href="/job/po43241412.html" target="_blank">技术工程师</a>
    <a title="外贸" href="/job/po433414121.html" target="_blank">外贸</a>
    <a title="业务工程师" href="/job/po54354112.html" target="_blank">业务工程师</a>
    <a title="运维工程师" href="/job/po43256412.html" target="_blank">运维工程师</a>
    '''
    item_list = re.findall(r'>(.*?)</a>', re_str)
    print(item_list)


def get_test():
    response = requests.get(
        url='http://www.gyfc.net.cn/2_proInfo/search.aspx?type=1&box_pro_qu=no&box_pro_xz=no&box_pro_mc=-%u8bf7%u8f93%u5165%u697c%u76d8%u540d%u79f0-&box_pro_dj=no',
        headers=headers
    )
    print(response.status_code)
    if response.status_code == 200:
        print(response.content)
        print(response.text)


if __name__ == '__main__':
    # get_test()
    # bs_test()
    # re_test()
    get_test()
