from bs4 import BeautifulSoup
import requests
import re

html = requests.get('https://www.kanunu8.com/book2/10943/').content.decode("gb2312","ignore")

soup = BeautifulSoup(html,'lxml')

useful = soup.find('d1')
all_ch = useful.find_all('dd')
for dd in all_ch:
    print(dd.string)
