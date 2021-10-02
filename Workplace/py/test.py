import requests
import re

cookie = r'X_CACHE_KEY=f386041ad84f8dc17925ca9d25a14e75; Andyt_2132_saltkey=NCdqq6X2; Andyt_2132_lastvisit=1616890719; Andyt_2132_sid=OKpZe8; Andyt_2132_lastact=1616894346%09home.php%09spacecp; Andyt_2132_sendmail=1; Andyt_2132_ulastactivity=ede9AVgbYmpn18%2BraFyDJqFyHXRmP%2Fc%2B25fbzfVstOMR7Qbih1iI; Andyt_2132_auth=5ef2bfvIOXwdj6HYjUP871PDnFeI0eaOtctj2PAm5YwmMz8Oq0POFaumE3vSSruuz3%2FbuxgoGDe7vXgGYkWe9q4RJA; Andyt_2132_lastcheckfeed=83394%7C1616894337; Andyt_2132_lip=223.167.152.14%2C1616894331; Andyt_2132_connect_is_bind=0'
print(1)
bbs_url = 'https://sq.wgrid.cn/'
print(2)

url_qd1 = 'https://sq.wgrid.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash={}&format=empty'
print(3)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'cookie': cookie
}
print(4)

# res = requests.get(url=bbs_url,headers=headers)
# cookies = requests.utils.dict_from_cookiejar(res.cookies)

# reqd = re.findall('formhash=(.+?)"',res.text)
# ccc= requests.get(url=url_qd1.format(reqd[0]),headers=headers,cookies=cookie)
# print(ccc.text)

# 申请任务 finish
## 接任务连接
url_m = 'https://sq.wgrid.cn/home.php?mod=task&do=apply&id=3'
print(5)

a = requests.post(url=url_m,headers=headers)
print(6)


## 领取任务奖励连接
url_fm = 'https://sq.wgrid.cn/home.php?mod=task&do=draw&id=3'
requests.post(url=url_fm,headers=headers)

# if '今日已签' in ccc.text:
#     content = 'checked'
# else:
#     content = 'aaa'
print(a.text)

