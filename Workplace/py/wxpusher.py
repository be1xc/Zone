import requests
import json

msg = '''

    as

'''
url = 'http://wxpusher.zjiecode.com/api/send/message'
header = {
    "Content-type": 'application/json'
}

data = {
  "appToken":"AT_rbjiSEIJ8sFgvSqaNSEfonKf3sZEE9tt",
  "content":msg,
  "contentType":1,#内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown 
  "uids":[
      "UID_oC35v5vJD99VDeEWT18s5QidGsaf"
  ]
}

requests.post(url=url,headers=header,json=data)


