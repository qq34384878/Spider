#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 14:55
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : learn_one.py
# @Software: PyCharm

# xpath选择器匹配练习
from lxml import etree  # 从lxml导入etree

# 定义一个函数, 给他一个html, 返回xml结构


def getxpath(html):
    return etree.HTML(html)


# 实战一
sample1 = """<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <!-- this is the end -->
  </body>
</html>
"""

# 获取xml结构
xml1 = getxpath(sample1)

# 获取标题(两种方法都可以)
# 相对路径和绝对路径
one = xml1.xpath('//title/text()')      # 返回的list类型
two = xml1.xpath('/html/head/title/text()')
print(one)  # ['My page']
print(two)  # ['My page']
print(type(one))    # <class 'list'>

three = xml1.xpath('//h2/a/@src')   # 获取属性内容用 @xxx
xml1.xpath('//@href')   # ['#']
print(three)    # ['x']

four = xml1.xpath('//text()')   # 获取文本内容用 text()
print(four)
'''
['\n  ',
 '\n    ',
 'My page',
 '\n  ',
 '\n  ',
 '\n    ',
 'Welcome to my ',
 'page',
 '\n    ',
 'This is the first paragraph.',
 '\n    ',
 '\n  ',
 '\n']
'''

five = xml1.xpath('//comment()')    # 获取注释用 comment()
print(five)  # [<!-- this is the end -->]


# 实战二
sample2 = """
<html>
  <body>
    <ul>
      <li>Quote 1</li>
      <li>Quote 2 with <a href="...">link</a></li>
      <li>Quote 3 with <a href="...">another link</a></li>
      <li><h2>Quote 4 title</h2> ...</li>
    </ul>
  </body>
</html>
"""
# 获取xml结构
xml2 = getxpath(sample2)
# 获取所有的li中的text文本内容
six = xml2.xpath('//li/text()')
print(six)  # ['Quote 1', 'Quote 2 with ', 'Quote 3 with ', ' ...']

# 获取第1个li(两种写法一样)
print(xml2.xpath('//li[position() = 1]/text()'))    # ['Quote 1']
print(xml2.xpath('//li[1]/text()'))  # ['Quote 1']
# 获取第2个li
print(xml2.xpath('//li[position() = 2]/text()'))    # ['Quote 2 with ']
print(xml2.xpath('//li[2]/text()'))  # ['Quote 2 with ']


# 获取所有奇数位的li
print(xml2.xpath('//li[position() mod2 = 1]/text()'))
# ['Quote 1', 'Quote 3 with ']

# 获取所有偶数位的li
print(xml2.xpath('//li[position() mod2 = 0]/text()'))
# ['Quote 2 with ', ' ...']

# 获取最后一个li
print(xml2.xpath('//li[last()]/text()'))    # [' ...']

# 获取li标签中所有有a标签的text
print(xml2.xpath('//li[a]/text()'))     # ['Quote 2 with ', 'Quote 3 with ']
# 获取li标签中所有有a或h2标签的text
# ['Quote 2 with ', 'Quote 3 with ', ' ...']
print(xml2.xpath('//li[a or h2]/text()'))

# 获取a标签 和 h2标签中的text
print(xml2.xpath('//a/text()|//h2/text()'))

'''
上面的li 可以更换为任何标签，如 p、div
位置默认以1开始的
最后一个用 li[last()] 不能用 li[-1]
这个一般在抓取网页的下一页，最后一页会用到
'''

# 实战三
sample3 = """<html>
  <body>
    <ul>
      <li id="begin"><a href="https://scrapy.org">Scrapy</a>begin</li>
      <li><a href="https://scrapinghub.com">Scrapinghub</a></li>
      <li><a href="https://blog.scrapinghub.com">Scrapinghub Blog</a></li>
      <li id="end"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
      <li data-xxxx="end" abc="abc"><a href="http://quotes.toscrape.com">Quotes To Scrape</a>end</li>
    </ul>
  </body>
</html>
"""

xml3 = getxpath(sample3)


# 获取 a标签下 href以https开始的
print(xml3.xpath('//a[starts-with(@href, "https")]/text()'))
# 获取 href=https://scrapy.org
print(xml3.xpath('//li/a[@href="https://scrapy.org"]/text()'))
# 获取 id=begin
print(xml3.xpath('//li[@id="begin"]/text()'))
# 获取text=Scrapinghub
print(xml3.xpath('//li/a[text()="Scrapinghub"]/text()'))


# 获取某个标签下 某个参数=xx
print(xml3.xpath('//li[@data-xxxx="end"]/text()'))
print(xml3.xpath('//li[@abc="abc"]/text()'))
'''
根据html的属性或者文本直接定位到当前标签
文本是 text()='xxx'
其它属性是@xx='xxx'
这个是我们用到最多的，如抓取知乎的xsrf(见下图)
我们只要用如下代码就可以了//input[@name="_xsrf"]/@value
'''


sample4 = u"""
<html>
  <head>
    <title>My page</title>
  </head>
  <body>
    <h2>Welcome to my <a href="#" src="x">page</a></h2>
    <p>This is the first paragraph.</p>
    <p class="test">
    编程语言<a href="#">python</a>
    <img src="#" alt="test"/>javascript
    <a href="#"><strong>C#</strong>JAVA</a>
    </p>
    <p class="content-a">a</p>
    <p class="content-b">b</p>
    <p class="content-c">c</p>
    <p class="content-d">d</p>
    <p class="econtent-e">e</p>
    <p class="heh">f</p>
    <!-- this is the end -->
  </body>
</html>
"""

xml4 = getxpath(sample4)

# 获取p标签下 class=test的所有文本
# 少了一个C#JAVA
print(''.join(xml4.xpath('//p[@class="test"]/text()')))
# 完整
# 获取p标签下的所有文字
print(xml4.xpath('string(//p[@class="test"])'))

'''
想要获取某个标签下所有的文本（包括子标签下的文本），使用string
如 <p>123<a>来获取我啊</a></p>，这边如果想要得到的文本为"123来获取我啊"，则需要使用string
'''

# 获取p标签下 所有class中有content的
# 发现少获取一个<p class="econtent-e">e</p>
print(xml4.xpath('//p[starts-with(@class,"content")]/text()'))
# 获取p标签下 所有class中有content的
# 这个成功了
print(xml4.xpath('//p[contains(@class,"content")]/text()'))

'''
starts-with 匹配字符串前面相等
contains 匹配任何位置相等
当然其中的(@class,"content")也可以根据需要改成(text(),"content")或者其它属性(@src,"content")
'''
