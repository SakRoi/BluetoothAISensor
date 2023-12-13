
# BluetoothAISensor

  

<p>A project for sending accelerometer data over a bluetooth connection and making conclusions about that data using machine learning</p>

  

## Description

The project is a collection of code that moves accelerometer data over a bluetooth connection and teaches both a k-means algorithm and a neural network to make predictions on that data. Centroids and weights gained from the teaching process can be used on nRF5340 to make predictions on the device itself. 


The sensor data collected by nRF is stored in a MySQL database after it has been moved to the Raspberry Pi. From there the data is fetched to a computer using a python script so that it can be used in the machine learning part of the project.

![Architecture](/pictures/arkkitehtuuri.png "Project Architecture")

Python was used for both the neural network and the k-means algorithm due to its ease of use. We used a Python library called Bleak for the bluetooth socket program.
and the neural network using TensorFlow.

After creating both algorithms they were recreated using C language by using the stored weights, biases and k-means centroids. This was done so that they could be used on the nRF without needing to transfer sensor data over bluetooth again. 

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



Above is a picture of a confusion matrix created based on live sensor data and a taught neural network. 
The matrix shows predicted direction compared to user-defined direction.
The same was done using K_Means but is not shown here.
