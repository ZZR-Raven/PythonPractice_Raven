import numpy as np


data1 = [6,7.5,8,0,9]
arr1 = np.array(data1)
# print(arr1)

data2 = ([1,2,3,4],[4,6,7,9,])
arr2 = np.array(data2)
# print(arr2)
# print(arr2.ndim,arr2.shape)

arr3 = np.zeros((3,7,5))
# print(arr3)

arr4 = np.empty((2,5))      #浮点数
# print(arr4)

arr5 = np.arange(0,17)      #0到16 左闭右开
# print(arr5)

arr6 = np.random.random(5)
print(arr6)
print(arr6.shape,arr6.dtype)        # (5,) float64  
arr6.dtype = 'float32' 
print(arr6)
print(arr6.shape,arr6.dtype)        # (10,) float32
arr6.dtype = 'float16' 
print(arr6)
print(arr6.shape,arr6.dtype)        # (20,) float16
arr6.dtype = 'float' 
print(arr6)
print(arr6.shape,arr6.dtype)        # (5,) float64
arr6.dtype = 'int64' 
print(arr6)
print(arr6.shape,arr6.dtype)        # (5,) int64    变成了无穷大






