#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 10:25
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : learn1.py
# @Software: PyCharm
import pymongo

client = pymongo.MongoClient('localhost', 27017)    # 连接数据库
walden =client['walden']    # 创建数据库,并给数据库命名
sheet_tab = walden['sheet_tab'] # 创建数据表单

'''
写入操作
'''
# path = 'C:/Users/double/PycharmProjects/Spider/mongodb/walden.txt'
# with open(path, 'r') as file:
#     lines = file.readlines()
#     for index, line in enumerate(lines):
#         data = {
#             'index': index,
#             'line': line,
#             'words': len(line.split())
#         }
#         # print(data)
#         sheet_tab.insert_one(data)

'''
读取操作
'''
for item in sheet_tab.find():
    print(item['line'])