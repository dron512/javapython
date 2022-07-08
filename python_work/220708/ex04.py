import math
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = []
for i in x:
    y.append(math.sin(i))

print(x)
print(y)
plt.plot(x,y)
plt.scatter(x,y,c="#ff0000")
plt.show()