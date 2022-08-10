import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
ab = np.concatenate([a,b])
print(ab)

c = [1,2,3]
d = [4,5,6]

print(c+d)

e = np.array([3,4])
f = np.array([11])
print(e+f)

g = np.array([[1,2],[3,4]])
h = np.array([10,20])
print(g+h)