import requests
import json

qq = 'https://qmsg.zendee.cn/send/6af4e501c2fe9492d166baa167e199bb'  # Qmsg酱接口
api_url = 'https://tianqiapi.com/api'  # 免费天气接口

weatherParams = {
    'appid': '19995755',  # 必填
    'appsecret': 'R6UjInwq',  # 必填
    'version': 'v6',  # 必填
    'city': "成都",  # 城市代码，名字，ip三选一，默认ip
}

def main_handler(url, params):
    dataList = []                   # 创建空列表
    res = json.loads(requests.get(url, params).text)       # 提交post
    city = res['city']              # 城市名字
    date = res['date']              # 当前日期
    week = res['week']              # 当前星期
    update = res['update_time']     # 更新时间
    wea = res['wea']                # 天气情况
    tem = res['tem']                # 实时温度
    tem1 = res['tem1']              # 温度上限
    tem2 = res['tem2']              # 温度下限
    hunidity = res['humidity']      # 湿度
    win = res['win']                # 风向
    win_speed = res['win_speed']    # 风力等级
    visibility = res['visibility']  # 能见度
    air = res['air']                # 空气质量
    air_level = res['air_level']    # 空气质量等级
    air_tips = res['air_tips']      # 空气质量描述

    dataList.extend(
        [city, date, week, update, wea, tem, tem1, tem2, hunidity, win, win_speed, visibility, air, air_level,
         air_tips])                 # 向空列表中追加天气内容
    QQPusher(dataList)


def QQPusher(dataList):
    data1 = {
        'msg': '{} {} {}\n{} {}℃ {}～{}℃\n湿度: {}\n{}，{}\n空气质量: {}，{}'.format(
            dataList[0], dataList[3], dataList[2], dataList[4], dataList[5], dataList[6], dataList[7],
            dataList[8], dataList[9], dataList[10], dataList[12], dataList[13])
    }
    requests.post(qq, data1)   # qq推送
    print(data1)

main_handler(api_url, weatherParams)