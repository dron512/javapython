import cv2

def doloadimg(filename):
    p1 = cv2.imread(f'img/{filename}.png',cv2.IMREAD_GRAYSCALE)
    p1 = p1/255
    p1 = 1 - p1
    return p1.reshape(1,28,28,1)


def dosaveimg(filename,filedata):
    cv2.imwrite(f'{filename}.png',filedata)

def tempread():
    p1 = cv2.imread(f'temp.png',cv2.IMREAD_GRAYSCALE)
    p1 = p1/255
    p1 = 1 - p1
    return p1.reshape(1,28,28,1)