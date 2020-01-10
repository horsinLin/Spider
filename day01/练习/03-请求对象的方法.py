import urllib.request

url = "http://www.baidu.com/"
headers = "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"

# 1.构建请求对象
request = urllib.request.Request(url)
# 请求对象方法 add_header()
request.add_header("User-Agent", headers)
# 2.获取响应对象
response = urllib.request.urlopen(request)
# get_header() 方法获取 User-Agent
print(request.get_header("User-agent"))
# 获取响应码
print(response.getcode())
print(response.info())