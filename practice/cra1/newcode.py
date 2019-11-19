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
rpl_tem = ''
rpl_com = ''
ori_code = requests.get(url,re.S).content.decode(encoding = 'UTF-8',errors = 'ignore')

for num in range(1,35):      # 左闭右开
    # print(xp)
    com_xp_1 = xp_1 + str(num) + xp_2
    com_xp_2 = xp_1 + str(num) + xp_3
    selector = etree.HTML(ori_code)
    temp_com = selector.xpath(com_xp_1)
    word = selector.xpath(com_xp_2)
    if len(word) > 0 :
        for wnum in range(0,len(word)):
            rpl_tem = str(temp_com).replace('\', \'',word[wnum],wnum+1)
            rpl_com = rpl_tem
            print(rpl_com)
    rpl_com = rpl_tem
    com = re.findall('(\d*\.+.*)',str(rpl_com)) 
    if len(com) > 0 :                # 不为空
        comments_1.append(com)
    
    



print(comments_1)
# print(comments_2)

# [['            本人现在在这里为大家把龙一到龙四的东西疑点都梳理一下，然后并对他们进行推测，预判五的内容和每个人的身份。'], ['
#           1.', '对', '说他是最想杀死黑王的人。'], ['            2.零对', '感到熟悉。'], ['            3.小魔鬼具有打通现实与梦
# 境的能力，还送了诺诺', '，', '与此同时问mint', '要了烟花。'], ['            4.', '走出浴池对', '说，他找的不是路明非。'], ['
#          5.', '打死', '的时候犹豫了一下，打偏了。'], ['            6.第一次与', '交换生命的时候路鸣泽说几千年了，你什么事都答应
# 我，唯独这件事不答应，犹犹豫豫（大概这个意思）'], ['            7.', '没有杀了诺顿，只是用色欲重伤了他，然后', '一枪KO。'], ['
#            8.', '没有找到', '的龙骨。'], ['            9.', '对神秘古尸苏醒这件事从没提过。'], ['            10.', '3e考试时画
# 的最后一张画，', '看了一眼说了句好久不见就烧了。'], ['            11.鸣泽认为', '和', '最后没有好的结果。'], ['            12.
# 明非的父母一直没有路面，只送了两封信。从此音讯全无。'], ['            对于龙1的疑点设悬就是这些，龙2的后续会发。'], ['
#    大家跟帖啊，别让我单飞！！！'], ['            顶一下！'], ['            补充一下，13.', '爆掉', '是说了句逆臣。'], ['
#      龙二开始。'], ['            14.楚爸s+级血统，在一座小城里看着尼伯龙根。'], ['            15.楚爸的后备箱里有', '想要的东西
# 。'], ['            16.楚爸认识', '。'], ['            17.楚爸时间零影响不到', '。'], ['            18.派来抢学校文件的', '不是
# 和', '一伙的，也不是', '先生'], ['            19.', '因为当年的夏之哀悼想要复仇的是整个龙族，每条龙都算。'], ['            20.
# 汉高把混血中的未来寄托到了', '先生那里。']]
# [[], ['路鸣泽', '路明非'], ['路明非'], ['烟花', '酒德麻衣', '俱乐部'], ['康斯坦丁', '路明非'], ['路明非', '康斯坦丁'], ['路鸣泽
# '], ['路明非', '酒德麻衣'], ['昂热', '诺顿'], ['昂热'], ['路明非', '昂热'], ['明妃', '诺诺'], [], [], [], [], ['路明非', '楚子
# 航'], [], [], ['奥丁'], ['奥丁'], ['奥丁'], ['麦当劳叔叔', '卡塞尔', '肯德基'], ['昂热'], ['肯德基']]
