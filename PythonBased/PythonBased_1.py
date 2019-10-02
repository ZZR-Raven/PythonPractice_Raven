#Python基础知识练习

__author__ = 'Raven'

#输入输出
print('hallo world')
print('I','am','Raven')
print((100**2)%5)#10000
print(100**2%5)#10000
#myname=input('please input your name : ')#括号里运行print
#print(myname)

#数据类型和变量
print(3.6%2)#取模函数支持浮点数
print('i\'m \"ok\"')
print('\\\t\\')
print(r'\\\t\\')#r''的''里面的字符串不转义
print('''line1
line2
line3''')
testor = 1>3 or 3>1
testnot = not 3>1
print('testor = ',testor)
print('testnot = ',testnot)
print(9/3)
print(10/3)
print(10//3)
#   占位
#   %s  字符串
#   %d  整数 
#   %f  浮点数
#   %x  十六进制整数
print('hallo,{0},你的生日是{1}'.format('Raven',1999))

#list 不定长 可修改
testlist = ['a','b','c']
print(len(testlist))
testlist.append('test')
print(testlist)
testlist.pop(3)
testlist.insert(-2,233)#负号索引,最右-1；插入在再左一位！！['a', 233, 'b', 'c']
print(testlist)
testlist_2 = [1,testlist,True]
print(testlist_2)
print(len(testlist_2))#list插入到另一个list只算一个元素

#tuple 不可修改
testtuple = (2) #这是个运算，不是【一个元素的tuple】
print(testtuple)
testtuple_1 = (1,)
print(testtuple_1)#加个逗号才是【一个元素的tuple】
testyuple_2 = ('a',['b','c'])
testyuple_2[1][0] = 'B'#tuple内部的list内元素可变
print(testyuple_2)

#if else
age = 16
#age = input('age = ')
if age >= 18:
    print('adult')
elif age >= 6: #elif = else if in C
    print('teenager')
else:
    print('kids')

#for in
forsum = 0
for forx in [1,3,5,7,9] :
    forsum = forsum + forx*forx
print('forsum = ',forsum)

#while
whilesum = 0
whilen = 0
while whilen < 100 :
    #if whilen > 50 : break 这里插结果会不一样
    whilen = whilen + 2
    if whilen > 50 : 
        break #跳出循环
    if whilen % 4 == 0  : 
        continue#不执行下面语句,继续下一轮循环
    whilesum  = whilesum + whilen
print('whilesum = ',whilesum)

#dict key-value ！key不可变，不可以用list当key
dicttest = {'A':65,'B':66,'C':67}   #定义大括号
dicttest['A'] = 1                   #调用中括号
print(dicttest)
#print(dicttest['D'])直接写会报错
print(dicttest.get('B','wrong'))    #函数小括号
print(dicttest.get('D','wrong'))





