import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.utils import load_img, img_to_array 
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import tensorflow as tf

# 기본 경로
base_dir = 'cats_and_dogs_filtered/cats_and_dogs_filtered'

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# 훈련에 사용되는 고양이/개 이미지 경로
train_cats_dir = os.path.join(train_dir, 'cats')
train_dogs_dir = os.path.join(train_dir, 'dogs')
print(train_cats_dir)
print(train_dogs_dir)

# 테스트에 사용되는 고양이/개 이미지 경로
validation_cats_dir = os.path.join(validation_dir, 'cats')
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

train_cat_fnames = os.listdir(train_cats_dir)
train_dog_fnames = os.listdir(train_dogs_dir)

# 훈련데이터 고양이 1000개 1000개 준비
print('Total training cat images :', len(os.listdir(train_cats_dir)))
print('Total training dog images :', len(os.listdir(train_dogs_dir)))

# 검증데이터 고양이 500개 500개 준비
print('Total validation cat images :', len(os.listdir(validation_cats_dir)))
print('Total validation dog images :', len(os.listdir(validation_dogs_dir)))


# nrows, ncols = 4, 4
# pic_index = 8

# fig = plt.gcf()
# fig.set_size_inches(ncols*3, nrows*3)

# next_cat_pix = [os.path.join(train_cats_dir, fname)
#                 for fname in train_cat_fnames[pic_index-8:pic_index]]
# print(next_cat_pix)

# next_dog_pix = [os.path.join(train_dogs_dir, fname)
#                 for fname in train_dog_fnames[pic_index-8:pic_index]]
# print(next_dog_pix)

# for i, img_path in enumerate(next_cat_pix+next_dog_pix):
#     sp = plt.subplot(nrows, ncols, i + 1)
#     sp.axis('Off')

#     img = mpimg.imread(img_path)
#     print(img.shape)
#     plt.imshow(img)

# plt.savefig('cat_dog.png')

# import cv2
# for i in range(30):
#     img = mpimg.imread(f'cats_and_dogs_filtered/cats_and_dogs_filtered\\train\\dogs\\dog.{i}.jpg')
#     img = cv2.resize(img,(150,150))
#     cv2.imshow('img',img)
#     cv2.waitKey(1000)


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu',
                           input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

print(model.summary())


model.compile(optimizer=RMSprop(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])


train_datagen = ImageDataGenerator(rescale=1.0/255.)
test_datagen = ImageDataGenerator(rescale=1.0/255.)

train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size=20,
                                                    class_mode='binary',
                                                    target_size=(150, 150))
validation_generator = test_datagen.flow_from_directory(validation_dir,
                                                        batch_size=20,
                                                        class_mode='binary',
                                                        target_size=(150, 150))

# print(train_generator)
# print(validation_generator)

# print(next(train_generator))


checkpoint_cb = tf.keras.callbacks.ModelCheckpoint('best-catdog-cnn-model.h5',
                                                   save_best_only=True)
early_stopping_cb = tf.keras.callbacks.EarlyStopping(patience=10,
                                                     restore_best_weights=True)

history = model.fit(train_generator,
                    validation_data=validation_generator,
                    steps_per_epoch=100,
                    epochs=100,
                    validation_steps=50,
                    callbacks=[checkpoint_cb, early_stopping_cb])


acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()

plt.savefig('acc.png')

plt.plot(epochs, loss, 'go', label='Training Loss')
plt.plot(epochs, val_loss, 'g', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()

plt.savefig('loss.png')



