from collections.abc import Iterable 
from functools import reduce  # py3
#reduce函数在python3的内建函数移除了，放入了functools模块
import functools

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
def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digits[s]
    return reduce(fn,map(char2num,s))
print((str2int('3456789765')))

#filter 过滤器
#从3开始的奇数列    生成器
def _odd_iter():
    n = 1
    while True:
        n = n +2
        yield n
#筛选出与n取模都不为0的数，返回true/false
def _not_divisible(n):
    return lambda x: x % n > 0
#素数生成器
def primes():
    yield 2
    it = _odd_iter()#初始序列
    while True:
        n = next (it)
        yield n
        it = filter(_not_divisible(n),it)
for n in primes():
    if n < 100 :
        print(n)
    else :
        break

#sorted
print(sorted([23,-27,57,-98,99,-278],key = abs))
print(sorted(['a','hg','BH','YG',' ','.']))
#[' ', '.', 'BH', 'YG', 'a', 'hg']

#闭包   返回函数不能引用会改变的变量！
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
#f1,f2,f3 = count()
#print(f1())
#print(f2())
#print(f3())
#结果全是9  【返回函数】引用的【变量】i，三个函数都返回是变量i是3，结果全都是9
def count_1 ():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
#f1,f2,f3=count_1()
#print(f1())
#print(f2())
#print(f3())
#Possible unbalanced tuple unpacking with sequence defined at line 90: left side has 3 label(s), right side has 0 value(s)
#print('fi:',f1)
#print('f1_list:',list(f1))
#for i in f1:
#    print('elem:',i,'result:',i())

#匿名函数 lambda
def lambda_test(x,y):
    return lambda : x*x + y+y

#装饰器 decorator
def now():
    print('2019-10-04')
f = now
f()
print(now.__name__)
print(f.__name__)
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def log_now():
    print('2019.10.04')
log_now()
#等价于
f_log = log(now)
f_log()
#decorator本身需要传入参数，要写隔返回decorator的高阶函数
def log_text(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log_text ('execute')
def now_log_text():
    print('2019/10/04')
now_log_text()
#等价于 now_log_text = log_text('execute')(now_log_text)
#先执行 log('execute')，
#返回decorator，
#再调用返回函数，参数是函数now_log_text，
#最终返回wrapper

###############################
#使用functools模块
#import functools
def log_functools(text):
    def decorator(func):
        @functools.wraps(func)  ################################    记得加这句
        def wrapper(*args,**kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
###############################

#偏函数 functools.partial 
#固定一个函数的某些参数，设置默认值，返回一个新函数
int2 = functools.partial(int, base = 2)
print(int2('1000000'))
print(int2('1000000',base = 10))
print(int2('1000000',base = 8))

