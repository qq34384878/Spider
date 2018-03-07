#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 15:27
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider.py
# @Software: PyCharm
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
import requests
from pyquery import PyQuery as pq
import pymongo
from wechat.config import *

client = pymongo.MongoClient(MONGO_URI)
db = client[MONGO_DB]


# 爬取的主链接
base_url = 'http://weixin.sogou.com/weixin?'

# 请求头
header = {
    'Cookie': 'IPLOC=CN4201; SUID=F804121B3120910A000000005A4DD06D; SUV=006871D91B1204F85A4DD06FB4ECF618; clientId=21B734D32AA26C3731583F772B626D89; ld=4Zllllllll2zOks0lllllV$g$G1lllll$TV6tZllll9llllllylll5@@@@@@@@@@; ABTEST=7|1519888946|v1; JSESSIONID=aaas2pgLqE2BX6-xizwhw; sct=2; PHPSESSID=c90626fjteo8bkroo80iitrs67; SUIR=D3C4D10BA1A5C69CA64638C2A10708F2; seccodeErrorCount=1|Fri, 02 Mar 2018 03:23:18 GMT; SNUID=B9D1D903A7ADCECDC41F88B2A8897727; seccodeRight=success; successCount=1|Fri, 02 Mar 2018 03:23:35 GMT; refresh=1',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://weixin.sogou.com/weixin?query=python&_sug_type_=&s_from=input&_sug_=n&type=2&page=10&ie=utf8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

proxy = None

'''
获取代理IP, 从已搭建好的代理池中取一个
'''
def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy
    if count >= MAX_COUNT:
        print('Tried Too Many Counts')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=header, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=header)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # Need Proxy(ip限制需要设置一个代理ip)
            print('302')
            # 获取代理方法
            proxy = get_proxy()
            if proxy:
                print("Using Proxy", proxy)
                # count += 1
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        # 连接失败则抛出一个异常,并打印异常消息,尝试重新获取次数+1,然后回调此方法
        print('Error Occurred', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    # print(html)
    return html

def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html):
    doc = pq(html)
    title = doc('.rich_media_title').text()
    content = doc('.rich_media_content').text()
    date = doc('#post-date').text()
    nickname = doc('#post-user').text()
    wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
    return {
        'title': title,
        'content': content,
        'date': date,
        'nickname': nickname,
        'wechat': wechat
    }

def sava_to_mongo(data):
    if db['articles'].update({'title': data['title']}, {'$set': data}, True):
        print('Saved to Mongo', data['title'])
    else:
        print('Saved to Mongo Failed', data['title'])


def main():
    for page in range(1, 11):
        html = get_index(KEYWORD, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                if article_html:
                    article_data = parse_detail(article_html)
                    print(article_data)
                    sava_to_mongo(article_data)

if __name__ == '__main__':
    # get_index('风景', 1)
    main()
