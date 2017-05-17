# coding=utf-8

import itchat
from itchat.content import *

import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

logfile = open('./log.txt', 'a')

def dict2string(dict):

    res = ''
    for key in dict:

        if res is not '':
            res += '`|`'

        res += key + ':' + str(dict[key])

    return res

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def group_reply_text(msg):

    logfile.write(dict2string(msg) + '\n')
    logfile.flush()

    if msg['IsAt']:
        itchat.send(u'@%s\u2005我收到了你的消息: %s' % (msg['ActualNickName'], msg['Content']), msg['ToUserName'])

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def group_reply_text(msg):

    logfile.write(dict2string(msg) + '\n')
    logfile.flush()

@itchat.msg_register([itchat.content.PICTURE, itchat.content.VIDEO], isGroupChat=True)
def group_reply_media(msg):
    msg['Text'](msg['FileName'])

@itchat.msg_register([itchat.content.PICTURE, itchat.content.VIDEO])
def group_reply_media(msg):
    msg['Text'](msg['FileName'])

itchat.auto_login()
itchat.run()