#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re

def main_handler():
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.51 Safari/537.36 Edg/92.0.902.15'
    }
    url = 'https://v1.jinrishici.com/.json'
    res = requests.get(url,headers=headers)
    res = res.json()
    msg = '{} --- {}'.format(res['content'],res['author'])
    qq = 'https://qmsg.zendee.cn/send/6af4e501c2fe9492d166baa167e199bb'
    data = {
        'msg': msg
    }
    requests.post(qq, data)

main_handler()