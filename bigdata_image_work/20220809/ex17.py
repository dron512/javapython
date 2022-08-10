from itertools import count
import numpy as np

la = np.linspace(0,10,4)
print(la)

np.random.seed(42)
ra = np.random.randint(0,7,(1,3))
print(ra)

a1 = np.arange(0,10)
a2 = a1.copy()
print(a1)
print(a2)
a2[0] = 20
print(a1)
print(a2)

a3 = np.array([4,3,1,2,3,1,3])
a4 = np.unique(a3)
print(a4)
