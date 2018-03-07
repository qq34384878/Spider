#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 12:11
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : crawler.py
# @Software: PyCharm
import logging
import os
import time

from urllib.parse import urlparse  # py3

import pdfkit
import requests


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

}

class Crawler(object):
    """
    爬虫基类，所有爬虫都应该继承此类
    """

    def __init__(self, name, start_url):
        """
        初始化
        :param name:
        :param start_url:
        """
        self.name = name
        self.start_url = start_url
        self.domain = '{uri.scheme}://{uri.netloc}'.format(
            uri=urlparse(self.start_url))

    @staticmethod
    def request(url, **kwargs):
        """
        网络请求，返回response对象
        :param url:
        :param kwargs:
        :return:
        """
        response = requests.get(url, headers=HEADERS, **kwargs)
        if response.status_code == 200:
            return response
        else:
            logging.error(str(response.url)+u"请求失败，错误码:"+str(response.status_code))
            raise Exception

    def parse_menu(self, response):
        """
        从response中解析出所有目录的URL链接
        :param response:
        :return:
        """
        raise NotImplementedError

    def parse_body(self, response):
        """
        解析正文，由子类实现
        :param response: 爬虫返回的response对象
        :return: 返回经过处理的html正文文本
        """
        raise NotImplementedError

    def run(self):
        start = time.time()
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }
        htmls = []
        for index, url in enumerate(
            self.parse_menu(
                self.request(
                self.start_url))):
            html = self.parse_body(self.request(url))
            f_name = ".".join([str(index), "html"])
            with open(f_name, 'wb') as f:
                f.write(html)
            htmls.append(f_name)

        pdfkit.from_file(htmls, self.name + ".pdf", options=options)
        for html in htmls:
            os.remove(html)
        total_time = time.time() - start
        print(u"总共耗时: %f 秒" % total_time)
