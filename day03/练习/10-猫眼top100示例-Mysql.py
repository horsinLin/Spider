import requests
import re
import pymysql
import warnings

class maoyanSpider:
    def __init__(self):
        self.baseUrl = "https://maoyan.com/board/4?offset={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36"}
        self.page = 1
        self.proxies = {"HTTP": "36.25.42.108:9999"}
        self.db = pymysql.connect("localhost", "root", "horsin@123", charset="utf8")
        self.cursor = self.db.cursor()

    def getPage(self, url):
        res = requests.get(url, proxies=self.proxies, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)

    def parsePage(self, html):
        p = re.compile('<div class="movie-item-info">.*?data-val=".*?">(.*?)</a>.*?<p class="star">\n(.*?)</p>.*?<p class="releasetime">(.*?)</p>', re.S)
        r_list = p.findall(html)
        self.writeToMysql(r_list)

    def writeToMysql(self, r_list):
        c_db = "create database if not exists spider;"
        u_db = "use spider;"
        c_tab = "create table if not exists maoyan(\
                 id int primary key auto_increment,\
                 name varchar(30),star varchar(150),\
                 releasetime varchar(80)) charset='utf8';"
        warnings.filterwarnings("error")
        warnings.simplefilter("ignore", ResourceWarning)
        try:
            self.cursor.execute(c_db)
        except:
            pass
        self.cursor.execute(u_db)
        try:
            self.cursor.execute(c_tab)
        except:
            pass
        for r_tuple in r_list:
            s_insert = "insert into maoyan(name,star,releasetime) values('%s','%s','%s')"\
                       % (r_tuple[0].strip(), r_tuple[1].strip(), r_tuple[2].strip())
            self.cursor.execute(s_insert)
            self.db.commit()
        print("第 %d 页存入数据库成功!" % self.page)


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