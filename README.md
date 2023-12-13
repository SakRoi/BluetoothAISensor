
# BluetoothAISensor

  

<p>A project for sending accelerometer data over a Bluetooth connection and making conclusions about that data using machine learning</p>

  
```
# Table of Contents
 1. [Description](#Description)
	 1. [Sensor data over Bluetooth LE](#Sensor data over Bluetooth LE)
	 2. [Getting data from the MySQL database](#Getting data from the MySQL database)
	 3. [K-means](#K-means)
	 4. [Neural Network](#Neural Network)
	 5. [Confusion matrix and ML on nRF5340](#Confusion matrix and ML on nRF5340)
2. [Installation guide](#Installation guide)
	1. [Requirements](#Requirements)
4. [How-to use](#How-to use)
5. [Credits](#Credits)
6. [License](#License]

```
## Description

The project is a collection of code that moves accelerometer data over a Bluetooth connection and teaches both a k-means algorithm and a neural network to make predictions on that data. Centroids and weights gained from the teaching process can be used on an nRF5340 to make predictions on the device itself. 

The sensor data collected by nRF is stored in a MySQL database after it has been moved to the Raspberry Pi. From there the data is fetched to a computer using a python script so that it can be used in the machine learning part of the project.

![Architecture](/pictures/arkkitehtuuri.png "Project Architecture")

### Sensor data over Bluetooth LE

<p align="center">
nRF5340<br>
 <img src="https://github.com/SakRoi/BluetoothAISensor/blob/readme/pictures/nRF5340.jpg?raw=true" alt="K_Means_Centers"/>
</p>

The nRF5340 microcontroller supports Bluetooth LE. Using this feat, the accelerometer data is sent over the air to the receiving computer. The receiving computer uses a Python library called Bleak for the Bluetooth socket program receiving the data. Bleak was chosen for its ease of use.

The Python script knows all the data is received from one measurement and to start a new one, when the nRF5340 sends a "666" value to it. If it has received the full measurement data, it is then sent to a MySQL database server using a TCP connection.

### Getting data from the MySQL database

Using an HTTP request to the MySQL server, the Python script gets the wanted sensor data from it and writes it as either a .csv or .txt file that then can be used as input for machine learning algorithms. 

For the HTTP requests, the Requests library was chosen for its ease of use.

### K-means
<p align="center">
Visualization of the working k-means algorithm. <br> Red dots = data points. Grey dots = centroid starting positions. Green areas = resulting clusters <br>
 <img src="https://github.com/SakRoi/BluetoothAISensor/blob/readme/pictures/k_means_centers.png?raw=true" alt="K_Means_Centers"/>
</p>
K-means was built using NumPy. <br>
In this K-means algorithm, 6 central points called centroids are created. These centroids are compared to the data points, and the closest are assigned to their clusters. After the iteration, the centroids are set to the central point of that cluster. This is repeated multiple times until the specified amount of iterations has been done. If the centroid's cluster is empty at the end of an iteration then it randomizes its location for the next iteration.

The centroids are then written into a separate .h file as an array for use in the nRF5340.

### Neural Network
<p align="center">
Visualization of the Neural Network<br>
 <img src="https://github.com/SakRoi/BluetoothAISensor/blob/readme/pictures/neural_network_pic.png?raw=true" alt="Neural_Network"/>
</p>

<p align="center">
Summary of the Neural Network model<br>
 <img src="https://github.com/SakRoi/BluetoothAISensor/blob/readme/pictures/neural_model.png?raw=true" alt="Neural_Model"/>
</p>

The neural network was built using TensorFlow. The model has two layers, one hidden and one output. ReLU activation was used to remove any negative values from the hidden layer. SoftMax activation was used to restrict the output between 0 and 1 in the output layer.

The above neural network was also built manually using numPy and the layer's weights and biasses are written into a separate .h file as arrays for use in the nRF5340.

### Confusion matrix and ML on nRF5340

<p align="center">
A picture of a confusion matrix visualizing the taught neural network's direction predictions compared to the user-defined direction.<br>
 <img src="https://github.com/SakRoi/BluetoothAISensor/blob/readme/pictures/confusion_matrix.png?raw=true" alt="Confusion_Matrix"/>
</p>

Finally, the resulting centroids, weights, and biases can be moved to the nRF5340, which can use the taught parameters to make predictions on the device itself without needing to send data over to a more powerful machine.

When using K-means, the nRF5340 compares the measurement data to each of the centroids and chooses the one closest to it. The index of the centroids is the same as the user-defined direction (0 = x high, 1 = x low, 2 = y high, etc.). This is charted on the confusion matrix.

When using a neural network, the nRF5340 puts the measurement data through forward propagation using a manually built model of the neural network. The weights and biases are also added to the calculation, resulting in a prediction. The made direction prediction is the index of the largest number in the output layer. This is charted on the confusion matrix.

## Installation guide
TO-DO
### Requirements
TO-DO
## How to use
TO-DO
## Credit
This project was a group effort by Kasperi Sänkiniemi and Saku Roininen. Most of the code was written pair programming.

## License
This project uses an MIT license
