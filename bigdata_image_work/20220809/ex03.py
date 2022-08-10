import numpy as np

def doA(*a,**b):
    print(a)
    print(*a)

a = np.zeros((3,3))
b = np.ones((4,4))
c = np.full((5,5),10)

print(a)
print(b)
print(c)

doA(3,{"aa":"aaa","bb":"bbb"})
doA((3,3))