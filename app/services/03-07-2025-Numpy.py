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
print(np.random.randint(1, 10, (2,5)))
