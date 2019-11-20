'''
由于每层楼都兼顾部分人名变化成百度百科链接
考虑将链接与其他内容分开爬取再合并
'''
import scrapy
import lxml
import requests
import redis
import chardet
from lxml import etree
from scrapy.selector import Selector
import time
import re
from Raven import tqdmRaven


url = 'https://tieba.baidu.com/p/4975393487?pn=1'
xp_eg = '//*[@id="j_p_postlist"]/div[1]/div[2]/div[1]/cc/div[2]/text()'

xp_1 = '//*[@id="j_p_postlist"]/div['
xp_2 = ']/div[2]/div[1]/cc/div[2]/text()'
xp_3 = ']/div[2]/div[1]/cc/div[2]/a/text()'
comments_1 = []
comments_2 = []
# rpl_tem = ''
# rpl_com = ''
rpl_com = []
ori_code = requests.get(url,re.S).content.decode(encoding = 'UTF-8',errors = 'ignore')

for num in range(1,35):      # 左闭右开
    # print(xp)
    com_xp_1 = xp_1 + str(num) + xp_2
    com_xp_2 = xp_1 + str(num) + xp_3
    selector = etree.HTML(ori_code)
    temp_com = selector.xpath(com_xp_1)
    word = selector.xpath(com_xp_2)
    if len(word) > 0 :                    # 不为空
        for wnum in range(0,len(word)):
            if wnum == 0 :
                rpl_com.append(str(temp_com).replace('\', \'',word[wnum],1))   
            else :
                rpl_com.append(str(rpl_com[wnum-1]).replace('\', \'',word[wnum],1))   
        print(rpl_com[wnum])
        com = re.findall('(\d*\.+.*)',str(rpl_com[wnum]))
        comments_1.append(com)
    else :
        com = re.findall('(\d*\.+.*)',str(temp_com))
        if len(com) > 0 :
            comments_1.append(com)   
    rpl_com = []
    
    
    
print(comments_1)

[["1.路鸣泽对路明非说他是最想杀死黑王的人。']"],
 ["2.零对路明非感到熟悉。']"], 
 ["3.小魔鬼具有打通现实与梦境的能力，还送了诺诺烟花，酒德麻衣与此同时问mint俱乐部要了烟花。']"], 
 ["4.康斯坦丁走出浴池对路明非说，他找的不是路明非。']"], 
 ["5.路明非打死康斯坦丁的时候犹豫了一下，打偏了。']"], 
 ["6.第一次与路鸣泽交换生命的时候路鸣泽说几千年了，你什么事都答应我，唯独这件事不答应，犹犹豫豫（大概这个意思）']"], 
 ["7.路明非没有杀了诺顿，只是用色欲重伤了他，然后酒德麻衣一枪KO。']"], 
 ["8.昂热没有找到诺顿的龙骨。']"],
 ["9.昂热对神秘古尸苏醒这件事从没提过。']"], 
 ["10.路明非3e考试时画的最后一张画，昂热看了一眼说了句好久不见就烧了。']"], 
 ["11.鸣泽认为明妃和诺诺最后没有好的结果。']"],
 ["12.明非的父母一直没有路面，只送了两封信。从此音讯全无。']"], 
 ["13.路明非爆掉楚子航是说了句逆臣。']"], 
 ["14.楚爸s+级血统，在一座小城里看着尼伯龙根。']"], 
 ["15.楚爸的后备箱里有奥丁想要的东西。']"], 
 ["16.楚爸认识奥丁。']"], 
 ["17.楚爸时间零影响不到奥丁。']"], 
 ["18.派来抢学校文件的麦当劳叔叔不是和卡塞尔一伙的，也不是肯德基先生']"], 
 ["19.昂热因为当年的夏之哀悼想要复仇的是整个龙族，每条龙都算。']"], 
 ["20.汉高把混血中的未来寄托到了肯德基先生那里。']"], 
 ["21.昂热对路明非说他父母生他的事纯属瞎掰。']"], 
 ["22.路明非战斗力低因为没觉醒。']"], 
 ["23.和EVA在一起的邋遢大叔是肯德基先生。']"], 
 ["24.酒德麻衣和耶梦加德打仗时站在他后面的不是路明非，是路鸣泽。']"], 
 ["25.小魔鬼是白王或黑王。']"]]
