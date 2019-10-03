from collections.abc import Iterable 
import os

#高级特性

#切片 Slice 跟matlab差不多
Slice_List = list(range(100)) #是0到99哦
print(Slice_List)
print(Slice_List[10:20])
print(Slice_List[-30:-5])
print(Slice_List[20:40:3])#20开始每3取1到40
Slice_Tuple = tuple(range(20,40))
print(Slice_Tuple)
print(Slice_Tuple[::3])#     ::3
print('qwertuio'[::2])

#迭代 for in
#from collections.abc import Iterable 
#判断对象是否可迭代
print(isinstance('asdfg',Iterable))
print(isinstance(1234,Iterable))
#enumerate 把list变成 索引—元素
for i,value in enumerate(['a','b','c']):
    print(i,value)
#   0 a
#   1 b
#   2 c

#列表生成式 List Comprehensions 
#从一个list生成另一个list 简洁！
#   eg：生成[1*1,2*2,...,10*10]
#   way 1
LC_1 = []
for i in range(1,11):
    LC_1.append(i*i)
print(LC_1)
#   way 2
LC_2 = [i*i for i in range(1,11)]
print(LC_2)
#两层循环   可以一起写
print([ m + n for m in 'ABC' for n in 'XYZ'])
print([d for d in os.listdir('.')])
#['PythonBased_1.py', 'PythonBased_2.py', 'PythonBased_3.py']
LC_dict = {'X':'A','y':'b','Z':'C'}
for k,v in LC_dict.items():
    print(k,'=',v)
print([k + '=' + v for k,v in LC_dict.items()])# + 连接起来成字符串

#生成器 generator
#把列表生成器的[]变()
#保存的是算法，用next()计算出下一个元素的值
generator_1 = (x*x for x in range(1,11))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
#超出会溢出
#print(next(generator_1))
for n in generator_1:
    print(n)
#并不会打印东西，这个generator已经被迭代完了
for n in (x*x for x in range(1,11)):
    print(n)
#写一个斐波那契数列
#a, b = b, a + b 等价于 tuple(b,a+b) a = tuple[0], b = tuple[1]
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n +1
    return 'done'
fib (20)
#把它变成generator
#只需要把print变成yield
#函数运行到return或者最后一句就返回
#generator函数遇到next执行，遇到yield返回，再次执行时从yield处继续执行
def fib_generator(max):
    n,a,b = 0,0,1
    while n < max:
        yield(b)
        a, b = b, a + b
        n = n +1
    return 'done'
for n in fib_generator(10):
    print(n)
#next yield
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)
#odd()
#next(odd())
#next(odd())
o = odd()
next(o)
next(o)
next(o)
#next(o)    会溢出

#迭代器 Iterator
print(isinstance('asdfg',Iterable))
print(isinstance(1234,Iterable))




