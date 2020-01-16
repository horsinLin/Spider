import requests

url = "http://www.baidu.com/s?"
headers = {"User-Agent": "Mozilla5.0/"}
s = input("请输入要搜索的内容:")
# get方法params参数必须为字典格式
wd = {"wd" : s}
res = requests.get(url,params=wd,headers=headers)
res.encoding = "utf-8"
print(res.text)