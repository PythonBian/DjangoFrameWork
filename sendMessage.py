
import requests #pip install requests

url = "http://106.ihuyi.com/webservice/sms.php?method=Submit" #来自于文档

#APIID
account = "C42059483"
#APIkey
password = "3a908b6a18a22986bc57d267cfe808b3"

mobile = "13331153360"
content = "您的验证码是：135279。请不要把验证码泄露给其他人。"
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
#构建发送参数
data = {
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}
#开始发送
response = requests.post(url,headers = headers,data=data)
    #url 请求接口路由
    #headers 请求头部
    #data 请求的内容

print(response.content.decode())