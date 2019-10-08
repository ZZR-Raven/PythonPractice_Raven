from pymongo import MongoClient

client = MongoClient()
database = client.ch6
collection = database.spider
#或 datbase = client[db_name] 变量名
#或 collection = client[col_name]
data_test = {'id':123,'name':'Raven','age':19}

#   插入   
#   insert_one  insert_many 【instead】 of insert
collection.insert_one(data_test)           
more_data = [
    {'id': 2, 'name': '张三', 'age': 10, 'salary': 0},
    {'id': 3, 'name': '李四', 'age': 30, 'salary': -100},
    {'id': 4, 'name': '王五', 'age': 40, 'salary': 1000},
    {'id': 5, 'name': '外国人', 'age': 50, 'salary': '未知'},
]
collection.insert_many(more_data)

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




