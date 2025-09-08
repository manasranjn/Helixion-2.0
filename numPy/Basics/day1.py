import numpy as np
import sys

a = np.array([1,2,3,4])
# print(a)
# print(a.size*a.itemsize)

b = [1,2,3,4]
# print(sys.getsizeof(b))

list1 = range(10000)
print(sys.getsizeof(1)*len(list1))

array1 = np.arange(10000)
print(sys.getsizeof(array1.size*array1.itemsize))