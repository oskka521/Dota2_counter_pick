import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

X = pickle.load(open('X.pickle', 'rb'))
y = pickle.load(open('y.pickle', 'rb'))


X = X/255.0

X = np.asarray(X).astype(np.float32)
y = np.asarray(y).astype(np.float32)

model = Sequential()

model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Dense(1, activation='softmax'))


model.compile(loss='binary_crossentropy',
              optimizer='adam', merics=['accuracy'])

model.fit(X, y, batch_size=32, validation_split=0.1, epochs=10)
