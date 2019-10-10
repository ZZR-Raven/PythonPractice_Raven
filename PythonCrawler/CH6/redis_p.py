import redis

#也可以
pool = redis.ConnectionPool() 
client = redis.Redis(connection_pool=pool)
#client = redis.StrictRedis()
client.set('name', 'raven')     #添加
#print (client.get('name'))      #获取 字节类型 b

#client.mset = (num1 = 'q',num2 = 'w')
num_dict = {'num1':1,'str1':'1'}    
client.mset (num_dict)
# print(client.mget('num1'))
# print(client.mget('str1'))
#返回都是字节类型

client.lpush('ch6',233)
client.rpush('ch6',9999)
print(client.llen('ch6'))

