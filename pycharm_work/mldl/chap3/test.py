import cv2
import numpy as np
import time

myimg = np.zeros((400,400,3), np.uint8)
myimg1 = myimg

cv2.imshow('img',myimg)
cv2.imshow('img1',myimg1)
cv2.waitKey()

# myimg1[:] = [255,0,0]
myimg1=np.full((400,400,3),[255,0,0], np.uint8)

cv2.imshow('img3',myimg)
cv2.imshow('img4',myimg1)
cv2.waitKey()

cv2.destroyAllWindows()
for i in range(255):
    myimg1[100:-1,100:-1] = [255,i,0]
    cv2.imshow('img4', myimg1)
    cv2.waitKey(10)