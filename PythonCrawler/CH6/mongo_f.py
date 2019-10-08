from pymongo import MongoClient

client = MongoClient()
database = client.ch6
collection = database.spider


#   查找
#   find(条件，返回字段)
#   find_one(条件，返回字段)
content_find = collection.find()
content_find = collection.find({'age':29})
content_find = collection.find({'age':29},{'_id':0})
#print(content_find)
#<pymongo.cursor.Cursor object at 0x00000279C3E3FEF0>
#可迭代的pyMongo对象，可以被for或者列表生成式展开
content_find = [x for x in collection.find({'age':19})]
print(content_find)
print(len(content_find))
#会越来越长，每次运行都插了一遍
