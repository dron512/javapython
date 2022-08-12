from email.mime import image
import cv2 
import numpy as np

img = cv2.imread('20220811/gora.jpg',cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(gray_img[100,100])
ret,th_img = cv2.threshold(gray_img,50,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(th_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# print(contours)
# print(type(contours))

# na = np.array(list(contours),dtype=int)
# print(na.shape)
con = contours[1]
print(con)

image = cv2.drawContours(img,contours,1,(0,255,0),1)

cv2.imshow('th_img',th_img)
cv2.imshow('image',image)
cv2.waitKey(0)
