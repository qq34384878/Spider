#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 12:28
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : liaoxuefeng_python_crawler.py
# @Software: PyCharm
import logging
import re

from pdf.crawler import Crawler
from bs4 import BeautifulSoup

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


class LiaoXueFengPythonCrawler(Crawler):
    """
    廖雪峰python3教程
    """

    def parse_menu(self, response):
        """
        解析目录结构，获取所有URL目录列表
        :param response: 爬虫所返回的response对象
        :return: url生成器
        """
        soup = BeautifulSoup(response.content, "html.parser")
        menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
        for li in menu_tag.find_all("li"):
            url = li.a.get("href")
            if not url.satrtswith("http"):
                url = "".join([self.domain, url])
            yield url

    def parse_body(self, response):
        """
        解析正文
        :param response: 爬虫返回的response对象
        :return: url生成器
        """
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            body = soup.find_all(class_="x-wiki-content")[0]

            # 加入标题，居中显示
            title = soup.find('h4').get_text()
            center_tag = soup.new_tag("center")
            title_tag = soup.new_tag("h1")
            title_tag.string = title
            center_tag.insert(1, title_tag)
            body.insert(1, center_tag)

            html = str(body)
            # body中的img标签的src相对路径的改成绝对路径
            pattern = "(<img .*?src=\")(\")"

            def func(m):
                if not m.group(2).startswith("http"):
                    return "".join(
                        m.group(1), self.domain, m.group(2), m.group(3))
                else:
                    return "".join([m.group(1), m.group(2), m.group(3)])

            html = re.compile(pattern).sub(func, html)
            html = html_template.format(content=html)
            html = html.encode("utf-8")
            return html
        except Exception as e:
            logging.error("解析错误", exc_info=True)


if __name__ == '__main__':
    start_url = "http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000"
    crawler = LiaoXueFengPythonCrawler("廖雪峰Git", start_url)
    crawler.run()