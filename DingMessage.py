import json
import requests

url = "https://oapi.dingtalk.com/robot/send?access_token=739cdc134a4021dfe673a5ba5b73e772af3da26d94c246a93d9d16fdf7f8658e"

headers = {
    "Content-Type": "application/json",
    "Charset": "utf-8"
}

requests_data = {
    "msgtype": "text",
    "text": {
        "content": "饿了吗？来个士力架"
    },
    "at": {
        "atMobiles": [
        ],
        "isAtAll": True
    }
}

sendData = json.dumps(requests_data)

response = requests.post(url = url,headers = headers, data = sendData)

content = response.json()

print(content)