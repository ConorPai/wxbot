# coding=utf-8

import itchat
from itchat.content import *

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#创建消息记录日志文件
logfile = open('./log.txt', 'a')

#消息数组转字符串
def dict2string(dict):

    res = ''
    for key in dict:

        if res is not '':
            res += '`|`'

        res += key + ':' + str(dict[key])

    return res

#群组消息记录(文本、位置、名片、通知、分享)
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def group_reply_text(msg):

    logfile.write(dict2string(msg) + '\n')
    logfile.flush()

    #被@之后自动回复
    if msg['IsAt']:
        itchat.send(u'@%s\u2005我收到了你的消息: %s' % (msg['ActualNickName'], msg['Content']), msg['ToUserName'])

#个人消息记录(文本、位置、名片、通知、分享)
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def group_reply_text(msg):

    logfile.write(dict2string(msg) + '\n')
    logfile.flush()

#群组文件下载(图片、录音、文件、视频)
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def group_reply_media(msg):
    msg['Text'](msg['FileName'])

#个人文件下载(图片、录音、文件、视频)
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def group_reply_media(msg):
    msg['Text'](msg['FileName'])

itchat.auto_login(True)
itchat.run()