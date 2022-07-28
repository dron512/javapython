import cv2
import numpy as np
import matplotlib.pyplot as plt
from fruitslog import getlog

a = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
print(a.shape)

b = cv2.imread('b.jpg', cv2.IMREAD_GRAYSCALE)
print(b.shape)
plt.imshow(b,cmap='gray_r')
plt.show()

lr = getlog()
pred = lr.predict(a.reshape(-1,10000))
print(pred)
pred = lr.predict(b.reshape(-1,10000))
print(pred)