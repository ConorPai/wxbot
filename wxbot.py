import itchat

@itchat.msg_register([itchat.content.TEXT, itchat.content.SHARING], isGroupChat=True)
def group_reply_text(msg):
    source = msg['FromUserName']

    if msg['Type'] == itchat.content.TEXT:
        print msg
    elif msg['Type'] == itchat.content.SHARING:
        print msg

@itchat.msg_register([itchat.content.PICTURE, itchat.content.VIDEO])
def group_reply_media(msg):
    source = msg['FromUserName']
    msg['Text'](msg['FileName'])

itchat.auto_login()
itchat.run()