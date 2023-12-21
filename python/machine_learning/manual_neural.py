'''
Manual neural network.
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd

def h_write(RW, RB, SW, SB):
    '''Write the neural networks weights and biases into a C-compatible header file '''


    with open("ml.h", "w", newline='') as data:
        #Write ReLU layer weights
        j = f"#ifndef HEADER_FILE\n#define HEADER_FILE\nfloat relu_weights[{RW.shape[0]}][{RW.shape[1]}] = {{"
        data.write(j)
        for i in RW:
            data.write("{")
            for j in i:
                data.write(f"{j},")
            data.write("},")

        #Write ReLU layer biases
        j = f"}};\nfloat relu_biases[{RB.shape[0]}] = {{"
        data.write(j)
        for i in RB:
            data.write(f"{i},")
        
        #Write softMax layer weights
        j = F"}};\nfloat softmax_weights[{SW.shape[0]}][{SW.shape[1]}] = {{"
        data.write(j)
        for i in SW:
            data.write("{")
            for j in i:
                data.write(f"{j},")
            data.write("},")

        #Write softMax layer biases
        j = f"}};\nfloat softmax_biases[{SB.shape[0]}] = {{"
        data.write(j)
        for i in SB:
            data.write(f"{i},")

        j = "};\n#endif"
        data.write(j)

        

def reLU(Z):
    '''reLU layer calculations'''
    #print(Z.shape)
    A = Z
    for i in range(Z.shape[0]):
            A[i] = max(Z[i], 0)
    return A

def softmax(Z):
    '''SoftMax layer calculations'''
    return np.exp(Z) / sum(np.exp(Z))

if '__main__':
    '''Neural network with forward propagation and prediction
    using already taught weights and biases.
    Write the taught weights and biases into a c-compatible header file'''
    input_shape = (3)
    num_classes = 6

    #Test data
    x = 1900
    y = 1600
    z = 1600
    test_data = np.array([x, y, z])

    #Load the weights and biases from .csv files
    RW = np.loadtxt("RW.csv", delimiter=',')
    RB = np.loadtxt("RB.csv", delimiter=',')
    SW = np.loadtxt("SW.csv", delimiter=',')
    SB = np.loadtxt("SB.csv", delimiter=',')

    #print(RW.shape)

    #Neural network forward propagation
    Z1 = np.dot(test_data, RW) + RB
    A1 = reLU(Z1)
    #print(A1.shape)
    Z2 = np.dot(A1, SW) + SB
    A2 = softmax(Z2)
    
    print(A2)

    h_write(RW, RB, SW, SB)