import urllib.request
import urllib.parse

# 得到html : 发请求获响应
def getPage(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    return html

# 保存html到本地
def writePage(filename, html):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(html)

# 主函数
def workon():
    name = input("请输入贴吧名:")
    begin = int(input("请输入起始页:"))
    end = int(input("请输入终止:"))
    baseurl = "https://tieba.baidu.com/f?"
    kw = {"kw": name}
    kw = urllib.parse.urlencode(kw)
    for page in range(begin, end+1):
        pn = (page - 1) * 50
        url = baseurl + kw + "&pn=" + str(pn)
        print(url)
        print("正在下载第%d页" % page)
        html = getPage(url)
        filename = "第" + str(page) + "页.html"
        writePage(filename, html)
        print("第%d页下载完成" % page)
        print("*" * 30)

if __name__ == '__main__':
    workon()