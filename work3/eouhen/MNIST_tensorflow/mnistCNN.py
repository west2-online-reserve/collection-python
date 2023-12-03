# Author : AnnieHathaway
from tensorflow.python.keras.utils.np_utils import to_categorical
from tensorflow.keras import models, layers, regularizers
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.datasets import mnist
import tensorflow as tf

import matplotlib.pyplot as plt

# 加载数据集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
"""print(train_images.shape, test_images.shape)
print(train_images[0])
print(train_labels[0])
plt.imshow(train_images[0])
plt.show()"""
# 平铺
train_images = train_images.reshape((60000, 28*28)).astype('float')
test_images = test_images.reshape((10000, 28*28)).astype('float')
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
# 建立神经网络模式
network = models.Sequential()
network.add(layers.Dense(units=128, activation='relu', input_shape=(28*28, ),))
network.add(layers.Dense(units=32, activation='relu'))
network.add(layers.Dense(units=10, activation='softmax'))
# print(network.summary())
# 训练神经网路
# 调用compile编译接口：确定优化器和损失函数
# network.compile(optimizer=RMSprop(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
network.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
# 调用fit函数训练网络：确定训练的数据、训练的轮数和每次训练的样本数等
# epochs表示训练多少个回合，batch_size表示每次训练给多大的数据
network.fit(train_images, train_labels, epochs=20, batch_size=128, verbose=2)
# 测试集
# y_pre = network.predict(test_images[:5])
# print(y_pre, test_labels[:5])
test_loss, test_accuracy = network.evaluate(test_images, test_labels)
print("test_loss:", test_loss, "    test_accuracy:", test_accuracy)