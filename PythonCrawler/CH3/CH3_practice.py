import re
import csv

with open('tieba_long5.txt','r',encoding='utf-8') as f:
    source = f.read()    

result_list = [] 
username_list = re.findall('username=".*?"',source,re.S)
content_list = re.findall('j_d_post_content ">(.*?)<"',source,re.S)

print(username_list)
print(content_list)

#for i in range(len(username_list)):
    #result = {'username':username_list[i],
    #         'content':content_list[i]}
    #result_list.append(result)



