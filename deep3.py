import numpy as np

a = np.array([[1,2], [2,4], [5,6]])
print(a)
print(np.ndim(a))
print(a.shape)

b = np.array([[1,2], [4,5]])
c = np.array([[2,3], [5,6]])
print(b.shape)
print(c.shape)
print(np.dot(b,c))

