#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/10 11:13
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : spider.py
# @Software: PyCharm
import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

# Headless无界面模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()   # 对接FireFox
# browser = webdriver.PhantomJS() # 对接PhantomJS
# browser.get('https://www.taobao.com')
wait = WebDriverWait(browser, 10)   # 等待10秒后再操作
KEYWORD = 'iPad'
MAX_PAGE = 100

# MongoDB配置
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located(  # 判断该页面元素是否在页面中存在
                (By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))  # 定位到输入元素
            submit = wait.until(EC.element_to_be_clickable(  # 判断该页面元素是否在页面上可用和可被单击
                (By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))  # 定位到提交元素
            input.clear()   # 清空输入标签中的内容
            input.send_keys(page)   # 传递page值到输入框
            submit.click()  # 点击提交标签
        wait.until(
            EC.text_to_be_present_in_element(   # 判断在该页面元素中是否包含特定的文本
                (By.CSS_SELECTOR,
                 '#mainsrp-pager li.item.active > span'),
                str(page)))  # 判断该page值是与CSS_SELECTOR找到的是否相同
        wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.m-itemlist .items .item')))  # 所有元素加载出来后才允许通过
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


def get_products():
    """
    提取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    # print(doc)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def main():
    """
    遍历每一页
    :return:
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)


if __name__ == '__main__':
    main()
