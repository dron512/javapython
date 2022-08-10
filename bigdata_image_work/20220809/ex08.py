import numpy as np
import matplotlib.pyplot as plt

img = np.random.randint(0, 255, size=512*512*3).reshape(-1, 512, 3)
print(img.shape)

myfilter = np.full((100,100,3),[0,120,100])

print(myfilter.shape)

plt.imshow(img)
plt.show()

img[100:200, 200:300] = [255, 0, 0]
img[100:200, 200:300] = img[100:200, 200:300]+myfilter
# print(img[100:200,200:300])
# img = img[100:200, 200:300]+myfilter
# img[img[100:200, 200:300,0]>255] =[255,0,0]
plt.imshow(img)
plt.show()
