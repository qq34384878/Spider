#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 15:46
# @Author  : Leo
# @Mail    : leo@1201.us
# @File    : bot.py
# @Software: PyCharm
import time

import talk
from qqbot import QQBotSlot as qqbotslot, qqbotsched, RunBot


@qqbotslot
def onQQMessage(bot, contact, member, content):
    print(content)
    if '@ME' or 'bot' or '机器人' in content:
        # result = talk.talk(content, contact.qq).encode('utf-8')
        # bot.SendTo(contact, '' + result)
        bot.SendTo(contact, talk.talk(content, 1234))
        time.sleep(5)



@qqbotsched(hour='18', minute='00')
def mytask(bot):
    gl = bot.List('group', '东湖赏梅')
    if gl is not None:
        for group in gl:
            bot.SendTo(group, '同学们，下班啦啦啦啦啦啦！！！')


if __name__ == '__main__':
    RunBot()