
import re
import json
import requests
from selenium import webdriver
from lxml import etree
from scrapy.selector import Selector
import scrapy
import lxml
# class smsspider(object):
#     url = 'http://www.scut.edu.cn/sms/'

#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Cookie': 'clwz_blc_pst_WWW=1863413962.20480',
#         'DNT': '1',
#         'Host': 'www.scut.edu.cn',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
#     }

#     def __init__(self):
#         # self.necessary_info = {}
#         # self.url = url
#         # self.get_necessary_id()
#         # self.get_comment()
#         pass

#     def get_source(self,url,headers):
#         return requests.get(url,headers).content.decode(encoding = 'gb2312',errors = 'ignore')

#     # # @staticmethod
#     # def get_necessary_id(self):
#     #     source = self.get_source(self.url,self.headers)
#     #     vid = re.search(r'vid: (\d+)',source).group(1)
#     #     pid = re.search(r'pid: (\d+)',source).group(1)
#     #     self.necessary_info['xid'] = vid
#     #     self.necessary_info['pid'] = pid

#     def get_comment(self):
#         self.source = self.get_source(self.url,self.headers)


# if __name__ == '__main__':
#     spider = smsspider()
#     spider.get_comment()
#     print(spider.source)

# ch_xpath = '//*[@id="pageForm"]/table/tbody/tr[3]/td/table[2]/tbody/text()'
smsurl = 'http://www.scut.edu.cn/sms/'
driver = webdriver.Chrome()
driver.get(smsurl)

input('手动输入账号密码')

# ch_code = requests.get('http://xsgl.7i5q.cas.scut.edu.cn/sms2/homepage.jsp').content.decode(encoding = 'gb2312',errors = 'ignore')
# selector = etree.HTML(ch_code)
# all_info = selector.xpath(ch_xpath)
# print(all_info)
# xpath_score = '//*[@id="pageForm"]/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td'
real_url = []

with open('zhiyu_info.html',encoding='utf-8') as aaa:
    # print(scorelist)
    hhh = aaa.read()
    url_list = re.findall('<td><a href="(.*?)" target=',str(hhh))
    for url in url_list:
        real_url.append('http://xsgl.7i5q.cas.scut.edu.cn' + url)
    
code = requests.post('http://xsgl.7i5q.cas.scut.edu.cn/sms2/student/module/evaluation/studentIntellectualDetail.jsp?evaluationId=10573&classYearId=13').content.decode(encoding = 'utf-8',errors = 'ignore')
print(code)
    # scorelist = re.findall('<td>(\\d.\\d)</td>',str(hhh))
    # print(scorelist)
    # finallist = []
    # i = 0
    # for score in scorelist:
    #     if i%2 == 0:
    #         finallist.append(scorelist[i]) 
    #     i = i + 1
    # print(finallist)
    # with open('list.xlsx')as x:
    #     x.writelines(finallist)
