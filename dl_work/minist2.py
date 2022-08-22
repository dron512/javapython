from tensorflow import keras
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

model = keras.models.load_model('best-cnn-model.h5')

(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

train_scaled = train_input.reshape(-1, 28, 28, 1) / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)

# print(train_scaled[0].shape)
# model.predict()

# plt.imshow(train_scaled[0].reshape(28,28),cmap='gray_r')
# plt.show()

pred = model.predict(train_scaled[0:1])
print(pred)

import numpy as np

print(np.argmax(pred))
classes = ['티셔츠', '바지', '스웨터', '드레스', '코트',
           '샌달', '셔츠', '스니커즈', '가방', '앵클 부츠']
print(classes[np.argmax(pred)])

import myloaddata

print(train_scaled[0:1])
print(train_scaled[0:1].shape)

# p1 = myloaddata.doloadimg("p1")
# sh1 = myloaddata.doloadimg("sh1")
# gabang = myloaddata.doloadimg("gabang")
# t1 = myloaddata.doloadimg("t1")

# plt.imshow(train_scaled[0].reshape(28,28),cmap='gray_r')
# plt.show()
# plt.imshow(p1[0].reshape(28,28),cmap='gray_r')
# plt.show()
# plt.imshow(sh1[0].reshape(28,28),cmap='gray_r')
# plt.show()
# plt.imshow(gabang[0].reshape(28,28),cmap='gray_r')
# plt.show()
# plt.imshow(t1[0].reshape(28,28),cmap='gray_r')
# plt.show()

# pred = model.predict(p1)
# print(classes[np.argmax(pred)])

# pred = model.predict(sh1)
# print(classes[np.argmax(pred)])

# pred = model.predict(gabang)
# print(classes[np.argmax(pred)])

# pred = model.predict(t1)
# print(classes[np.argmax(pred)])

for i in range(20):
    train = (1-train_scaled[i:i+1])*255
    myloaddata.dosaveimg(f'train{i}',train.reshape(28,28))