import requests
import re
import pymysql
import warnings

class LianJiaSpider:
    def __init__(self):
        self.page = 1
        self.baseurl = "https://sz.lianjia.com/ershoufang/pg"
        self.headers = {"User-Agent": "Mozilla5.0/"}
        self.proxies = {"HTTP": "222.240.184.126:8086"}
        self.db = pymysql.connect("localhost", "root",
                                  "horsin@123", charset="utf8")
        self.cursor = self.db.cursor()

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
        self.writeToMysql(r_list)

    # 保存到mysql
    def writeToMysql(self, r_list):
        c_db = "create database if not exists spider;"
        u_db = "use spider;"
        c_tab = "create table if not exists lianjia(\
                 id int primary key auto_increment, \
                 name varchar(30),\
                 price decimal(20,2))charset=utf8;"
        warnings.filterwarnings("error")
        try:
            self.cursor.execute(c_db)
        except Warning:
            pass
        self.cursor.execute(u_db)
        try:
            self.cursor.execute(c_tab)
        except Warning:
            pass

        # r_list : [("置地逸轩", "240"),(),()]
        for r_tuple in r_list:
            s_insert = "insert into lianjia(name,price) values('%s','%s')"\
                       %(r_tuple[0].strip(), float(r_tuple[1].strip())*10000)
            self.cursor.execute(s_insert)
            self.db.commit()
        print("第 %d 页存入数据库成功!" % self.page)


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
