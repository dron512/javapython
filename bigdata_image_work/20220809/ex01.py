import numpy as np

a = [1,2,3,4,5]
na = np.array(a)

print(len(a))
print(na.size)
# print(a.dtype)
print(na.dtype)
print(na.shape)

b = [10]*3
print(b)

nb = np.array(b)
nb = nb*3
print(nb)