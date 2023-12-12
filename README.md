# BluetoothAISensor

  

<p>A project for sending accelerometer data over a bluetooth connection and making conclusions about that data using machine learning</p>

  

## Description

The project is a collection of code that moves accelerometer data over a bluetooth connection and teaches both a k-means algorithm and a neural network to make predictions on that data. Centroids and weights gained from the teaching process can be used on nRF5340 to make predictions on the device itself.

[picture of the architecture]
![Employee data](/BluetoothAISensor/pictures/arkkitehtuuri.png?raw=true "Project Architecture")

Python was used for both the neural network and the k-means algorithm due to its ease of use. We used a Python library called Bleak for the bluetooth socket program.

K-means was built using NumPy and the neural network using TensorFlow.

[picture of the k-means output]

[picture of the neural network decription]

[model picture of the neural network]
pictures/arkkitehtuuri.png