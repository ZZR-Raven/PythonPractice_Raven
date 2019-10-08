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

#[{'_id': ObjectId('5d9c4cc11f39b302ae08e5d8'), 'id': 123, 'name': 'Raven', 'age': 19}, {'_id': ObjectId('5d9c4cdb8ee140708bf5bf11'), 'id': 123, 'name': 'Raven', 'age': 19}, {'_id': ObjectId('5d9c4f7a6009cd1249b9ac20'), 'id': 123, 'name': 'Raven', 'age': 19}, {'_id': ObjectId('5d9c50ca489510c580616b44'), 'id': 123, 'name': 'Raven', 'age': 19}, {'_id': ObjectId('5d9c50ddb1a1828c88e52d91'), 'id': 123, 'name': 'Raven', 'age': 19}, {'_id': ObjectId('5d9c512fafa15a656ff6cf6f'), 'id': 123, 'name': 'Raven', 'age': 19}, {'_id': ObjectId('5d9c515a1bfa669a3a7da97d'), 'id': 123, 'name': 'Raven', 'age': 19}, {'_id': ObjectId('5d9c5170ae21e3753daa31ed'), 'id': 123, 'name': 'Raven', 'age': 19}]
#8




