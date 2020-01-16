import urllib.request

url = "http://www.baidu.com/"
proxy = {"HTTP": "120.83.110.247:9999"}
# 1.创建Handler
proxy_handler = urllib.request.ProxyHandler(proxy)
# 2.创建自定义opener
opener = urllib.request.build_opener(proxy_handler)
# 3.利用open方法发请求
req = urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))
