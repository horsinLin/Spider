# 创建一个库testsipder
# 创建一张表 t1 (id int)
# 在 表中插入一条数据 id=1
import pymysql

db = pymysql.connect("localhost", "root", "horsin@123", charset="utf8")

cursor = db.cursor()

cursor.execute("create database testspider;")
cursor.execute("use testspider;")
cursor.execute("create table t1(id int);")
cursor.execute("insert into t1 values(1);")

db.commit()
cursor.close()
db.close()