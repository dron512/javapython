from tensorflow import keras
from sklearn.model_selection import train_test_split


(train_input, train_target), (test_input, test_target) \
    = keras.datasets.fashion_mnist.load_data()

train_input, val_input, train_target, val_target = \
    train_test_split(train_input, train_target, random_state=42)

train_scaled = train_input /255.0
test_scaled = test_input /255.0
val_scaled = val_input /255.0

# model = keras.models.load_model('whole.h5')
# print(model.history)
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(28,28)))
model.add(keras.layers.Dense(100,activation='relu'))
model.add(keras.layers.Dropout(0.3))
model.add(keras.layers.Dense(10,activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',metrics='accuracy',
              optimizer='adam')

history = model.fit(train_scaled,train_target,epochs=20
                    ,validation_data=[val_scaled,val_target])

print(history.history)
# model.save('whole.h5')

import matplotlib.pyplot as plt

plt.plot(history.history['loss'],label='loss')
plt.plot(history.history['val_loss'],label='val_loss')
plt.legend()
plt.show()

# 훈련점수 = model.evaluate(train_scaled,train_target)
# print(훈련점수)

import ex03

gabang = 1-ex03.gabang()
p1 = 1-ex03.p1()
sh1 = 1-ex03.sh1()
t1 = 1-ex03.t1()

import numpy as np

pred = model.predict(gabang.reshape(-1,28,28))
print(np.round(pred,decimals=0))
print(np.argmax(pred))

pred = model.predict(p1.reshape(-1,28,28))
print(np.round(pred,decimals=2))
print(np.argmax(pred))

pred = model.predict(sh1.reshape(-1,28,28))
print(np.round(pred,decimals=2))
print(np.argmax(pred))

pred = model.predict(t1.reshape(-1,28,28))
print(np.round(pred,decimals=2))
print(np.argmax(pred))








