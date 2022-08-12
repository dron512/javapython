import cv2

img = cv2.imread('20220811/gora.jpg',cv2.IMREAD_COLOR)

print(img.shape)
print(img.size)

px = img[100,100]

print(px)
print(px[2])