import urllib.request
import urllib.parse

baseurl = "https://tieba.baidu.com/f?"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}

name = input("请输入贴吧名:")
begin = int(input("请输入起始页:"))
end = int(input("请输入终止页:"))

# url进行编码
kw = {"kw": name}
kw = urllib.parse.urlencode(kw)
# 写循环拼接url,发请求获响应,写入本地
for page in range(begin,end+1):
    # 拼接URL
    pn = (page - 1) * 50
    url = baseurl + kw + "&pn=" + str(pn)
    # 发请求,获取响应
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    # 写文件保存到本地
    filename = "第" + str(page) + "页.html"
    with open(filename, "w", encoding="utf-8") as f:
        print("正在下载第%d页" % page)
        f.write(html)
        print("第%d页下载完成" % page)
        print("*" * 30)
