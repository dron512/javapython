from tensorflow import keras
from sklearn.model_selection import train_test_split

(train_input, train_target), (test_input, test_target) \
    = keras.datasets.fashion_mnist.load_data()

train_input = train_input.reshape(-1, 784)
test_input = test_input.reshape(-1, 784)
train_input, val_input, train_target, val_target = \
    train_test_split(train_input, train_target, random_state=42)

train_scaled = train_input / 255.0
test_scaled = test_input / 255.0
val_scaled = val_input / 255.0

dense1 = keras.layers.Dense(100, activation='sigmoid', input_shape=(784,))
dense2 = keras.layers.Dense(10, activation='softmax')
model = keras.Sequential([dense1, dense2])

model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')

model.fit(train_scaled, train_target, epochs=5)

훈련점수 = model.evaluate(train_scaled, train_target)
print(훈련점수)
