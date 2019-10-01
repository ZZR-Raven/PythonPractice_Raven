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
if age >= 18:
    print('adult')
elif age >= 6: #elif = else if in C
    print('teenager')
else:
    print('kids')










