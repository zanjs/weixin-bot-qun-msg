# coding: utf-8
''' '''
from __future__ import unicode_literals

import sys
from wxpy import Bot
from wxpy import ensure_one
from wxpy import get_wechat_logger
import uuid


reload(sys)

sys.setdefaultencoding('utf-8')

def get_mac_address():
    '''mac address '''
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


print get_mac_address()


# 初始化机器人
# bot = Bot(console_qr=2)
# # 找到需要接收日志的群 -- `ensure_one()` 用于确保找到的结果是唯一的，避免发错地方
# group_receiver = ensure_one(bot.groups().search('测试服务警报通知'))

# print group_receiver

# if group_receiver:
#     # 指定这个群为接收者
#     logger = get_wechat_logger(group_receiver)
#     logger.error('打扰大家了，但这是一条重要的错误日志...')




