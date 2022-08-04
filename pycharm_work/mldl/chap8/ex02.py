from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

(train_input, train_target), (test_input, test_target) \
    = keras.datasets.fashion_mnist.load_data()

train_scaled = train_input / 255.0
test_scaled = test_input / 255.0

train_scaled,val_scaled,train_target,val_target =\
    train_test_split(train_scaled,train_target,random_state=42)

model = keras.models.load_model('best_cnn_model.h5')

print(model.layers[0])
print(model.layers[1])
print(model.layers[2])
print(model.layers[3])

pred = model.predict( train_scaled[0].reshape(-1,28,28))
print(np.argmax(pred))

classes = ['티셔츠', '바지', '스웨터', '드레스', '코트',
           '샌달', '셔츠', '스니커즈', '가방', '앵클 부츠']

print(classes[np.argmax(pred)])

plt.imshow(train_scaled[0].reshape(28,28),cmap='gray_r')
plt.show()

inputs = model.input
con2v0out = model.layers[2]
print(model.input)
print(con2v0out)

con1model = keras.Model(inputs,con2v0out.output)
con1feac = con1model.predict(train_scaled[0].reshape(-1,28,28))

print(con1feac.shape)

fig,axs = plt.subplots(2,16,figsize=(16,2))
for i in range(2):
    for j in range(16):
        axs[i,j].imshow(con1feac[0,:,:,i*16+j])
        axs[i,j].axis('off')

plt.savefig(f'img/conv2.png')






