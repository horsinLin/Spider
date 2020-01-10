import urllib.request

url = "http://www.baidu.com/"
# 发起请求并获取响应对象
response = urllib.request.urlopen(url)
# 响应对象的read()方法获取响应内容
# read()得到的是 bytes 类型
html = response.read().decode("utf-8")
print(html)
