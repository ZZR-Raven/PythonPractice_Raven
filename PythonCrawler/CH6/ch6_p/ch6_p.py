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
# with open('title_get.txt','w',encoding='utf-8') as txt1:
#    txt1.write(ori_code)
selector = etree.HTML(ori_code)
url_list = selector.xpath('//tbody/tr/td/a/@href')
print(url_list)
# for url in url_list:
#   client.lpush('url_queue',url)
# print(client.llen('url_queue'))


# selector = etree.HTML(title_code)
# url_list = selector.xpath('/html/body/div[2]/div[2]/div/dl/dd[1]/a')
# for url in url_list:
#   client.lpush('url_queue',url)

# content_list = []
# while client.llen('url_queue') == 0:
#     url = loop('url_queue').decode()
#     source = requests.get(url).content
#     selector = html.fromstring(source)
#     ch_name = selector.xpath('xpath')[0]
#     content_list.append('title':ch_name,'content':'\n'.join(content))
# handler.insert(content_list)
