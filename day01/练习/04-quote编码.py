import urllib.request
import urllib.parse

url = "http://www.baidu.com/s?wd="
key = input("请输入要搜索的内容:")
# 编码,拼接URL
key = urllib.parse.quote(key)
fullurll = url + key

headers = "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"

# 1.构建请求对象
request = urllib.request.Request(fullurll)
# 添加User-Agent
request.add_header("User-Agent", headers)
# 2.获取响应对象
response = urllib.request.urlopen(request)
# 3.获取响应内容
html = response.read().decode("utf-8")
print(html)



