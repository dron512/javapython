import time
import cv2

img = cv2.imread('20220811/gora.jpg',cv2.IMREAD_COLOR)

start_time = time.time()
for i in range(100):
    for j in range(100):
        img[i,j] = [255,255,255]

print(f"걸린시간 = {time.time()-start_time}")

cv2.imshow('gora',img)
cv2.waitKey(0)

start_time = time.time()
img[:100,:100] = [0,0,0]
print(f"걸린시간 = {time.time()-start_time}")

cv2.imshow('gora',img)
cv2.waitKey(0)


