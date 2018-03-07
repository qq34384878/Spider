#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 17:32
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : test3.py
# @Software: PyCharm
import requests
import time


def get_html():
    html = requests.get(url='http://news.163.com/18/0226/04/DBHTL2FT0001875P.html')


def post_html():
    form_data = {
        'request:queryType': '',
        'request:queryAuto': '',
        'request:queryMode': '',
        'request:queryCom': '1',
        'request:mn': '小米',
        'request:ncs': '',
        'request:nc': '',
        'request:hnc': '',
        'request:hne': '',
        'request:sn': '',
        'request:imf': '',
        'request:maxHint': '',
        'request:queryExp': 'mnoc = 小米*',
        'request:mi': '7C507F9BD853BD0BB0905F8B0F68C6FB',
        'request:tlong': 'TdA0gRBFZCH/BcCEVceniI65c+uLJu7uPVLpYYXcxSrDd83mNhgZiWoc2X8sUFW5',
        'attribute-node:record_cache-flag': 'false',
        'attribute-node:record_start-row': '1',
        'attribute-node:record_page-row': '50',
        'attribute-node:record_sort-column': 'RELEVANCE',
        'attribute-node:record_page': '1'
    }
    Headers = {
        'Cookie': 'FSSBBIl1UgzbN7N80S=2tkuLgceJNLQI7GzfvDxqEhYWtUr72q_ezhiFNv6nsS62Ji4.e3R82FImA4awOwN; __jsluid=a39dc756c9d93c311104445d5c1dbe9a; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1519698849; Hm_lpvt_d7682ab43891c68a00de46e9ce5b76aa=1519698849; tmrpToken=F571C0A466C9B9CA98EC9C568C6C6884; FSSBBIl1UgzbN7N80T=1yDMYPiAiUbtITCt3c7MvStEArgmZ4E_mZzTyEL9Kp3dD.bhi.XVNC8IpATAJhSIDUHtPKSUv9Gf78d4wyYaCTKpQXiEUdP9Q6_u3xF0q52fCCwPjKXi0wuN1FgEN92x3Cb1is.38U.7AnkNQd9GpvGzPhCBHxqa.Ij9cyu1ZLxx0TQvCSFFxdAv1XjbyM0QEJspV.uG8nb.GfGeoM6pSKVy7ANqY5x1HuRxEwYWY1pJHBfRHxk9xaKOKvYtLb7XLogf0oBH_9psQg.U4Q4qukzFpg8yi41pBLbRJSsmrMQyMyUFl6ZS5iv011vhQ3iMZxca_MMEPHYrL0NCo18ebyoNMpYXK8FTbvnAuqoBzAzOo5p4c.M9U6TRMpTxfHxk9YQq; JSESSIONID=21C3BF1BD07C8766AEC983E475AE40A1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    response = requests.post(url='http://wsjs.saic.gov.cn/txnRead02.ajax?MmEwMD=1VwJGHYD4_eQj3zQzB6J1Qp827OsxKs7apCOW2unOZkNuDew4DTcQMmx9eXDgbjxu_VQU4jr1x46Ru9zLVibk3JoN2bgkSepR7i2QLf5hB84CppZj.bq2OyINktkpyiITbfOztwT6PUgfCvXVigb37kZ1RgwuRgDEkHdsytQobhfC_uaqMP0d_Xg86mERHCb__SGYBPrpAM8vRqkTNWBfQzKQ1pla_DbiteU8SYKXo1wv5JurkLf2rDiiuZKa2MpZrXX0hEBLX40ARgSxGG0EARZ5ek99PoqKhdxYaCE1_6vxbEqXIRYfcAz6ZQda3q6yK1W9fJ_OUqf517pDfH22KBlDC9VCpHSY6MkaKZeyocxo0gsAVqiUwm5IAzyP.y01Tpk', headers=Headers, data=form_data)
    print(response.status_code)
    print(response.content)

def print_sub(x):
    print(x**2)

from multiprocessing import Pool





if __name__ == '__main__':
    start_time = time.clock()
    post_html()
    p = Pool()
    p.map(print_sub, [i for i in range(0,50000)])
    # for i in range(0,700000):
    #     print_sub(i)
    end = (time.clock() - start_time)
    print(end)
