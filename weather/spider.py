#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 17:45
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider.py
# @Software: PyCharm

"""
抓取每天的天气预报
python
url:http://www.weather.com.cn/weather1d/10280101.shtml#dingzhi_first

"""
import requests
import bs4


def get_html(url):
    """
    封装请求
    :param url:
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'ContentType': 'text/html; charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
    }

    try:
        respoense = requests.get(url)
        if respoense.status_code == 200:
            print(respoense.text.encode('utf-8'))
            return respoense.text.encode('utf-8')
    except BaseException:
        print("请求失败")


def get_content(url):
    """
    抓取页面天气数据
    :param url:
    :return:
    """
    weather_list = []
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    content_ul = soup.find('div', class_='t').find_all('li')
    print(content_ul)
    for content in content_ul:
        try:
            weather = []
            weather['day'] = content.find('h1').text
            print(weather['day'])
            weather['temperature'] = content.find(
                'p', class_='tem').span.text + content.find('p', class_='tem').em.text
            weather_list.append(weather)
        except BaseException:
            print('查询不到')
    print(weather_list)


if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather1d/101200101.shtml'
    # print(url)
    get_content(url)
