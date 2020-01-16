import urllib.request

url = "http://www.baidu.com/"

# 1.创建HTTPHandler处理器对象
handler_http = urllib.request.HTTPHandler()
# 2.创建自定义的opener对象
opener = urllib.request.build_opener(handler_http)
# 3.利用opener对象的open方法发请求
req = urllib.request.Request(url)
res = opener.open(req)
print(res.read().decode("utf-8"))