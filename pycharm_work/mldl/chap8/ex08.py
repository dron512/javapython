import numpy as np
from tensorflow import keras
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0
test_scaled = test_input / 255.0

train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)

# def model_fn(a_layer=None):
#     model = keras.Sequential()
#     model.add(keras.layers.Flatten(input_shape=(28,28)))
#     model.add(keras.layers.Dense(100,activation='relu'))
#     if a_layer:
#         model.add(a_layer)
#     model.add(keras.layers.Dense(10,activation='softmax'))
#     return model
#
#
# model = model_fn(keras.layers.Dropout(0.3))
# model.load_weights('model_weights.h5')
#
import cv2
def dopredict(a='t1.png'):
    img = cv2.imread(a, cv2.IMREAD_GRAYSCALE)
    img = 1 - img/255.0
    img[img<0.09] = 0
    print(img)
    plt.imshow(img,cmap='gray_r')
    plt.show()

    classes = ['티셔츠', '바지', '스웨터', '드레스', '코트',
               '샌달', '셔츠', '스니커즈', '가방', '앵클 부츠']

    model = keras.models.load_model('best_cnn_model.h5')
    pred = model.predict(img.reshape(-1,28,28))
    print(np.round(pred))
    print(classes[np.argmax(pred)])

dopredict('p1.png')
# dopredict('t1.png')
# dopredict('sh1.png')
# dopredict('sh2.png')
# dopredict('gabang.png')





