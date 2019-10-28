
import re
import json
import requests
from selenium import webdriver
from lxml import etree
from scrapy.selector import Selector
import scrapy
import lxml

# with open('html_get.txt','w',encoding='utf-8') as temp:  
#     temp.truncate()

smsurl = 'http://www.scut.edu.cn/sms/'
driver = webdriver.Chrome()
driver.get(smsurl)
input('手动输入账号密码')

# header = {
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#             'Accept-Encoding': 'gzip, deflate',
#             'Accept-Language': 'zh-CN,zh;q=0.9',
#             'Cache-Control': 'max-age=0',
#             'Connection': 'keep-alive',
#             'Cookie': 'clwz_blc_pst_WWW=1863413962.20480',
#             'DNT': '1',
#             'Host': 'www.scut.edu.cn',
#             'Upgrade-Insecure-Requests': '1',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
#         }

temp = driver.get('http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/evaluation/intellectualList.jsp')
temp_source = driver.page_source
# print(temp_source)
num_list = []
num_list = re.findall('evaluationId=(\\d*)&classYearId=13',temp_source,re.S)
print(num_list)


# target_url = 'http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/evaluation/intellectualList.jsp'
# session = requests.Session()
# source = session.get(target_url).content.decode(encoding = 'utf-8',errors = 'ignore')
# print(type(source))
# # print(type(source_))
# with open('html_get.txt','w') as h1:
#     h1.write(str(source))



real_url = []






# with open('zhiyu_info.html',encoding='utf-8') as aaa:
#     # print(scorelist)
#     hhh = aaa.read()
#     url_list = re.findall('<td><a href="(.*?)" target=',str(hhh))
#     for url in url_list:
#         real_url.append('http://xsgl.7i5q.cas.scut.edu.cn' + url)
    
# code = requests.post('http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId=10573&classYearId=13').content.decode(encoding = 'utf-8',errors = 'ignore')
# print(code)
