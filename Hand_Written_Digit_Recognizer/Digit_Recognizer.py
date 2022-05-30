import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('Digit_Recognition.model')
print('i')
img = cv2.imread('digittest.png')[:, :, 0]
img = np.invert(np.array([img]))
prediction = model.predict(img)
print(prediction)
print(f'The number is probably a {np.argmax(prediction)}')
cv2.imshow('Window', cv2.imread('digittest.png'))
cv2.waitKey(0)
