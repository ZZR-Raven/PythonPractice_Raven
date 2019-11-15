
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
print(temp_source)
num_list = []
num_list = re.findall('evaluationId=(.*?)&amp;classYearId=13',temp_source,re.S)
print(num_list)
# num_list = ['4461', '2911', '10233', '10245', '10246', '10249', '10254', '10257', '7490', '10283', '10285', '10298', '10300', '10303', '10305', '10307', '10334', '10337', '10343', '10348', '10362', '10369', '949', '10379', '10392', '6552', '10400', '10407', '4841', '1319', '10431', '3422', '10450', '1024', '6577', '3375', '10475', '10478', '10723', '6563', '4850', '10893', '10900']

# code = requests.post('http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId=10573&classYearId=13').content.decode(encoding = 'utf-8',errors = 'ignore')
# print(code)

real_url = []
with open('zhiyu.html',encoding='utf-8') as aaa:
    # print(scorelist)
    hhh = aaa.read()
    url_list = re.findall('<td><a href="(.*?)" target=',str(hhh))
    for url in url_list:
        real_url.append('http://xsgl.7i5q.cas.scut.edu.cn' + url)  
    scorelist = re.findall('<td>(\\d.\\d)</td>',str(hhh))
    print(scorelist)
    finallist = []
    i = 0
    for score in scorelist:
        if i%2 == 0:
            finallist.append(scorelist[i]) 
        i = i + 1
    print(finallist)