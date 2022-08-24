import numpy as np
from tensorflow.keras.utils import load_img, img_to_array 
import matplotlib.image as mpimg
import tensorflow as tf
from scipy.special import expit



model = tf.keras.models.load_model('best-catdog-cnn-model.h5')

paths = [
# './cats_and_dogs_filtered/cats_and_dogs_filtered/validation/dogs/dog.2000.jpg',
# './cats_and_dogs_filtered/cats_and_dogs_filtered/validation/dogs/dog.2001.jpg',
# './cats_and_dogs_filtered/cats_and_dogs_filtered/validation/dogs/dog.2002.jpg',
# './cats_and_dogs_filtered/cats_and_dogs_filtered/validation/dogs/dog.2003.jpg',
# './cats_and_dogs_filtered/cats_and_dogs_filtered/validation/dogs/dog.2020.jpg',
'./cats_and_dogs_filtered/cats_and_dogs_filtered/validation/cats/cat.2001.jpg',
'./cats_and_dogs_filtered/cats_and_dogs_filtered/validation/cats/cat.2002.jpg',
'./cats_and_dogs_filtered/cats_and_dogs_filtered/validation/cats/cat.2003.jpg',
'./cats_and_dogs_filtered/cats_and_dogs_filtered/validation/cats/cat.2004.jpg',
'./cats_and_dogs_filtered/cats_and_dogs_filtered/validation/cats/cat.2005.jpg'
]

paths = [
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/dogs/dog.0.jpg',
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/dogs/dog.1.jpg',
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/dogs/dog.2.jpg',
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/dogs/dog.3.jpg',
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/dogs/dog.4.jpg',
]
paths = [
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/cats/cat.0.jpg',
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/cats/cat.1.jpg',
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/cats/cat.2.jpg',
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/cats/cat.3.jpg',
 './cats_and_dogs_filtered/cats_and_dogs_filtered/train/cats/cat.4.jpg',
]
for path in paths:
    img = load_img(path, target_size=(150, 150))

    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    classes = model.predict(images)

    print(path , classes)

    if classes[0] > 0:
        print("path 0 is a dog")
    else:
        print("path 1 is a cat")