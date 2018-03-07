#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 15:08
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : test.py
# @Software: PyCharm
import requests
import time
from bs4 import BeautifulSoup
import pdfkit

'''
需要解决被反爬问题
'''


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "Hm_lvt_2efddd14a5f2b304677462d06fb4f964=1517986170; atsp=1517996024946_1517995863628; Hm_lpvt_2efddd14a5f2b304677462d06fb4f964=1517995864",
    "Host": "www.liaoxuefeng.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
# url = 'https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000'


def par_url_to_html(url):
    response = requests.get(url, headers=header)
    time.sleep(2)
    # print(response.content)
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup)
    if len(soup.find_all(class_="x-wiki-content x-main-content")) == 0:
        print("跳过")
        return
    else:
        body = soup.find_all(class_="x-wiki-content x-main-content")[0]
        print(body)
        # html = bytes(str(body).encode('utf-8'))
        html = str(body).encode('utf-8')
        # return html
        with open("a.html", 'wb') as f:
            f.write(html)
            sava_pdf('a.html', 'h.pdf')


def get_url_list():
    """
    获取所有URL目录列表
    """
    response = requests.get(
        'https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000',
        headers=header)
    print(response.status_code)
    if response.status_code == 200:
        print(response.content)
        time.sleep(2)
        soup = BeautifulSoup(response.content, "html.parser")
        menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
        urls = []
        for div in menu_tag.find_all("div"):
            url = "http://www.liaoxuefeng.com" + div.a.get('href')
            urls.append(url)
        print(urls)
        return urls
    else:
        print('请求失败')
        time.sleep(5)
        pass


def sava_pdf(html, file_name):
    """
    把所有html文件转换成pdf文件
    :param htmls:
    :return:
    """
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
    pdfkit.from_file(html, file_name, options=options)


if __name__ == '__main__':
    # for url in get_url_list():
    #     print(url)
    #     par_url_to_html(url=url)
    #     break
    sava_pdf('a.html', 'git.pdf')
    # sava_pdf()
