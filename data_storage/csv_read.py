#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 10:14
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : csv_read.py
# @Software: PyCharm


import csv
import json


# csv读取

csv_file = csv.reader(open('11.csv', 'r'))
print(csv_file)
for stu in csv_file:
    print(stu)


# csv写入
stu1 = ['marry',26]
stu2 = ['bob',23]
# 打开文件，追加a
out = open('11.csv','a', newline='')
# 设定写入模式
csv_write = csv.writer(out,dialect='excel')
# 写入具体内容
csv_write.writerow(stu1)
csv_write.writerow(stu2)
print ("write over")