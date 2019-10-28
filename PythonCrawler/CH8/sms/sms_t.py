
# import re
# import json
import requests
# from selenium import webdriver
# from lxml import etree
# from scrapy.selector import Selector
# import scrapy
# import lxml

smsurl = 'http://www.scut.edu.cn/sms/'
# driver = webdriver.Chrome()
# driver.get(smsurl)

# input('手动输入账号密码')

# header = {
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Accept-Language': 'zh-CN,zh;q=0.9',
#             'Cache-Control': 'max-age=0',
#             'Connection': 'keep-alive',
#             # 'Content-Length': '365',
#             'Content-Type': 'application/x-www-form-urlencoded',
#             'Cookie': 'JSESSIONID=8081BCF40750B46F8B4BD9DDE4CDA8BA; Language=zh_CN; clwz_blc_pst_SSO=79767242.38943',
#             'DNT': '1',
#             'Host': 'sso.scut.edu.cn',
#             # 'Origin': 'https://sso.scut.edu.cn',
#             # 'Referer': 'https://sso.scut.edu.cn/cas/login?service=http%3A%2F%2Fxsgl.7i5q.cas.scut.edu.cn%3A80%2Fsms2%2Fhomepage.jsp',
#             'Upgrade-Insecure-Requests': '1',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'

# }

header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'clwz_blc_pst_WWW=1863413962.20480',
            'DNT': '1',
            'Host': 'www.scut.edu.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
        }



session = requests.Session()
source = session.get(smsurl,headers=header,verify=False).content.decode(encoding = 'gb2312',errors = 'ignore')
print(source)



# encoding = 'gb2312',errors = 'ignore'

# real_url = []

# with open('zhiyu_info.html',encoding='utf-8') as aaa:
#     # print(scorelist)
#     hhh = aaa.read()
#     url_list = re.findall('<td><a href="(.*?)" target=',str(hhh))
#     for url in url_list:
#         real_url.append('http://xsgl.7i5q.cas.scut.edu.cn' + url)
    
# code = requests.post('http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId=10573&classYearId=13').content.decode(encoding = 'utf-8',errors = 'ignore')
# print(code)
#     # scorelist = re.findall('<td>(\\d.\\d)</td>',str(hhh))
#     # print(scorelist)
#     # finallist = []
#     # i = 0
#     # for score in scorelist:
#     #     if i%2 == 0:
#     #         finallist.append(scorelist[i]) 
#     #     i = i + 1
#     # print(finallist)
#     # with open('list.xlsx')as x:
#     #     x.writelines(finallist)
