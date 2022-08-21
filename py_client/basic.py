import requests

endpoint = "https://httpbin.org/anything"

res = requests.get(endpoint, json={"data": "Data Here..."})
res_json = res.json()
res_text = res.text


print(res_json)
# print(res_json['headers'])