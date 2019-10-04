# 正则表达式基本符号
# . 代表任意一个字符
# * 代表前面的子表达式（包括 . ）， 0 到无限次
# ? 代表前面的子表达式（包括 . * ） 0 或 1 次

#提取数字 \d*
str1 = '第一个数786543567，第二个数75643245，第三个数876543567'
str1_n = '''第一个数786543567，
第二个数756\n43245，        
第三个数876543567'''        
#忽略换行符，但不会连起来，数字会被拆开，只爬到换行符前面的内容

#提取内容 () 小括号 
str2 = '我密码是：34567asdfg你记下'
# :.*?      ==  :34567asdfg你
# :(.*)?你  ==  34567asdfg

import re

#findall 以列表形式返回所有满足要求的字符串
#re.findall(pattern,string,flags = 0)
num_str1 = re.findall('数(\\d*)',str1)  #\\代表普通反斜杠
print (num_str1)
fre_str1 = re.findall('第.个数',str1)
print(fre_str1)
all_str1 = re.findall('(第.个数)(\\d*)',str1)
print(all_str1)
#[('第一个数', '786543567'), ('第二个数', '75643245'), ('第三个数', '876543567')]
all_str1_n = re.findall('(第.个数)(\\d*)',str1_n,re.S)
print(all_str1_n)

#search
all_search = re.search('(第.个数)(\\d*)',str1)
print(all_search)
print(all_search.group())   #括号的全部
print(all_search.group(1))  #第一部分()
print(all_search.group(2))  #第二部分()

# (.*) (.*?) 区别
# (.*) 
# (.*?)     符合的最短字符串
str_3 = '我的微博密码是123456，QQ密码是qwerty，银行卡密码是567890，记住它们'
without_question_mark = re.findall('密码是(.*)，',str_3)
with_question_mark = re.findall('密码是(.*?)，',str_3)      #记得加限定符号（，），前后限定
print('without_question_mark :',without_question_mark)
print('with_question_mark :',with_question_mark)

