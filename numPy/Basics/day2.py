import numpy as np
import time

# size = 10000000
# l1 = range(size)
# l2 = range(size)
#
# a1 = np.arange(size)
# a2 = np.arange(size)
#
# start = time.time()
# result = [(x + y) for x, y in zip(l1, l2)]
# print("Python list took: ", (time.time() - start) * 1000)

# start = time.time()
# result = a1 + a2
# print("Numpy array took: ", (time.time() - start) * 1000)




a = np.array([1,2,3,4,5])
# print(a.dtype)

b = np.array([[1,2,3, 5], [4,5,6, 2], [1,2,3,4]])

# print(b)
# print(a[1])
# print(b[2,2])
# print(b.size)
# print(b.shape)

# c = np.zeros(50)
# print(c)

# d = np.ones(50)
# print(d)

# e = b.reshape(4,3)
# print(e)

# x = np.arange(10)
# print(x)
# y = np.arange(10, 20)
# print(y)

# p = np.arange(1,10,2)
# print(p)

linearArr = np.linspace(1,5, 100)
# print(linearArr)

z = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
# print(z.min())
# print(z.max())

oneD = z.ravel()
# print(oneD)

# print(b.sum())
# print(b.sum(axis=0))
# print(b.sum(axis=1))

one = np.array([[1,2,3],[2,3,4],[2,5,7]])
two = np.array([[4,2,3],[2,36,4],[9,5,7]])
# print(one + two)

sum = one.dot(two)
print(sum)

print(np.std(one))
