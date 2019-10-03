from collections.abc import Iterable 
from functools import reduce  # py3
#reduce函数在python3的内建函数移除了，放入了functools模块



#函数式编程
#函数名也是变量
#变量可以指向函数
#高阶函数   函数名也可以作为参数传入另一个函数

#map
def Calc(x):
    return x*x
List_1 = list(range(1,11))
print(List_1)
#List_2 = map(Calc,List_1)
print(list(map(Calc,List_1)))
#map不能直接打印,需要转换成list对象

#reduce
#reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)
def add_reduce(x,y):
    return x+y
print(reduce(add_reduce,[1,2,3,4,6,7,9]))
#序列变整数
def fn(x,y):
    return x*10 + y
print(reduce(fn,[1,4,6,2,8,0]))
def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
#字符串转数字
print(reduce(fn,map(char2num,'14785')))



