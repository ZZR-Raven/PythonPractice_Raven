import requests
import re

#get
html_1 = requests.get('http://www.google.cn')
print('html_1',html_1)
#html_1 <Response [200]>
html_1_bytes = html_1.content   #bytes
#with open('content.txt','w',encoding='utf-8') as txt1:
#    txt1.write(html_1_bytes)
html_1_str = html_1_bytes.decode()
with open('decode_get.txt','w',encoding='utf-8') as txt2:
        txt2.write(html_1_str)

#post
#data = {'key1':'value1','key2':'value2'}
#html_2 = requests.post('http://exrcise.kingname.info/exercise_requests_post',)
html_2 = requests.post('http://www.google.cn').content.decode()
with open('decode_post.txt','w',encoding='utf-8') as txt3:
        txt3.write(html_1_str)
#print(data)

#regular
title = re.search('title>(.*?)<',html_1_str,re.S).group(1)
print(title)
content_list = re.findall('p>(.*?)<',html_1_str,re.S)
print(content_list)
content_str = '\n'.join(content_list)
print(content_str)


