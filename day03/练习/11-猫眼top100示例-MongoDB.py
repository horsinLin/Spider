import requests
import re
import pymongo

class maoyanSpider:
    def __init__(self):
        self.baseUrl = "https://maoyan.com/board/4?offset={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
        self.page = 1
        self.proxies = {"HTTP": "36.25.42.108:9999"}
        self.conn = pymongo.MongoClient("localhost", 27017)
        self.db = self.conn.maoyan
        self.myset = self.db.movies

    def getPage(self, url):
        res = requests.get(url, proxies=self.proxies, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<div class="movie-item-info">.*?data-val=".*?">(.*?)</a>.*?<p class="star">\n(.*?)</p>.*?<p class="releasetime">(.*?)</p>', re.S)
        r_list = p.findall(html)
        self.writeMongoDB(r_list)

    def writeMongoDB(self, r_list):
        for r_tuple in r_list:
            d = {
                "name": r_tuple[0].strip(),
                "star": r_tuple[1].strip(),
                "releasetime": r_tuple[2].strip()
            }
            self.myset.insert(d)
        print("存入mongodb数据库成功!")


    def workOn(self):
        while True:
            page = (self.page - 1) * 10
            # https: // maoyan.com / board / 4?offset = 10
            url = self.baseUrl.format(page)
            print("开始爬取第 %d 页" % self.page)
            self.getPage(url)
            c = input("是否继续爬取下一页(y/n)?")
            if c == "y":
                self.page += 1
            else:
                print("感谢使用!")
                break

if __name__ == '__main__':
    spider = maoyanSpider()
    spider.workOn()