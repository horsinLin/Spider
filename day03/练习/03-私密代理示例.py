import requests

url = "http://www.taobao.com/"
headers = {"User-Agent": "Mozilla5.0/"}
proxies = {"http": "http://309435365:szayclhp@114.67.228.126:16819"}

res = requests.get(url, proxies=proxies, headers=headers)
res.encoding = "utf-8"
print(res.text)