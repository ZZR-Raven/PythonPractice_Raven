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
url_list.pop(0)
url_count = len(url_list)

for url in url_list:
    real_url = 'https://www.kanunu8.com/book3/7750/'+url
    client.sadd('url_set',real_url)         #set元素不能重复
    # print('\n',real_url)
# print(client.scard('url_set'))


# content_list = []



#                                   xpath testing
url_b = client.spop('url_set')
url_s = str(url_b,encoding='utf-8')
print(url_s)
ch_code = requests.get(str(url_s)).content.decode(encoding = 'GB2312')
with open('text_get.html','w',encoding='utf-8') as txt2:
   txt2.write(ch_code)

selector = etree.HTML(ch_code)
ch_pre = selector.xpath('/html/body/div[@align="center"]/table/tr/td/p/text()')
print(len(ch_pre))
print(ch_pre)


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
