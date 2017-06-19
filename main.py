#coding=utf-8
''' jing '''

import itchat
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

itchat.auto_login(enableCmdQR=2)

itchat.send('hello, 你好',toUserName='filehelper')

chatroomList = itchat.get_chatrooms()

# print chatroomList

print itchat.search_friends()
print '+++'
print itchat.search_friends(name='anla.io')

itchat.run()
