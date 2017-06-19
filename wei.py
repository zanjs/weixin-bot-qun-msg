# coding: utf-8
''' '''
from __future__ import unicode_literals

import sys
from wxpy import Bot
from wxpy import ensure_one
from wxpy import get_wechat_logger
from flask import Flask
from flask import request

reload(sys)

sys.setdefaultencoding('utf-8')

app = Flask(__name__)



# 初始化机器人
bot = Bot(console_qr=2)

qun_def = '测试服务警报通知'
qun_1 = '测试服务警报通知1'
qun_name = qun_1
by_name = '\n---来自 anla.io 的智能机器人服务'



def init():
    """
    初始化
    """
    # 找到需要接收日志的群 -- `ensure_one()` 用于确保找到的结果是唯一的，避免发错地方
    group_receiver = ensure_one(bot.groups().search(qun_name))

    print group_receiver

    if group_receiver:
        # 指定这个群为接收者
        logger = get_wechat_logger(group_receiver)
        logger.error('监听启动...' + by_name)

    return 'logger'


def sed_qun(msg, qun):
    """
    全消息发送
    """

    # 找到需要接收日志的群 -- `ensure_one()` 用于确保找到的结果是唯一的，避免发错地方
    group_receiver = ensure_one(bot.groups().search(qun))

    print group_receiver

    if group_receiver:
        # 指定这个群为接收者
        logger = get_wechat_logger(group_receiver)
        logger.error(msg + by_name)

    return 'logger'


@app.route("/")
def hello():
    """
    hello console
    """

    return "hello"

@app.route("/wei",methods=['POST', 'GET'])
def wei():
    """
    微信群消息发送
    """
    # msg = request.form['msg']
    msg = request.args.get('msg', '')
    qun = request.args.get('qun', '')
    print msg
    print qun

    return sed_qun(msg, qun)




if __name__ == '__main__':
    app.run()




