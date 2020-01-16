import pymongo

# 创建连接对象
conn = pymongo.MongoClient("localhost", 27017)
# 创建数据库对象
db = conn.testpymongo
# 利用数据库对象创建集合对象
myset = db.t1
# 插入一条文档
myset.insert({"name": "Tom"})
