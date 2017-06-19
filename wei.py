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

bot.messages.max_history = 0

qun_def = '测试服务警报通知'
qun_1 = '测试服务警报通知2'
qun_2 = '日志消息'
qun_name = qun_2
by_name = '\n\n🤖 来自 anla.io 的智能机器人服务\n\n👺 消息来自 By '


def sed_qun(msg, qun, auth):
    """
    群消息发送
    msg 要发送的消息
    qun 要发送到的群
    """

    # 找到需要接收日志的群 -- `ensure_one()` 用于确保找到的结果是唯一的，避免发错地方
    searchV = bot.groups().search(qun)
    print searchV
    if not searchV:
        errMsg = '未搜索到要发送的群: ' + qun
        print errMsg
        bot.file_helper.send(errMsg)

        return 'null'
    if len(searchV) > 1:
        return 'list > 2'

    group_receiver = ensure_one(searchV)

    print group_receiver

    del searchV

    if group_receiver:
        # 指定这个群为接收者
        logger = get_wechat_logger(group_receiver, 'api')

        logger.warning(msg + by_name + auth)

        del group_receiver
    else:
        return 'err：group_receiver'

    del logger

    return 'ok : '+msg

def init():
    """
    初始化服务
    """
    sed_qun('服务监听启动' + by_name, qun_name, 'serve')


@app.route("/")
def hello():
    """
    hello console
    """

    return "hello"

@app.route("/wei", methods=['POST', 'GET'])
def wei():
    """
    微信群消息发送
    """
    # msg = request.form['msg']
    # msg = request.args.get('msg', '')
    # qun = request.args.get('qun', '')
    # auth = request.arge.get('auth', '')

    bodyVal = request.values

    msg = bodyVal.get('msg')
    qun = bodyVal.get('qun')
    auth = bodyVal.get('auth')

    print msg
    print qun
    print auth

    if not qun:
        return '群名称 is null'

    if not msg:
        return '消息 is null'

    if not auth:
        return '发布者 is null'

    # if auth.strip() == '':
    #     return '发送者 is null'
    sed_qun(msg, qun, auth)

    return msg+qun+auth



if __name__ == '__main__':
    # init()
    app.run()
