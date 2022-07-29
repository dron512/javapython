import cv2


def gabang():
    gabang = cv2.imread('gabang.png', cv2.IMREAD_GRAYSCALE)
    print(gabang.shape)
    return gabang


def t1():
    t1 = cv2.imread('t1.png', cv2.IMREAD_GRAYSCALE)
    return t1

def p1():
    p1 = cv2.imread('p1.png', cv2.IMREAD_GRAYSCALE)
    return p1

def sh1():
    sh1 = cv2.imread('sh1.png', cv2.IMREAD_GRAYSCALE)
    return sh1