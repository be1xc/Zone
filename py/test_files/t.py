# cxleb
import requests
import re,time
from requests import cookies
from requests.sessions import session


def deepink():
    cookie = (r'X_CACHE_KEY=f386041ad84f8dc17925ca9d25a14e75; Andyt_2132_saltkey=NCdqq6X2; Andyt_2132_lastvisit=1616890719; Andyt_2132_sid=OKpZe8; Andyt_2132_lastact=1616894346%09home.php%09spacecp; Andyt_2132_sendmail=1; Andyt_2132_ulastactivity=ede9AVgbYmpn18%2BraFyDJqFyHXRmP%2Fc%2B25fbzfVstOMR7Qbih1iI; Andyt_2132_auth=5ef2bfvIOXwdj6HYjUP871PDnFeI0eaOtctj2PAm5YwmMz8Oq0POFaumE3vSSruuz3%2FbuxgoGDe7vXgGYkWe9q4RJA; Andyt_2132_lastcheckfeed=83394%7C1616894337; Andyt_2132_lip=223.167.152.14%2C1616894331; Andyt_2132_connect_is_bind=0')
    bbs_url = 'https://sq.wgrid.cn/'
    url_qd1 = 'https://sq.wgrid.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash={}&format=empty'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'cookie': cookie
    }

    def coin():
        main_index = 'https://sq.wgrid.cn/home.php?mod=spacecp&ac=credit&showcredit=1'
        res = requests.get(url=main_index, headers=headers)
        today = re.findall(
            r'银币: </em>(\d*).*&nbsp; <a href="home.p', res.text)[0]
        return int(today)

    tcoin = coin()

    res = requests.get(url=bbs_url, headers=headers)
    cookies = requests.utils.dict_from_cookiejar(res.cookies)

    reqd = re.findall('formhash=(.+?)"', res.text)
    requests.get(url=url_qd1.format(reqd[0]), headers=headers, cookies=cookies)

    url_m = 'https://sq.wgrid.cn/home.php?mod=task&do=apply&id=3'
    requests.post(url=url_m, headers=headers)

    url_fm = 'https://sq.wgrid.cn/home.php?mod=task&do=draw&id=3'
    requests.post(url=url_fm, headers=headers)

    member_url = 'https://sq.wgrid.cn/home.php?mod=space&uid='
    member_list = ('122818', '1359', '96526', '65532', '89848', '41468')

    for i in member_list:
        requests.get(url=member_url+i, headers=headers)
        time.sleep(.5)

    qq = 'https://qmsg.zendee.cn/send/6af4e501c2fe9492d166baa167e199bb'  # Qmsg酱接口
    msg = 'deepink check, coin{}, new{}'.format(coin(), coin()-tcoin)
    data = {
        'msg': msg
    }
    requests.post(qq, data)


def main_handler():
    deepink()


main_handler()
