import cv2
import numpy as np
img = cv2.imread('20220811/gora.jpg',cv2.IMREAD_COLOR)

cv2.imshow('img[:,:,0]',img)
cv2.waitKey(0)

img[:,:,2] = 0

cv2.imshow('gora',img)
cv2.waitKey(0)

#[ 0 29 55]
a1 = img[:,:,2]<60
a2 = img[:,:,2]>53
b1 = img[:,:,1]<35 
b2 = img[:,:,1]>28
test1 = a1==a2
test2 = b1==b2
print(test1)
print(test2)

# print(all())
img[test1==test2] = [255,0,0]
cv2.imshow('gora2',img)
cv2.waitKey(0)
    

