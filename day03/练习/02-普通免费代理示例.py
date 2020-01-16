import requests

url = "http://www.taobao.com"
proxies = {"HTTP":"222.240.184.126:8086"}
headers = {"User-Agent": "Mozilla5.0/"}

res = requests.get(url, proxies=proxies, headers=headers)
res.encoding = "utf-8"
print(res.text)