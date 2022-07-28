from tensorflow import keras
import numpy as np
import cv2
import matplotlib.pyplot as plt

model = keras.Sequential()

model.add(keras.layers.Conv2D(32,
                              kernel_size=3, activation='relu',
                              padding='same',
                              input_shape=(100,100,1)))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Conv2D(64,
                              kernel_size=(3,3),
                              activation='relu',
                              padding='same'))
model.add(keras.layers.MaxPooling2D(2))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(3, activation='softmax'))
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics='accuracy')

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.h5',
                                                save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                                  restore_best_weights=True)

fruits = np.load('fruits_300.npy')
print(fruits.shape)
fruits2d = fruits.reshape(-1, 100,100, 1)
# 사과 0 파인애플 1 바나나 1
target = np.array([0] * 100 + [1] * 100 + [2] * 100)

history = model.fit(fruits2d, target, epochs=20)

a = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
print(a.shape)

b = cv2.imread('b.jpg', cv2.IMREAD_GRAYSCALE)
print(b.shape)
plt.imshow(b,cmap='gray_r')
plt.show()
# 사과 0 파인애플 1 바나나 2
pred = model.predict(a.reshape(-1,100,100,1))
print(pred,np.argmax(pred))
pred = model.predict(b.reshape(-1,100,100,1))
print(pred,np.argmax(pred))