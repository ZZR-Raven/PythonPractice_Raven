import re
import csv

with open('dragon5.txt','r',encoding='utf-8') as f:
    source_temp = f.read()
    source = source_temp#.decode()    

result_list = [] 
username_list = re.findall('username=".*?"',source,re.S)
content_list = re.findall('j_d_post_content ">(.*?)<"',source,re.S)
#正则表达式解决不了

print(username_list)
print(content_list)

#for i in range(len(username_list)):
    #result = {'username':username_list[i],
    #         'content':content_list[i]}
    #result_list.append(result)



