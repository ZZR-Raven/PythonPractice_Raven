#默认参数
def Function_Default(name,gender,age = 19, city = 'Guangzhou'):
    print('name:',name)
    print('gendor = ',gender)
    print('age = ',age)
    print('city: ',city)
Function_Default('Raven','F',city = 'Shaoguan')

#坑
def Function_AddEnd(L=[]):
    L.append('END')
    return L
print(Function_AddEnd([1,2,'a']))
print(Function_AddEnd())#['END']
print(Function_AddEnd())#['END','END'] 默认参数也是个变量，指向对象[]，每次调用都改变了L
def Function_AddEnd_Modified(L = None):
    if L is None:
        L = []
    L.append('END')
    return L
print(Function_AddEnd_Modified())#['END']
print(Function_AddEnd_Modified())#['END']

#可变参数 * + 变量名
def Function_Calc_1(numbers):#需要给一个list或者tuple
    sum = 0
    for n in numbers:
        sum = sum + n*n 
    return sum
print(Function_Calc_1([1,2,3]))#list    []
print(Function_Calc_1((1,2,3)))#tuple   ()
def Function_Calc_2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n 
    return sum

print(Function_Calc_2(1,2,3))#直接写参数
print(Function_Calc_2())#还可以传入 0 个参数
CalcList = [1,2,3]
print(Function_Calc_2(*CalcList))#可以传入list
#*list表示把list的所有元素作为可变参数传入

#关键字参数 **kw
def Function_Keywords(name,age,**kw):
    print('name: ',name,'age:',age,'other',kw)
Function_Keywords('Raven', 19, city = 'Shaoguan')
Function_Keywords('HYY',20,gender = 'M')
#可以组装一个dict作为关键字参数传入{}
KeywordsDict = {'city': 'Shenzhen','job':'Engineer'}
Function_Keywords('Jane',21,**KeywordsDict)

#命名关键字参数 *,变量名,变量名...      【必须传入参数名！！】    
# *后的变量都是命名关键字参数
# *args(可变参数)后的命名关键字参数不再需要特殊分隔符
def Function_Rename_1(name,age,*,city,job):
    print(name,age,city,job)
Function_Rename_1('Jack',24,city = 'Shanghai',job = 'Engineer')
def Function_Rename_2(name,age,*args,city = 'Beijing',job): #可以用默认关键字
    print(name,age,args,city,job)
Function_Rename_2('Jack',24,job = 'Engineer')
Rename_dict = {'gender':'M'}
Function_Rename_2('Jack',24,Rename_dict,job = 'Engineer')
Rename_Tuple = ('gender = M')
Function_Rename_2('Jack',24,Rename_Tuple,job = 'Engineer')
Rename_List = ('m',1,3)
Function_Rename_2('Jack',24,Rename_List,Rename_Tuple,job = 'Engineer')
#Jack 24 (('m', 1, 3), 'gender = M') Beijing Engineer

#参数组合
#参数定义的顺序必须是：必选参数、默认参数、可选参数、命名关键字参数、关键字参数
def Function_Combining_1 (a, b, c = 0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)
Function_Combining_1(1,2,3,'a','b',x=99)
def Function_Combining_2 (a, b, c = 0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)
Function_Combining_2(1,2,'d = 1',d = 1,xyz = None, abc = 233)
#a =  1 b =  2 c =  d = 1 d =  1 kw =  {'xyz': None, 'abc': 233}
Rename_tuple = (1,2,3)
Rename_dict = {'d': 2333,'#':'d'}
Function_Combining_1(*Rename_tuple,**Rename_dict)
Function_Combining_2(*Rename_tuple,**Rename_dict)

#递归函数
#无优化
def Function_Fact(n):
    if n == 1:
        return 1
    return n * Function_Fact(n - 1)
print(Function_Fact(5))
print(Function_Fact(500))
#print(Function_Fact(1000))     
# 堆栈溢出 Traceback (most recent call last)
#尾递归优化
def Function_Fact_Tail(n):
    return Function_Fact_iter(n,1)
def Function_Fact_iter(num,product):
    if num == 1:
        return product
    return Function_Fact_iter(num - 1, num* product)
#print(Function_Fact_Tail(1000))
#Python解释器没有对尾递归做优化，还是会溢出的   -_-||
print(Function_Fact_Tail(500))





