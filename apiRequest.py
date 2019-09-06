import requests

# req = requests.get("http://127.0.0.1:8000/goods_list_api/1/1/")
# result = req.json()
# for k,v in result.items():
#     print(k)
#     print(v)
#     print("+++++++++++++++++++++++++++++++++++++++++++++++++")

# req = requests.post("http://127.0.0.1:8000/goods/")
# result = req
# print(result)

import json

result = json.dumps({"a":1}) #将字典转换为json字符串
print(type(json.loads(result))) #将json字符串转换为字典