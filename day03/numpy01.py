import numpy as np

a = np.array([[2,3],[5,2]])
print(a)

d= np.array([2,3,4,5,6])
print(d)

print(d.shape)
e = np.array([[1,2,3,4],[3,4,5,6]])
print(e.shape)
print(e.dtype)

print(np.zeros((2,10)))
print(np.ones((2,10)))
print(np.arange(2,10)) #2이상 10미만의 1차원 배열 생성

a = np.ones((2,3))
print(a)
b = np.transpose(a) #행과 열이 바뀜
print(b)

arr1 = np.array([[2,3,4],[6,7,8]])
arr2 = np.array([[12,13,14],[26,27,28]])

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)


d = np.array([[1,2,3,4,5],[2,3,4,5,6,7],[5,6,7,8,9]])
print(d)
d_list = [[1,2,3,4,5],[2,3,4,5,6,7],[5,6,7,8,9]]
print(d_list)
print(type(d_list))
#d_list[:2] = 0 오류 발생
d_list[2] = 0
print(d_list)
print('===========================')
print(d)
d[:2] = 0
print(d)
print(np.arange(10))