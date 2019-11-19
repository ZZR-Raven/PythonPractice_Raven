'''
由于每层楼都兼顾部分人名变化成百度百科链接
考虑将链接与其他内容分开爬取再合并
'''
import scrapy
import lxml
import requests
import redis
import chardet
from lxml import etree
from scrapy.selector import Selector
import time
import re
from Raven import tqdmRaven


url = 'https://tieba.baidu.com/p/4975393487?pn=1'
xp_eg = '//*[@id="j_p_postlist"]/div[1]/div[2]/div[1]/cc/div[2]/text()'
xp_1 =  '//*[@id="j_p_postlist"]/div['
xp_2 =  ']/div[2]/div[1]/cc/div[2]/text()'
comments = []
ori_code = requests.get(url,re.S).content.decode(encoding = 'UTF-8',errors = 'ignore')

for xp in range(1,26):      # 左闭右开
    # print(xp)
    com_xp_1 = xp_1 + str(xp) + xp_2
    selector = etree.HTML(ori_code)
    comments.append(selector.xpath(com_xp_1))
    print(comments)



