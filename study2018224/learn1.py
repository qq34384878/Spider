#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 14:47
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : learn1.py
# @Software: PyCharm

import requests
import re
import random

import time


class download:

    def __init__(self):
        self.iplist = [
            '120.50.72.21:80',
            '124.206.133.227:80',
            '115.28.101.22:3128',
            '61.135.217.7:80',
            '103.239.253.137:8080',
            '174.32.136.106:87',
            '198.148.112.37:1080',
            '171.113.159.219:808',
            '110.200.76.103:80',
            '116.211.123.138:80',
            '121.61.2.135:8888',
        ]
        self.ip = ''.join(str(random.choice(self.iplist)).strip())
        print(self.ip)

        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]

    def get(self, url, timeout, proxy=None, num_retries=6):  # 给函数一个默认参数proxy为空
        # 从self.user_agent_list中随机取出一个字符串
        UA = random.choice(self.user_agent_list)
        headers = {'User-Agent': UA}  # 构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）

        if proxy is None:  # 当代理为空时，不使用代理获取response（别忘了response啥哦！之前说过了！！）
            try:
                return requests.get(
                    url, headers=headers, timeout=timeout)  # 这样服务器就会以为我们是真的浏览器了
            except BaseException:  # 如过上面的代码执行报错则执行下面的代码
                if num_retries > 0:  # num_retries是我们限定的重试次数
                    time.sleep(10)  # 延迟十秒
                    print(u'获取网页出错，10S后将获取倒数第：', num_retries, u'次')
                    return self.get(
                        url, timeout, num_retries - 1)  # 调用自身 并将次数减1
                else:
                    print(u'开始使用代理')
                    time.sleep(10)
                    IP = ''.join(
                        str(random.choice(self.iplist)).strip())  # 下面有解释哦
                    proxy = {'http': IP}
                    return self.get(url, timeout, proxy, )  # 代理不为空的时候

        else:  # 当代理不为空
            # 将从self.iplist中获取的字符串处理成我们需要的格式（处理了些什么自己看哦，这是基础呢）
            print(self.ip)
            proxy = {'http': self.ip}  # 构造成一个代理
            return requests.get(
                url,
                headers=headers,
                proxies=proxy,
                timeout=timeout)


Xz = download()
print(Xz.get("http://www.mzitu.com/", 3))
# Xz.get("http://www.mzitu.com/", 3)