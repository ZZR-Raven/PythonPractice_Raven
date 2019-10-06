#import multiprocess
from multiprocess.dummy import Pool

def calc_power2(num):
    return num*num
    
p = Pool(3)
origin_num = [x for x in range(10)]
result = p.map(calc_power2,origin_num)
print('0到9的平方分别为',result)






