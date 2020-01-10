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
def workOn():
    baseUrl = "https://maoyan.com/board/4?"
    pn = 1
    while True:
        page = (pn - 1) * 10
        offset = {"offset": str(page)}
        offset = urllib.parse.urlencode(offset)
        url = baseUrl + offset
        html = getPage(url)
        filename = "猫眼top100榜第" + str(pn) + "页.html"
        print("正在下载第%d页" % pn)
        writePage(filename, html)
        print("第%d页下载完成" % pn)
        isCon = input("是否继续爬取(y/n)")
        if isCon == "y":
            pn += 1
        elif isCon == "n":
            print("爬取结束,谢谢使用!")
            break
        else:
            print("输入有误,程序停止运行!")

if __name__ == '__main__':
    workOn()