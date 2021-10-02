import requests

qq = 'https://qmsg.zendee.cn/send/6af4e501c2fe9492d166baa167e199bb'  # Qmsg酱接口

msg = input()

data = {
    'msg': msg
}

requests.post(qq, data)   # qq推送
