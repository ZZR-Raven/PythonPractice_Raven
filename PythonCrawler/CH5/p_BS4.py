from bs4 import BeautifulSoup
import requests
import re

html = requests.get('https://www.kanunu8.com/book2/10943/').content.decode("gb2312","ignore")

soup = BeautifulSoup(html,'lxml')

useful = soup.find(class_ ='book')
all_ch = useful.find_all('dd')
for dd in all_ch:
    print(dd.string)
#打印出了每章的标题
#第1章 全民公敌(1)
#第2章 全民公敌(2)
# 第3章 全民公敌(3)
# 第4章 全民公敌(4)
# 第5章 全民公敌(5)
# 第6章 全民公敌(6)
# 第7章 全民公敌(7) 
