import cv2
import numpy as np
import matplotlib.pyplot as plt

woyo = cv2.imread('wt.png',cv2.IMREAD_GRAYSCALE)
print(woyo.shape)
print(woyo[0,:])
# pltwoyo = cv2.cvtColor(woyo, cv2.COLOR_BGR2RGB)
# np.save('a.npy',pltwoyo)

# pltwoyo = np.load('a.npy')

plt.scatter([10,20,30],[10,20,30],s=1000)
plt.text(100, 200, 'hihihi')
# plt.axis('off')
plt.imshow(woyo, cmap='gray_r')
plt.show()