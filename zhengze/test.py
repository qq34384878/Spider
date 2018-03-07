#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 14:32
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : test.py
# @Software: PyCharm


import re

line = 'fanyu123213213uuuuuuufff'
# if line == 'fangyu123':
# regex_str = '.*?(u.*?u).*?'
regex_str = '.*(u.{3,5}u).*'
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
