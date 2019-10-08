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

#   条件查询
#   大于        $gt
#   小于        $lt
#   大于等于    $gte
#   小于等于    $lte
#   等于        $eq
#   不等于      $ne
content_find = collection.find({'age':{'$gte':29,'$lte':40}})


#   查询
content_find = collection.find({'age':{'$gte':29,'$lte':40}}).sort('age',1)
content_find = collection.find({'age':{'$gte':29,'$lte':40}}).sort('age',-1)

#   更新
collection.update_one({'age':20},{'$set':{'name':'another name'}})
#第一个符合条件 age 20 的更新name 为 another name
collection.update_many({'age':20},{'$set':{'age':'30'}})
#所有符合条件 age 20 的更新age 为 30

#   删除
collection.delete_many({'age':30})
collection.delete_one({'name':'外国人'})

#    返回列中所有元素（除去重复）不删除
print(collection.distinct('name'))



