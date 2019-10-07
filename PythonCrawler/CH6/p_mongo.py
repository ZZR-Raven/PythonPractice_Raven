from pymongo import MongoClient

client = MongoClient()
database = client.ch6
collection = database.spider
#或 datbase = client[db_name] 变量名
#或 collection = client[col_name]
data_test = {'id':123,'name':'Raven','age':19}
collection.insert(data_test)











