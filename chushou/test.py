#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 17:25
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : test.py
# @Software: PyCharm

from selenium_study import webdriver
import os
import time

req_url = 'http://www.baidu.com'

browser = webdriver.Firefox()
browser.get(req_url)