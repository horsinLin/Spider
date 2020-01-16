import requests
import re
import pymongo

class LianJiaSpider:
    def __init__(self):
        self.page = 1
        self.baseurl = "https://sz.lianjia.com/ershoufang/pg"
        self.headers = {"User-Agent": "Mozilla5.0/"}
        self.proxies = {"HTTP": "222.240.184.126:8086"}
        self.conn = pymongo.MongoClient("localhost", 27017)
        self.db = self.conn.Lianjia # 库名
        self.myset = self.db.housePrice  # 表名

    # 获取页面
    def getPage(self, url):
        res = requests.get(url, proxies=self.proxies, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)

    # 用正则解析页面
    def parsePage(self, html):
        p = re.compile('<div class="positionInfo">.*?data-el="region">(.*?)</a>.*?<div class="totalPrice">.*?<span>(.*?)</span>', re.S)
        r_list = p.findall(html)
        self.writeToMongo(r_list)

    # 保存到Mongodb
    def writeToMongo(self, r_list):
        for r_tuple in r_list:
            d = {"houseName": r_tuple[0].strip(),
                 "housePrice": float(r_tuple[1].strip())*10000}
            self.myset.insert(d)
        print("存入数据库成功")


    # 主函数
    def run(self):
        while True:
            print("正在爬取 %d 页" % self.page)
            # 拼接 URL
            url = self.baseurl + str(self.page) + "/"
            self.getPage(url)
            print("第 %d 页爬取成功" % self.page)

            c = input("是否继续爬取(y/n)?")
            if c.strip().lower() == "y":
                self.page += 1
            else:
                print("爬取结束,谢谢使用!")
                break

if __name__ == '__main__':
    spider = LianJiaSpider()
    spider.run()
