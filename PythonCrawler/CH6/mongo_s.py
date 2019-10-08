from pymongo import MongoClient

client = MongoClient()
database = client.ch6
collection = database.spider

content_find = collection.find({'age':{'$gte':29,'$lte':40}}).sort('age',1)
content_find = collection.find({'age':{'$gte':29,'$lte':40}}).sort('age',-1)




