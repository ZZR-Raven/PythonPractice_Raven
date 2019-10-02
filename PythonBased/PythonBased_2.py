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

#可变参数 *
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

#命名关键字参数





