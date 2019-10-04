import os
with open('test.txt',encoding = 'utf-8') as txt1:
    content_list = txt1.readlines()
    content_str = txt1.read()
print('readlines',content_list)
print('read',len(content_str))

