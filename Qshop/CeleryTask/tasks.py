from __future__ import absolute_import
from Qshop.celery import app

@app.task #将普通的函数转换为celery任务
def taskExample():
    print("I am task Example")
    return "I am task Example"

@app.task #将普通的函数转换为celery任务
def add(x,y):
    return x+y

import json
import requests
from Qshop.settings import DING_URL
@app.task
def sendDing(content="hello world",to=None):
    headers = {
        "Content-Type": "application/json",
        "Charset": "utf-8"
    }
    requests_data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": [
            ],
            "isAtAll": True
        }
    }
    if to:
        requests_data["at"]["atMobiles"].append(to)
        requests_data["at"]["isAtAll"] = False
    else:
        requests_data["at"]["atMobiles"].clear()
        requests_data["at"]["isAtAll"] = True
    sendData = json.dumps(requests_data)
    response = requests.post(url=DING_URL, headers=headers, data=sendData)
    content = response.json()
    return content
