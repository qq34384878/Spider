#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 10:25
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : test.py
# @Software: PyCharm
import json
import threading

import time
import requests
import xlwt as xlwt

balance = 1000
lock = threading.Lock()


def chande_balance(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(10000):
        chande_balance(n)


def main():
    t1 = threading.Thread(target=run_thread, args=(1,))
    t2 = threading.Thread(target=run_thread, args=(10,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()


def postman():
    url = 'https://now.qq.com/cgi-bin/poll'

    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://now.qq.com/h5/index.html?_bid=2336&_wv=16778245&roomid=1210810416&from=50027&channellink=CK1335890252938&ioschannel=50027',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

    cookies = {}

    cookie = "_qpsvr_localtk=0.5914363602200843; pgv_pvi=2127276032; pgv_si=s9249711104; pt2gguin=o0034384878; uin=o0034384878; ptisp=ctc; RK=SElGDO6fOe; ptcz=cb3e6d57ab915a3f1fdbe8561089972bd2e4c4d3cc24e0562043d10fe32aded8; _supWebp=1; skey=@sr0wPJIyd; Hm_lvt_1243dadf55248215260536a63a47c6d1=1514520341,1514529346,1514859751,1514859755; Hm_lpvt_1243dadf55248215260536a63a47c6d1=1514859755; _qpsvr_localtk=0.5914363602200843; pgv_pvi=2127276032; pgv_si=s9249711104; pt2gguin=o0034384878; uin=o0034384878; ptisp=ctc; RK=SElGDO6fOe; ptcz=cb3e6d57ab915a3f1fdbe8561089972bd2e4c4d3cc24e0562043d10fe32aded8; _supWebp=1; skey=@sr0wPJIyd; Hm_lvt_1243dadf55248215260536a63a47c6d1=1514520341,1514529346,1514859751,1514859755; Hm_lpvt_1243dadf55248215260536a63a47c6d1=1514859755"

    for line in cookie.split(';'):
        name, value = line.strip().split('=')
        cookies[name] = value

    r = str(json.dumps({"seq1": 0, "seq2": 0,
                        "roomid": 1046416731, "client_type": 0}))
    send_data = {'r': r}
    s = requests.Session()
    r = s.post(url, headers=headers, data=send_data, cookies=cookies)
    source = json.loads(r.text)
    print(source)
    # print(r.cookies.get_dict())


def save_csv():
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    DATA = [
        ['学号', '姓名', '年龄', '性别', '成绩'],
        ['1001', 'A', '11', '男', '12'],
        ['1002', 'B', '12', '女', '22'],
        ['1003', 'C', '13', '女', '32'],
        ['1004', 'D', '14', '男', '52'],
    ]
    for i, row in enumerate(DATA):
        for j, col in enumerate(row):
            booksheet.write(i, j, col)
    workbook.save('info.xls')


def scraping():
    # data = "cursor=6508521346694286093_1515383230325&user_id=83274563234&live_sdk_version=313&iid=22844387158&device_id=42834931943&ac=wifi&channel=oppo&aid=1112&app_name=live_stream&version_code=313&version_name=3.1.3&device_platform=android&ssmix=a&device_type=ONEPLUS+A5000&device_brand=OnePlus&language=zh&os_api=25&os_version=7.1.1&uuid=99001062553882&openudid=8f64987d7f0e26a4&manifest_version_code=313&resolution=1080*1920&dpi=420&update_version_code=3131&_rticket=1515383230467&ts=1515383231&as=a255ae75bfdb8a6912&cp=e1b7a05ff62e5a94e2&mas=00abe67276168317f730a89cc5d9aa61845e4180ba"

    # url = 'https://hotsoon.snssdk.com/hotsoon/room/6508468404381944579/_fetch_message_polling/'

    url = 'https://api.huoshan.com/hotsoon/room/6508835285743340302/_fetch_message_polling/'

    # url = 'https://hotsoon.snssdk.com/hotsoon/room/6509526829710183171/_fetch_message_polling/'

    # cursor =

    # url = 'https://api.huoshan.com/hotsoon/room/{roomid}/_fetch_message_polling/?cursor={cursor}&user_id=83274563234&live_sdk_version=313&iid=22844387158&device_id=42834931943&ac=wifi&channel=oppo&aid=1112&app_name=live_stream&version_code=313&version_name=3.1.3&device_platform=android&ssmix=a&device_type=ONEPLUS+A5000&device_brand=OnePlus&language=zh&os_api=25&os_version=7.1.1&uuid=99001062553882&openudid=8f64987d7f0e26a4&manifest_version_code=313&resolution=1080*1920&dpi=420&update_version_code=3131&_rticket=1515652206205&ts=1515652207&as=a29540a59fc67a04b7&cp=0668a95bf8755f41e2&mas=0074d5c720028ee7beb31139570cab852be8808cdd'.format(roomid=6509610147810282247, cursor='6509676567374056196_1515652206339' )

    url = 'https://api.huoshan.com/hotsoon/room/6509964672626756356/_fetch_message_polling/?cursor=6509984792543791885_1515724011863&user_id=83274563234&live_sdk_version=313&iid=22844387158&device_id=42834931943&ac=wifi&channel=oppo&aid=1112&app_name=live_stream&version_code=313&version_name=3.1.3&device_platform=android&ssmix=a&device_type=ONEPLUS+A5000&device_brand=OnePlus&language=zh&os_api=25&os_version=7.1.1&uuid=99001062553882&openudid=8f64987d7f0e26a4&manifest_version_code=313&resolution=1080*1920&dpi=420&update_version_code=3131&_rticket=1515724012758&ts=1515724012&as=a225c115fc8e2afcf8&cp=1fefad53cb8f5dc2e2&mas=004b72e5c5e876bb74458240163faf029aa40e7ee0'

    data = {
        # "cursor": '6508868272904243972_1515464005055',
        "cursor": '6509616026429672205_1515638092547',  # room_id + 时间戳(从上个url找)
        "user_id": 83274563234,                         # 用户id固定
        "live_sdk_version": 313,                        # 不用管
        "iid": 22844387158,                             # 不用管
        "device_id": 42834931943,                       # 不用管
        "ac": 'wifi',                                   # 不用管
        "channel": 'oppo',                              # 不用管
        "aid": 1112,                                    # 不用管
        "app_name": 'live_stream',                      # 不用管
        "version_code": 313,                            # 不用管
        "version_name": '3.1.3',                        # 不用管
        "device_platform": 'android',                   # 不用管
        "ssmix": 'a',                                   # 不用管
        "device_type": 'ONEPLUS+A5000',                 # 不用管
        "device_brand": 'OnePlus',                      # 不用管
        "language": 'zh',                               # 不用管
        "os_api": 25,                                   # 不用管
        "os_version": '7.1.1',                          # 不用管
        "uuid": 99001062553882,                         # 不用管
        "openudid": '8f64987d7f0e26a4',                 # 不用管
        "manifest_version_code": 313,                   # 不用管
        "resolution": '1080*1920',                      # 不用管
        "dpi": 420,                                     # 不用管
        "update_version_code": 3131,                    # 不用管
        "_rticket": 1515637389594,                      # 时间戳
        "ts": 1515637390,                               # 时间戳
        "as": 'a295ecc5dea80a2a36',                     # 未知参数(可以扔掉)
        "cp": 'cf89a858ee6750a6e2',                     # 未知参数(可以扔掉)
        "mas": '005fe69644d902a5154acc918f8fe504cb46a0a4a0',    # 未知参数(可以扔掉)
    }
    response = requests.get(url)
    # print(data)

    print(response.content.decode('utf-8'))
    return response.json()


def parse_room():
    data = scraping()
    if data:
        now = data.get('data')
        print(now)


def get_msg_list():
    msg_list = []
    data = scraping()
    if data:
        return msg_list


def onTulingBot(contact, user):
    url = 'http://www.tuling123.com/openapi/api'
    apikey = '7159f3e34c864911ae660501f13a6f37'
    data = contact
    send_data = {
        'key': apikey,
        'info': data,
        'userid': user,
    }
    data = json.dumps(send_data)

    response = requests.post(url=url, params=send_data)
    print(response.data)
    print(type(response.data))
    print(response.type)
    # bot_msg = response.json().get('text')
    # if response.status_code==200:
    #     bot_msg = response.json().get('text')
    #     print(bot_msg)
    # return bot_msg


def get_res():
    response = requests.get(url='http://www.house-book.com.cn/buildslist')
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    # contact = '斗图'
    # onTulingBot(contact, 123456)
    # onTulingBot(content, member.name)
    #
    # while True:
    #     scraping()
    #     time.sleep(5)
    get_res()
    # postman()
    # save_csv()
    # dict = {
    #     '1': 2,
    #     '2': 2,
    #     'key': 3,
    # }
    # print(dict.keys())
    # print(type(dict))

    # url = 'https://now.qq.com/'
    # data = {'num': '120',
    #         'sessionid': 'nKSbF17GWpGR0FBjMPVmyGf7OHdB5lmEf2mavtnc6/1+6rETnKRZ5SGlIOKzXm+9/ObSnoq76YZQrGj3J9ZejIaNY85ZNxUn+zTeLD396WM4I3eSZ8tLon+zD9hK+KEfDml9JaPZDGDIRJ845MmmCA\u003d\u003d'}
    # s = requests.Session()
    # r = s.get(url=url)
