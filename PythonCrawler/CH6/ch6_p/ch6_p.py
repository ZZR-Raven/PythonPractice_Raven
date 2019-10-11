import scrapy
import lxml
import requests
import redis
import pymongo
from lxml import etree
from scrapy.selector import Selector

pool = redis.ConnectionPool() 
client = redis.Redis(connection_pool=pool)

ori_code = requests.get('https://www.kanunu8.com/book3/7750/').content.decode(encoding = 'GB2312')
with open('title_get.html','w',encoding='utf-8') as txt1:
    txt1.write(ori_code)
selector = etree.HTML(ori_code)
url_list = selector.xpath('//tbody/tr/td/a/@href')
url_list.pop(0)

for url in url_list:
    real_url = 'https://www.kanunu8.com/book3/7750/'+url
    client.lpush('url_list',real_url)    
    # print(real_url) 

count = 1
while client.llen('url_list') != 0 :
    # 从redis list里面获取并删除一个网址
    url_b = client.rpop('url_list')
    url_s = str(url_b,encoding='utf-8')
    if count <= 4:
        ch_code = requests.get(url_s).content.decode(encoding = 'GB2312')
    else:       #这个沙雕网站前7章跟后面不是同一种编码格式
        ch_code = requests.get(url_s).content.decode(encoding = 'gbk')
    selector = etree.HTML(ch_code)
    #要从源码看，chrome直接复制xpath可能有多余的误导标签
    ch_pre = selector.xpath('/html/body/div[@align="center"]/table/tr/td/p/text()')
    #print(ch_pre)
    with open('龙族前传.txt','a',encoding='utf-8') as txt2:  #
        txt2.writelines(ch_pre)
        print('ch%sdone'%count)
        count = count + 1



# while client.scard('url_set') == 0:
    # 从set里面取一个网址
    # url = client.spop('url_set')
    # ch_code = requests.get(url).content.decode(encoding = 'GB2312')
    # selector = etree.HTML(ch_code)
    # ch_pre = selector.xpath('//tbody/tr/td/text')
    # print(ch_pre)
    # selector = html.fromstring(source)
    # ch_name = selector.xpath('xpath')[0]
    # content_list.append('title':ch_name,'content':'\n'.join(content))
# handler.insert(content_list)
