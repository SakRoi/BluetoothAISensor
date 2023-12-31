import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from tensorflow.keras import layers

if '__main__':
    '''Create and teach a neural network.
    Ouput the taught weights and biases into .csv files'''

    # Model / data parameters
    num_classes = 6
    input_shape = (3)

    # Load the data and split it between train and test sets
    data = pd.read_csv("data.csv")
    x = np.array([])
    y = np.array([])

    for k in data.index:
            x = np.append(x, float(data.loc[k, "x"]))
            x = np.append(x, float(data.loc[k, "y"]))
            x = np.append(x, float(data.loc[k, "z"]))
            y = np.append(y, float(data.loc[k, "direction"]))
    x = x.reshape((-1, 3))

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    print("x_train shape:", x_train.shape)
    print(x_train.shape[0], "train samples")
    print(x_test.shape[0], "test samples")

    print(y_train)

    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    print(y_train)

    model = keras.Sequential(
        [
            keras.Input(shape=input_shape),
            layers.Dense(10, activation = "relu"),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )

    model.summary()

    batch_size = 10
    epochs = 250

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

    score = model.evaluate(x_test, y_test, verbose=0)

    print("Test loss:", score[0])
    print("Test accuracy:", score[1])

    #Use the taught neural network to make predictions on test data.
    predictions = model.predict(x_test)
    predicted_labels = np.argmax(predictions, axis=1)
    true_labels = np.argmax(y_test, axis=1)

    failed_indices = np.where(predicted_labels != true_labels)[0]

    succesful_indices = np.where(predicted_labels == true_labels)

    print(len(failed_indices))
    for idx in failed_indices:
        print(f"x_test {x_test[idx]}")
        print(f"Predicted: {predicted_labels[idx]}, Actual: {true_labels[idx]}")

    print(len(succesful_indices))
    for idx in succesful_indices:
        print(f"x_test {x_test[idx]}")
        print(f"Predicted: {predicted_labels[idx]}, Actual: {true_labels[idx]}")

    #Get the weights and biases and then write them as .csv files
    RW = model.layers[0].get_weights()[0]
    RB = model.layers[0].get_weights()[1]
    SW = model.layers[1].get_weights()[0]
    SB = model.layers[1].get_weights()[1]

    print(f"ReLU weights: {RW}")
    print(f"ReLU bias: {RB}")

    print(f"softmax weights: {SW}")
    print(f"softmax bias: {SB}")

    np.savetxt('RW.csv', RW, delimiter=',')
    np.savetxt('RB.csv', RB, delimiter=',')
    np.savetxt('SW.csv', SW, delimiter=',')
    np.savetxt('SB.csv', SB, delimiter=',')