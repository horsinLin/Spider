import requests

url = "https://www.12306.cn/index/"
headers = {"User-Agent": "Mozilla5.0/"}

res = requests.get(url, verify=False, headers=headers)
res.encoding = "utf-8"
print(res.text)