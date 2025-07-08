# keyboard shortcut to comment  ctrl + /
"""
 Numpy 
 Why numpy:
    1. Performance
    2. Memery efficiency 
    3. Powerful fucntion 
"""
import numpy as np

"""
import time

list1 = list(range(1,1000000))
list2 = list(range(1,1000000))
time_now = time.time()
sum_list = [x + y for x, y in zip(list1, list2)]
time_end = time.time()
print(f"List operation took {time_end - time_now}")

arr1 = np.arange(1,1000000)
arr2 = np.arange(1,1000000)
time_now = time.time()
sum_arr = arr1 + arr1
time_end = time.time()
print(f"NUMPY operation took {time_end - time_now}")
"""

# my_list = [1,2,3,4,5]
# arr = np.array(my_list)
# print(type(arr))


# my_list = [[1,2,3,4,5], [2,3,4,5,6]]
# arr = np.array(my_list)
# print(type(arr))

# arr_zero = np.zeros((3,4))
# print(arr_zero)
# arr_zero = np.ones((3,4))
# print(arr_zero)

# arr_const = np.full((2,3), 6)
# print(arr_const)

# arr_range = np.arange(1,10, 2, dtype=np.float32)
# print(arr_range)

# print(len(np.linspace(1,10)))

# print(np.random.rand(4))
# print(np.random.randint(1, 10, (2,5)))


# a = np.array([1,2,3,4,5])
# print(a.ndim)
# print(a.shape)

# a = np.array([[[300,2,3,4,5],
#              [6,7,8,9,0]]] , dtype="int32")
# print(a)
# print(a.ndim)
# print(a.shape)

# a = np.array([[[300,2,3,4,5],
#                 [6,7,8,9,0]],

#                 [[2,4,6,8,0],
#                  [1,3,5,7,9]]] , dtype="int32")
# print(a)
# a = np.array([1,2,3,4,5])
# a = np.array([[300,2,3,4,5],
#              [6,7,8,9,0]])
# print(a[1,0,1])
# print(a[1,1,4])
# print(a[1,1,-1])


# Element wise operation in array 

# a = np.array([1,2,4,5,8,9])
# print(a + 1)
# a = np.array([1,2,4,5,8,9])
# print(a - 5)
# a = np.array([1,2,4,5,8,9])
# print(a * 4)
# a = np.array([1,2,4,5,8,9])
# print(a / 4)

# a = np.array([1,2,4,5,8,9])
# print(a % 4)


# Matrix multiplication 
a = np.array([[1,2,3],
              [4,5,6]])
# print(a.shape)
# b = np.array([  [10, 20],
#                 [11, 21],
#                 [12, 22]])
# print(a)
# print(b)
# print(np.matmul(a,b))

# Broadcasting
# a = np.array([[1,2,3],
#               [4,5,6]])

# b = np.array([100, 200, 300])

# print(a + b)

a = np.array([[1,2,3],
              [4,5,6]])

# print(np.sum(a))
# print(np.sum(a, axis = 1))
# print(np.sum(a, axis = 0))
print(np.mean(a))
print(np.mean(a, axis = 1))
print(np.mean(a, axis = 0))


# a = np.array([[[300,2,3,4,5],
#                 [6,7,8,9,0]],

#                 [[2,4,6,8,0],
#                  [1,3,5,7,9]]] , dtype="int32")

# a[1,1,1 ] = 1000
# print(a)

a = np.array([1,2,3])
b = a.copy()
print(b)
b[2] = 1000
print(b) 
print(a)