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
# print(arr6)
# print(arr6.shape,arr6.dtype)        # (5,) float64  
# arr6.dtype = 'float32' 
# print(arr6)
# print(arr6.shape,arr6.dtype)        # (10,) float32
# arr6.dtype = 'float16' 
# print(arr6)
# print(arr6.shape,arr6.dtype)        # (20,) float16
# arr6.dtype = 'float' 
# print(arr6)
# print(arr6.shape,arr6.dtype)        # (5,) float64
# arr6.dtype = 'int64' 
# print(arr6)
# print(arr6.shape,arr6.dtype)        # (5,) int64    变成了无穷大

arr7 = np.array([[1,2,3],[4,6,7]])    # ndarray 类型才可以进行数组乘法操作
# print(arr7 * arr7)
# print(arr7 - arr7)
# print(99*arr7)
# print(1/arr7)
# print(arr7 ** 0.5)

# print(arr7)
# [[1 2 3]
#  [4 6 7]]
# print(arr6[2:4])
# print(arr7[1,2])    # a number
# print(arr7[1:2])    # [[4 6 7]]

arr8 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr8[:2,1:])
# [[2 3]
#  [5 6]]
print(arr8[:,:1])
# [[1]
#  [4]
#  [7]]
arr8[:,:1] = 0
print(arr8[:,:1])
# [[0]
#  [0]
#  [0]]







