#cxleb
import requests
import re
import datetime
from requests import cookies
from requests.sessions import session
import time

def kxd():
    cookie = r"G1NZ_2132_saltkey=NHhdX63C; G1NZ_2132_lastvisit=1628910793; G1NZ_2132_atarget=1; G1NZ_2132_client_token=58757A62D6ED0007C27F4D537849A970; G1NZ_2132_connect_is_bind=1; G1NZ_2132_connect_uin=58757A62D6ED0007C27F4D537849A970; G1NZ_2132_nofavfid=1; G1NZ_2132_smile=5D1; G1NZ_2132_client_created=1630373085; G1NZ_2132_auth=d247GxAnCLr3gMufEr2qkeU+ZgOK7p3pJ5yZugEgGV8fMuvTSXs5t12Cf04+GE/xUKbDKPIsy60bGLIpD3FpNaFMUA; G1NZ_2132_connect_login=1; G1NZ_2132_forum_lastvisit=D_47_1628914482D_36_1629894458D_37_1629894509D_42_1630373187D_38_1630460712; G1NZ_2132_visitedfid=46D38D42D36D37D47; G1NZ_2132_sid=m9SolV; G1NZ_2132_lip=139.155.16.10,1630944033; G1NZ_2132_popadv=a:0:{}; G1NZ_2132_dsu_amupper=DQo8c3R5bGU+DQoucHBlcndibSB7cGFkZGluZzo2cHggMTJweDtib3JkZXI6MXB4IHNvbGlkICNDRENEQ0Q7YmFja2dyb3VuZDojRjJGMkYyO2xpbmUtaGVpZ2h0OjEuOGVtO2NvbG9yOiMwMDMzMDA7d2lkdGg6MjAwcHg7b3ZlcmZsb3c6aGlkZGVufQ0KLnBwZXJ3Ym0gLnRpbWVze2NvbG9yOiNmZjk5MDA7fQ0KLnBwZXJ3Ym0gIGF7ZmxvYXQ6cmlnaHQ7Y29sb3I6I2ZmMzMwMDt0ZXh0LWRlY29yYXRpb246bm9uZX0NCjwvc3R5bGU+DQoNCjxkaXYgY2xhc3M9InBwZXJ3Ym0iIGlkPSJwcGVyd2JfbWVudSIgc3R5bGU9ImRpc3BsYXk6IG5vbmUiID4NCjxBIEhSRUY9InBsdWdpbi5waHA/aWQ9ZHN1X2FtdXBwZXI6cHBlcmxpc3QiIHRhcmdldD0iX2JsYW5rIj7mn6XnnIvnrb7liLDmjpLooYw8L0E+DQo8c3Ryb25nPue0r+iuoeetvuWIsDxzcGFuIGNsYXNzPSJ0aW1lcyI+MTIwPC9zcGFuPuasoTwvc3Ryb25nPjxicj4NCg0KPHN0cm9uZz7ov57nu63nrb7liLA8c3BhbiBjbGFzcz0idGltZXMiPjI8L3NwYW4+5qyhPC9zdHJvbmc+PGJyPg0KDQo8c3Ryb25nPuS4iuasoeetvuWIsDogPHNwYW4gY2xhc3M9InRpbWVzIj4yMDIxLTA5LTAxIDA3OjU3OjQ5PC9zcGFuPjwvc3Ryb25nPg0KPC9kaXY+DQo=; G1NZ_2132_myrepeat_rr=R0; G1NZ_2132_ulastactivity=c341oTl38hWxr2EJeWWBmMoH436XBHvXcGsMJIJNHOj4qoqRhaIl; PHPSESSID=69k32pf0435507gon0ngmu5j93; G1NZ_2132_lastcheckfeed=18383|1630976913; G1NZ_2132_checkfollow=1; G1NZ_2132_sendmail=1; G1NZ_2132_checkpm=1; G1NZ_2132_lastact=1630976937	index.php	"
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
                'cookie': cookie
            }
    url = 'https://www.kxdao.net/plugin.php?id=dsu_amupper&ppersubmit=true&formhash=1cabcefa'
    requests.get(url=url,headers=headers)

def deepink():
    cookie = (r'X_CACHE_KEY=f386041ad84f8dc17925ca9d25a14e75; Andyt_2132_saltkey=NCdqq6X2; Andyt_2132_lastvisit=1616890719; Andyt_2132_sid=OKpZe8; Andyt_2132_lastact=1616894346%09home.php%09spacecp; Andyt_2132_sendmail=1; Andyt_2132_ulastactivity=ede9AVgbYmpn18%2BraFyDJqFyHXRmP%2Fc%2B25fbzfVstOMR7Qbih1iI; Andyt_2132_auth=5ef2bfvIOXwdj6HYjUP871PDnFeI0eaOtctj2PAm5YwmMz8Oq0POFaumE3vSSruuz3%2FbuxgoGDe7vXgGYkWe9q4RJA; Andyt_2132_lastcheckfeed=83394%7C1616894337; Andyt_2132_lip=223.167.152.14%2C1616894331; Andyt_2132_connect_is_bind=0')
    bbs_url = 'https://sq.wgrid.cn/'
    url_qd1 = 'https://sq.wgrid.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash={}&format=empty'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'cookie': cookie
    }
    res = requests.get(url=bbs_url,headers=headers)
    print(res)
    cookies = requests.utils.dict_from_cookiejar(res.cookies)

    reqd = re.findall('formhash=(.+?)"',res.text)
    requests.get(url=url_qd1.format(reqd[0]),headers=headers,cookies=cookies)

    url_m = 'https://sq.wgrid.cn/home.php?mod=task&do=apply&id=3'
    requests.post(url=url_m,headers=headers)

    url_fm = 'https://sq.wgrid.cn/home.php?mod=task&do=draw&id=3'
    requests.post(url=url_fm,headers=headers)

def main_handler():
    kxd()
    # deepink()

main_handler()