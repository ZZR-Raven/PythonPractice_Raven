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
xp = '//div[@class="wrap2"]'

# ori_code = requests.get(url).content.decode(encoding = 'UTF-8',errors = 'ignore')
# with open('new.html','w') as html :
#     html.write(ori_code) 

with open('new.html','r') as html :
    ori_code = html.read()
    print(ori_code)