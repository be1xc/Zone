# -*- coding:utf-8 -*-
import requests
from requests import cookies
from requests.sessions import session

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Referer': 'https://cwv587.com/auth/login'
}
postdata1 = {
	"email": "stuzar@qq.com",
	"passwd": "Liu45.stuzar",
	"geetest_challenge": "e96cbebae4ea6d6c386e6ad9d8c00fef6z",
	"geetest_validate": "df4993fc0167935dfbed7dd1b59b0425",
	"geetest_seccode": "df4993fc0167935dfbed7dd1b59b0425|jordan",
    # "Cookie": "PHPSESSID=6qrr6j1sdnjoo7u49shbu8r4be; ip=a40942fa672d081f760a5d54039faa65; expire_in=1630976345; mtauth=5e2ceba40a7bb123052965a882244271; lang=zh-cn"
}
url = 'https://cwv587.com/auth/login'
a = requests.post(url=url,headers=headers,data=postdata1,verify=False)
# a = requests.post(url=url,headers=headers)


print(a)