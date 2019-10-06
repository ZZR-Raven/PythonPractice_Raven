import requests
import time
from multiprocess.dummy import Pool


def calc_power2(num):
    return num*num
    
#pool test
p = Pool(3)
origin_num = [x for x in range(10)]
result = p.map(calc_power2,origin_num)
print('0到9的平方分别为',result)

def query(url):
    requests.get(url)

start = time.time()
for i in range(100):
    query('https://baidu.com')
end = time.time()
print('单线程访问百度首页100次 耗时',{end - start})

start = time.time()
url_list = []
for i in range(100):
    url_list.append('https://baidu.com')
pool = Pool(5)
pool.map(query,url_list)
end = time.time()
print('5线程访问百度首页100次 耗时',{end - start})

#单线程访问百度首页100次 耗时 {21.853224754333496}
#5线程访问百度首页100次 耗时 {5.472562074661255}
#10线程访问百度首页100次 耗时 {2.786489248275757}

