
# -*- coding: utf8 -*-

import requests
import json
import time

# 填写cookie即可运行
'''
1、浏览器登入哔哩网站
2、访问 http://api.bilibili.com/x/space/myinfo
3、F12看到cookie的值粘贴即可
'''
cookies = "innersign=0; buvid3=D01E6C70-26D1-7F8A-4B3E-AF694377012293016infoc; b_lsid=6F532863_17D92E0019E; bsource=search_baidu; _uuid=91E174F7-9D81-95EC-8310A-10A26A3438171093803infoc; buvid_fp=D01E6C70-26D1-7F8A-4B3E-AF694377012293016infoc; sid=bpprokgs; fingerprint=bb5a106e90abf283f44ad8b4942150e5; buvid_fp_plain=CF29A948-AA02-4FBE-B219-75D7027F2338148821infoc; SESSDATA=b011f146%2C1654398712%2C31183%2Ac1; bili_jct=33e3381b50a8ffb68fa83a8829564c6d; DedeUserID=509156215; DedeUserID__ckMd5=1b7f6ec21c42a180; i-wanna-go-back=1; b_ut=6"

def extract_cookies(cookies):
    global csrf
    cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
    csrf = cookies['bili_jct']
    return cookies

# 银币数

def getCoin():
    cookie = extract_cookies(cookies)
    url = "http://account.bilibili.com/site/getCoin"
    r = requests.get(url, cookies=cookie).text
    j = json.loads(r)
    money = j['data']['money']
    return money

# 个人信息

def getInfo():
    global uid
    url = "http://api.bilibili.com/x/space/myinfo"
    cookie = extract_cookies(cookies)
    r = requests.get(url, cookies=cookie).text
    print(r)
    j = json.loads(r)
    uid = j['data']['mid']
    name = j['data']['name']
    level = j['data']['level']
    current_exp = j['data']['level_exp']['current_exp']
    next_exp = j['data']['level_exp']['next_exp']
    sub_exp = int(next_exp)-int(current_exp)
    days = int(int(sub_exp)/65)
    coin = getCoin()
    msg = "Welcome! Current level is "+str(level) + " ,Current experience are " + \
        str(current_exp)+",Not far from upgrading "+str(sub_exp) + \
        " ,need "+str(days)+" days"+"Remaining silver coins are "+str(coin)
    print(msg)

# 推荐动态

def getActiveInfo():
    url = "http://api.bilibili.com/x/web-interface/archive/related?aid=" + \
        str(7)
    cookie = extract_cookies(cookies)
    r = requests.get(url, cookies=cookie).text
    j = json.loads(r)
    return j

# 投币 分享5次

def Task():
    j = getActiveInfo()
    data = j['data']
    coin_count = 0
    for i in range(0, len(data)):
        bvid = data[i]['bvid']
        aid = data[i]['aid']
        print(str(bvid)+' -- '+str(aid))
        if coin_count < 5:
            coin_code = tocoin(bvid)
            if coin_code == -99:
                return
        toshare(aid)
        time.sleep(3)
        if coin_code == 1:
            coin_count = coin_count+1
        if coin_count == 5:
            break
        print('----------------------')

# 投币函数
def tocoin(bvid):
    coinNum = getCoin()
    if coinNum == 0:
        print('not enough coin !')
        return -99
    url = "http://api.bilibili.com/x/web-interface/coin/add"
    data = {
        'bvid': bvid,
        'multiply': 1,
        'select_like': 1,
        'csrf': csrf
    }
    cookie = extract_cookies(cookies)
    r = requests.post(url, data=data, cookies=cookie).text
    j = json.loads(r)
    code = j['code']
    print("code="+str(code))
    if code == 0:
        print(str(bvid)+' toaddcoin successful !')
        return 1
    else:
        print(str(bvid)+' toaddcoin failed!')
        return 0

# 分享视频

def toshare(rid):
    url = "https://api.vc.bilibili.com/dynamic_repost/v1/dynamic_repost/share"
    data = {
        'uid': 0,
        'type': 8,
        'share_uid': 0,
        'content': 'testing!',
        'rid': rid,
        'csrf': csrf
    }
    cookie = extract_cookies(cookies)
    r = requests.post(url, data=data, cookies=cookie).text
    j = json.loads(r)
    code = j['code']
    dynamic_id = j['data']['dynamic_id']
    if code == 0:
        print('share successful!')
    else:
        print('share failed!')
    time.sleep(2)
    todelshare(dynamic_id)

# 删除动态

def todelshare(dynamic_id):
    url = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/rm_dynamic"
    data = {
        'dynamic_id': dynamic_id,
        'csrf': csrf
    }
    cookie = extract_cookies(cookies)
    r = requests.post(url, data=data, cookies=cookie).text
    j = json.loads(r)
    code = j['code']
    if code == 0:
        print('share delete successful!')
    else:
        print('share delete failed!')

def run():
    getInfo()
    Task()

run()