import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
print(a.shape)

a = a.reshape(-1,2)
print(a.shape)

print(a)