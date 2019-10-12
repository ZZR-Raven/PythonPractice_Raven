#需要连接resis，检查url_lst是否被清空


import scrapy
import lxml
import requests
import redis
import pymongo
import chardet
from lxml import etree
from scrapy.selector import Selector

#   redis连接
pool = redis.ConnectionPool() 
client = redis.Redis(connection_pool=pool)

#   爬取小说每章节url
ori_code = requests.get('https://www.kanunu8.com/book3/7750/').content.decode(encoding = 'gb2312')
selector = etree.HTML(ori_code)
url_list = selector.xpath('//tbody/tr/td/a/@href')
url_list.pop(0)     #去掉第一个无用网址

#   将url补充成html路径并放入redis的list中
for url in url_list:
    real_url = 'https://www.kanunu8.com/book3/7750/'+url
    client.lpush('url_list',real_url)    

#   先清空目标txt文件防止被重复写入
with open('龙族前传.txt','w',encoding='utf-8') as temp:  #
    temp.truncate()


count = 1
#   爬取小说正文
while client.llen('url_list') != 0 :
    # 从redis list里面获取并删除一个网址(byte),转化成str
    url_b = client.rpop('url_list')
    url_s = str(url_b,encoding='utf-8')

    # get回来的byte自动查找解码格式chardet.detect
    ch_byte = requests.get(url_s).content
    charset_dict = chardet.detect(ch_byte)
    charset = charset_dict['encoding']
    print('charset = ',charset)

    # decode 记得ignore
    ch_code = ch_byte.decode(encoding = charset,errors = 'ignore')
    selector = etree.HTML(ch_code)

    # 要从源码看，chrome直接复制xpath可能有多余的误导标签
    ch_pre = selector.xpath('/html/body/div[@align="center"]/table/tr/td/p/text()')
    
    with open('龙族前传.txt','a',encoding='utf-8') as txt2:  
        txt2.writelines(ch_pre)
        print('ch%sdone'%count)
        count = count + 1



