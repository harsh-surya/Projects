import numpy as np
import pandas as pd
import os
import random
import tensorflow as tf
from tensorflow import keras
from keras import layers, Model, Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
import matplotlib.pyplot as plt

train_gen = ImageDataGenerator(rescale = 1./255)
train_datagen = train_gen.flow_from_directory("Dataset/Training",
                                              batch_size = 64,
                                              class_mode = "categorical",
                                              color_mode = 'grayscale')

validation_gen = ImageDataGenerator(rescale = 1./255)
validation_datagen = validation_gen.flow_from_directory("Dataset/Training",
                                              batch_size = 32,
                                              class_mode = "categorical",
                                              color_mode = 'grayscale') 

model = Sequential()
model.add(layers.Conv2D(32, kernel_size = (5,5),  
                 activation = "relu",
                 padding = "same",
                 input_shape = (256,256,1)))
model.add(layers.MaxPooling2D(pool_size = (2,2), strides = 2))
model.add(layers.Conv2D(64, kernel_size = (5,5),
                        activation = "relu",
                        padding = "same",))
model.add(layers.MaxPooling2D(pool_size = (2,2), strides = 2))
model.add(layers.Conv2D(128, kernel_size = (5,5),
                        activation = "relu",
                        padding = "same",))
model.add(layers.MaxPooling2D(pool_size = (2,2), strides = 2))
model.add(layers.Dense(256, activation = "relu"))
model.add(layers.Flatten())
model.add(layers.Dense(9, activation = "softmax"))

model.compile(optimizer=Adam(learning_rate = 0.001), loss = "categorical_crossentropy", metrics = ["accuracy"])

#early_stopping_cb = keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True)

history = model.fit(train_datagen, 
          steps_per_epoch=len(train_datagen),
          validation_data=validation_datagen,
          epochs = 10,
          verbose = 2)

model.save("HandGestureDetection_cnn.h5")

acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, "b", label = "Training accuracy")
plt.plot(epochs, val_acc, "b--", label = "Validation accuracy")
plt.title("Training and validation accuracy")
plt.legend()
plt.show()

plt.plot(epochs, loss, "r", label = "Training loss")
plt.plot(epochs, val_loss, "r--", label = "Validation loss")
plt.title("Training and validation loss")
plt.legend()
plt.show()




