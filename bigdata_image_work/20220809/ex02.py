import numpy as np

a = [1,2,3,4,5]
b = np.arange(1,6)
c = [x for x in range(1,6)]
d = [y for y in range(1,6) if y%2==0]
e = [y*2 for y in range(1,6) if y%2==0]

a = np.array(a)
c = np.array(c)

print(a)
print(b)
print(c)
print(d)
print(e)