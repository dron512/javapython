import numpy as np

a = np.arange(8).reshape(-1,4)
b = np.arange(8).reshape(-1,4)

c = np.concatenate([a,b],axis=0)
d = np.arange(4).reshape(4,1)

print(c)
print(d)

print(c+d)