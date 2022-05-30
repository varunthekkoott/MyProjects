import cv2
import numpy as np
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(train_x, train_y), (test_x, test_y) = mnist.load_data()

train_x = tf.keras.utils.normalize(train_x, axis=1)
test_x = tf.keras.utils.normalize(test_x, axis=1)
print('.', end='')

model = tf.keras.models.Sequential()
print('.', end='')
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
print('.', end='')

model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
print('.', end='')

model.add(tf.keras.layers.Conv2D(80, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
print('.', end='')

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))
print('.', end='')

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_x, train_y, epochs=3)
print('.', end='')

model.save('Digit_Recognition.model')
print('. Saved', end='')
