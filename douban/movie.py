#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 14:32
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : movie.py
# @Software: PyCharm
import urllib
from lxml import etree

import requests

"""
获取每个主题下有多少页内容  (没有输入，输出字典)
"""


class theme_page(object):
    def __init__(self):
        self.tags = [
            u"爱情",
            u"喜剧",
            u"动画",
            u'剧情',
            u'科幻',
            u'动作',
            u'经典',
            u'悬疑',
            u'青春',
            u'犯罪',
            u'惊悚',
            u"文艺",
            u"搞笑",
            u"纪录片",
            u'励志',
            u'恐怖',
            u'战争',
            u'短片',
            u'黑色幽默',
            u'魔幻',
            u'传记',
            u'情色',
            u"感人",
            u"暴力",
            u'动画短片',
            u'家庭',
            u'音乐',
            u'童年',
            u'浪漫',
            u'黑帮',
            u'女性',
            u'同志',
            u"史诗",
            u"童话",
            u'烂片',
            u'cult']

    def get_total_num(self):
        tags = self.tags
        total_num = []
        list = []
        for tag in tags:
            # print(tag)  # 主题名称
            re_url = 'https://movie.douban.com/tag/{}?start=0&type=T'.format(
                urllib.request.quote(tag))
            # print(re_url)   # 主题链接
            s = requests.get(re_url)    # 获取get请求返回的html源码
            contents = s.content.decode('utf-8')    # 将返回的html源码编码成utf-8
            selector = etree.HTML(contents)         # 将返回的html源码结构转换成xml
            num = selector.xpath(
                '//*[@id="content"]/div/div[1]/div[3]/a[10]/text()')
            total_num.append(int(num[0]))
            # print(num[0])   # 总页数
            list.append({       # list :{'爱情': '393'}, {'喜剧': '392'}, {'动画': '274'},
                '主题': tag,
                '总页数': num[0],
            })
        print(list)
        return list


if __name__ == '__main__':
    t = theme_page()
    t.get_total_num()