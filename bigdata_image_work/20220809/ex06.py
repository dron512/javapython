import numpy as np

a = np.arange(4)
b = np.arange(8)

print(a)
print(b)

c = np.concatenate([a,b],axis=0)
print(c)

a = a.reshape(-1,4)
b = b.reshape(-1,4)

print(a)
print(b)

c = np.concatenate([a,b],axis=0)
print(c)