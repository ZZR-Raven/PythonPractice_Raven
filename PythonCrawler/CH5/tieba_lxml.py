#//*[@id="post_content_103878045411"]
#https://tieba.baidu.com/p/4975393487?pn=1

import lxml.html
import requests

with open('tieba_long5.txt','r',encoding='utf-8') as f:
    source_temp = f.read()
    source = lxml.html.fromstring(source_temp)
    #data = source.xpath('//*[@id="post_content_103878045411"]')[0]
    #            7.路明非没有杀了诺顿，只是用色欲重伤了他，然后酒德麻衣一枪KO。
    data = source.xpath('//*[@id="j_p_postlist"]/div[8]/div[2]/div[1]')[0]
    #                                    该楼层疑似违规已被系统折叠 隐藏此楼查看此楼            7.路明非没有杀了诺顿，只是用色欲重伤了他，然后酒
    #德麻衣一枪KO。
    info = data.xpath('string(.)')
    print(info)


