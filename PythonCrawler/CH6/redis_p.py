import redis

#client = redis.Redis()
#远程
#client = redis.StrictRedis(host = '',port = 2739,password = 123456)

#将123放到列表ch6的左侧
#client.lpush('ch6',123)
#print(client.llen('ch6'))


pool = redis.ConnectionPool()
r = redis.Redis(connection_pool=pool)
r.set('name', 'zhangsan')   #添加
print (r.get('name'))   #获取


