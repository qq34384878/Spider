#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/10 17:38
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider_selenium.py
# @Software: PyCharm
import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq


url = 'http://maoyan.com/board/4?offset='
home = 'http://maoyan.com'

web = webdriver.Chrome()
wait = WebDriverWait(web, 10)   # 等待10秒后再操作

# MongoDB配置
MONGO_URL = 'localhost'
MONGO_DB = 'maoyan'
MONGO_COLLECTION = 'movie_ranking'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def get_products():
    html = web.page_source
    doc = pq(html)
    # print(doc)
    items = doc(
        '.main .board-wrapper .board-item-main .board-item-content').items()
    for item in items:
        product = {
            'name': item.find('.movie-item-info .name').text(),
            'url': home + item.find('.movie-item-info .name').children().attr('href'),
            # 'image': item.find('.movie-item-info .name a').attr('href'),
            'star': item.find('.movie-item-info .star').text(),
            'releasetime': item.find('.movie-item-info .releasetime').text(),
            # 'title': item.find('.shop').text(),
            # 'location': item.find('.location').text()
        }
        print(product)
    save_to_mongo(product)


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        offset = (page - 1) * 10
        web.get(url + str(offset))
        get_products()
    except TimeoutException:
        index_page(page)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result:
    :return:
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


if __name__ == '__main__':
    for page in range(1, 11):
        index_page(page)
