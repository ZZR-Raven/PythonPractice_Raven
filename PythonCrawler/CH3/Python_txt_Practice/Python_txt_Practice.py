import os

with open('test.txt',encoding = 'utf-8') as txt1:
    content_list = txt1.readlines()
    print(txt1.tell)
    txt1.seek(0,0)
    content_str = txt1.read()
    print(txt1.tell)
print('readlines',content_list)
#print('read',len(content_str))
#readlines已经把文件指针移到文件最后面了
print('read',content_str)

with open('new.txt','w',encoding='utf-8') as txt2:
    txt2.write('我写了一个踢叉踢文件\n')
    txt2.writelines(['第一段话\n','第二段话\n','第三段话\n'])



