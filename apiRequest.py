import requests

req = requests.get("http://127.0.0.1:8000/goods_list_api/1/1/")
result = req.json()
for k,v in result.items():
    print(k)
    print(v)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++")