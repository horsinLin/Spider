import urllib.request
import urllib.parse

baseurl = "http://www.baidu.com/s?"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
key = input("请输入要搜索的内容:")
# urlencode编码,参数一定要是字典
d = {"wd":key}
d = urllib.parse.urlencode(d)
url = baseurl + d
# print(url)
# 1.构建请求对象
request = urllib.request.Request(url, headers=headers)
# 2.获取响应对象
response = urllib.request.urlopen(request)
# 3.获取响应内容
html = response.read().decode()
print(html)