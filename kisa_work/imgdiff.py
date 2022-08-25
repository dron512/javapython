import os, time
from PIL import ImageChops
import cv2
from PIL import Image

# width, height = 956, 763
y_pos = 45

src = Image.open('src.png')
src = src.convert('RGB')
src.save('src.jpg')

dest = Image.open('org.png')
dest = dest.convert('RGB')
dest.save('dest.jpg')

diff = ImageChops.difference(src, dest)
diff.save('diff.jpg')

# 파일 생성 대기
while not os.path.exists('diff.jpg'):
    time.sleep(1)

import cv2
src_img = cv2.imread('src.jpg')
dest_img = cv2.imread('dest.jpg')
diff_img = cv2.imread('diff.jpg')

gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('diff_img', diff_img)
cv2.waitKey(0)

COLOR = (0, 200, 0)
for cnt in contours:
    print( cv2.contourArea(cnt) )
    x, y, width, height = cv2.boundingRect(cnt)
    cv2.rectangle(src_img, (x, y), (x + width, y + height), COLOR, 2)
    cv2.rectangle(dest_img, (x, y), (x + width, y + height), COLOR, 2)
    cv2.rectangle(diff_img, (x, y), (x + width, y + height), COLOR, 2)

    to_x = x + (width // 2)
    to_y = y + (height // 2) 
        
cv2.imshow('src', src_img)
cv2.imshow('dest', dest_img)
cv2.imshow('diff', diff_img)

cv2.waitKey(0)
cv2.destroyAllWindows()