import cv2
import numpy as np
from sklearn.tree import DecisionTreeClassifier

c11=cv2.imread('c11.png',cv2.IMREAD_GRAYSCALE)
c12=cv2.imread('c12.png',cv2.IMREAD_GRAYSCALE)
c11 = c11.reshape(-1)
c12 = c12.reshape(-1)

r11=cv2.imread('r11.png',cv2.IMREAD_GRAYSCALE)
r12=cv2.imread('r12.png',cv2.IMREAD_GRAYSCALE)
r11 = r11.reshape(-1)
r12 = r12.reshape(-1)

t11=cv2.imread('t11.png',cv2.IMREAD_GRAYSCALE)
t12=cv2.imread('t12.png',cv2.IMREAD_GRAYSCALE)
t11=t11.reshape(-1)
t12=t12.reshape(-1)

train_input=np.array([c11,c12,r11,r12,t11,t12])
print(train_input.shape)
train_target=['동그라미','동그라미','네모','네모','세모','세모']

dt = DecisionTreeClassifier()
dt.fit(train_input,train_target)

score = dt.score(train_input,train_target)
print(score)

prevalue = dt.predict([c11])
print(prevalue)

ct11 = cv2.imread('ct11.png',cv2.IMREAD_GRAYSCALE)
ct11 = ct11.reshape(-1)

prevalue = dt.predict([ct11])
print(prevalue)

np.savez('n1.npz',myarry=[c11,c12,r11,r12,t11,t12])








