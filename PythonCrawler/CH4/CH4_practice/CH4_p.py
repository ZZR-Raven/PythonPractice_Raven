#练习 https://www.kanunu8.com/book2/10943/

#使用request获取网页源代码
#正则表达式提取内容
#文件操作

import os
import re
import time
import requests
from multiprocess.dummy import Pool

#title_code = requests.post('https://www.kanunu8.com/book2/10943/').content.decode()
#with open('title_post.txt','w',encoding='utf-8') as txt1:
#    txt1.write(title_code)
#                                   405 Not Allowed 手动cv

with open('title_post.txt','r',encoding='utf-8') as txt1:
    title_all = txt1.read()
    title_code = re.findall('<dl><dt>正文</dt><dd>(.*?)<div class="clear"></div>',title_all,re.S)
    #print(title_code)     这里是目录和链接

real_url = []
ch_url = re.findall('a href="(.*?)">',str(title_code),re.S)
#print(ch_url)      这里是每章的url
ch_name = re.findall('.html">(.*?)</a></dd><dd><a',str(title_code),re.S)
#print(ch_name)     这里是每章的名字
for url_test in ch_url:
    real_url.append('https://www.kanunu8.com/book2/10943/' + str(url_test))  #每章网址

def save(chapter,article):
    #如果没有龙族5文件夹就建一个,如果有就不建
    os.makedirs('龙族5',exist_ok=True)
    with open (os.path.join('龙族5',chapter+'.txt'),'w',encoding='utf-8') as f :
        f.writelines(article)
#num = 65
#for url in real_url:
#for num in range(65,)
num = 65
while (num <= len(real_url)):
    print("request start")
    code_html = requests.get(real_url[num])
    code_bytes = code_html.content
    print("decode start")
    code_str = code_bytes.decode("gb2312","ignore")
    ch = ch_name[num]
    ar = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<p>',code_str,re.S)
    save(ch,ar)
    print('第%d章打印完成'%num)
    num = num + 1

#code_html = requests.get(real_url[0])
#code_bytes = code_html.content
#print(code_bytes)
#code_str = code_bytes.decode("gb2312","ignore")     #居然是GB2312编码的
#print(code_str)
#ch = ch_name[0]
#ar = re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<p>',code_str,re.S)
















