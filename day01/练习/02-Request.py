import urllib.request

url = "http://www.baidu.com/"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}

# 1.构建请求对象
request = urllib.request.Request(url, headers=headers)
# 2.获取响应对象
response = urllib.request.urlopen(request)
# 3.获取响应对象内容
html = response.read().decode("utf-8")
print(html)

