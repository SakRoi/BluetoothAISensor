'''
Manual neural network. 
Lines to ignore: 0, 67, 196, 325
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd

def h_write(RW, RB, SW, SB):
    with open("ml.h", "w", newline='') as data:
        j = f"#ifndef HEADER_FILE\n#define HEADER_FILE\nfloat relu_weights[{RW.shape[0]}][{RW.shape[1]}] = {{"
        data.write(j)
        for i in RW:
            data.write("{")
            for j in i:
                data.write(f"{j},")
            data.write("},")

        j = f"}};\nfloat relu_biases[{RB.shape[0]}] = {{"
        data.write(j)
        for i in RB:
            data.write(f"{i},")

        j = F"}};\nfloat softmax_weights[{SW.shape[0]}][{SW.shape[1]}] = {{"
        data.write(j)
        for i in SW:
            data.write("{")
            for j in i:
                data.write(f"{j},")
            data.write("},")

        j = f"}};\nfloat softmax_biases[{SB.shape[0]}] = {{"
        data.write(j)
        for i in SB:
            data.write(f"{i},")

        j = "};\n#endif"
        data.write(j)

        

def reLU(Z):
    print(Z.shape)
    A = Z
    for i in range(Z.shape[0]):
            A[i] = max(Z[i], 0)
    return A

def softmax(Z):
    return np.exp(Z) / sum(np.exp(Z))

input_shape = (3)
num_classes = 6

x = 1900
y = 1600
z = 1600

RW = np.loadtxt("RW.csv", delimiter=',')
RB = np.loadtxt("RB.csv", delimiter=',')
SW = np.loadtxt("SW.csv", delimiter=',')
SB = np.loadtxt("SB.csv", delimiter=',')

print(RW.shape)

test_data = np.array([x, y, z])

#RW = np.reshape(RW, (3, -1))

Z1 = np.dot(test_data, RW) + RB
A1 = reLU(Z1)
print(A1.shape)
Z2 = np.dot(A1, SW) + SB
A2 = softmax(Z2)

print(A2)

h_write(RW, RB, SW, SB)

'''
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Dense(128, activation = "relu"),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()
model.load_weights('.weights.h5', skip_mismatch=False)

true_labels = 0

model.compile(loss=keras.losses.BinaryCrossentropy(),
                optimizer=keras.optimizers.Adam(), # use Adam instead of SGD
                metrics=['accuracy'])
'''