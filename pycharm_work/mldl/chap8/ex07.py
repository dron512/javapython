from tensorflow import keras
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0
test_scaled = test_input / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)


# plt.imshow(train_scaled[40000],cmap='gray_r')
# plt.show()

def model_fn(a_layer=None):
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu',
                                  padding='same', input_shape=(28, 28, 1)))
    model.add(keras.layers.MaxPooling2D(2))
    model.add(keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu',
                                  padding='same'))
    model.add(keras.layers.MaxPooling2D(2))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(100, activation='relu'))
    if a_layer:
        model.add(a_layer)
    model.add(keras.layers.Dense(10, activation='softmax'))
    return model


# model = model_fn()
# model.compile(loss='sparse_categorical_crossentropy',metrics='accuracy')
#
# history = model.fit(train_scaled,train_target,epochs=20,
#               validation_data=(val_scaled,val_target))
#
# plt.plot(history.history['loss'],label='train')
# plt.plot(history.history['val_loss'],label='val')
# plt.legend()
# plt.show()

model = model_fn(keras.layers.Dropout(0.3))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam',
              metrics='accuracy')

checkpoint_cb = keras.callbacks.ModelCheckpoint('best_cnn_model.h5')
earlystopping = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)

history = model.fit(train_scaled, train_target, epochs=20,
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, earlystopping])
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.legend()
plt.show()

# model.save_weights('model_weights.h5')
# model.save('model_whole.h5')
