# coding:utf-8

import urllib.request
import json
import re
import requests
import codecs

# request head
head = {'User-Agent': \
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}

# 查找并返回网页vid，测试用的，实际程序没用到
def find_vid(web_adress):
    html_text = urllib.request.urlopen(web_adress).read()
    tag1 = re.findall(r'var .+?};', str(html_text))
    tag = ''
    for eco in tag1:
        tag2 = re.findall(r'vid: "(.+?)",', eco)
        if not tag2 == []:
            tag = tag2[0]
    return tag

# 查找并返回网页的comment_id
def find_comment_id(web_adress):
    html_text = urllib.request.urlopen(web_adress).read()
    tag = re.findall(r'"comment_id":"(\d+)"', str(html_text))
    return tag[0]


web_orig = r'http://v.qq.com/detail/q/qviv9yyjn83eyfu.html' # 《花千骨》首页
html_text = urllib.request.urlopen(web_orig).read() # 读取html源代码
# 在html文件中找到58季的vid
tag1 = re.findall(r'<a href=".+?vid=.+?</a>', str(html_text))
tag2 = list()
for i in tag1:
    if r'episodeNumber' in i:
        tag2.append(i)
vid = list()
for i in tag2:
    vid = vid + re.findall(r'vid=(.+?)"', i)

# 把评论存在文档里
file = codecs.open('comment.txt', 'w+','utf-8')
for i in vid:
    web_find_comment_id = r'http://ncgi.video.qq.com/fcgi-bin/video_comment_id?otype=json&op=1&vid=' + i
    comment_id = find_comment_id(web_find_comment_id)
    web_json = 'http://coral.qq.com/article/' + comment_id + '/comment?commentid=0&reqnum=20'
    jscontent = requests.get(web_json, headers=head).content
    jsDict = json.loads(jscontent.decode())
    jsData = jsDict['data']
    comments = jsData['commentid']
    for each in comments:
        # print(each['content'].encode('utf-8').decode())
        file.write(str(each['content']))
        file.write('\n')

file.close()
