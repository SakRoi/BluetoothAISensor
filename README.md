# BluetoothAISensor

  

<p>A project for sending accelerometer data over a bluetooth connection and making conclusions about that data using machine learning</p>

  

## Description

The project is a collection of code that moves accelerometer data over a bluetooth connection and teaches both a k-means algorithm and a neural network to make predictions on that data. Centroids and weights gained from the teaching process can be used on nRF5340 to make predictions on the device itself. 


The sensor data collected by nRF is stored in a MySQL database after it has been moved to the Raspberry Pi. From there the data is fetched to a computer using a python script so that it can be used in the machine learning part of the project.

![Architecture](/pictures/arkkitehtuuri.png "Project Architecture")


Python was used for both the neural network and the k-means algorithm due to its ease of use. We used a Python library called Bleak for the bluetooth socket program.
K-means was built using NumPy and the neural network using TensorFlow.

After creating both algorithms they were recreated using C language by using the stored weights, biases and k-means centroids. This was done so that they could be used on the nRF without needing to transfer sensor data over bluetooth again. 


<div style="width:60px ; height:60px ; center">
![K_Means_Centers](/pictures/k_means_centers.png "K_Means_Centers")
</div>


<p align="center">
 <img src="https://github.com/SakRoi/BluetoothAISensor/blob/readme/pictures/neural_network_pic.png?raw=true" alt="Neural_Network"/>
</p>



![Neural_Model](/pictures/neural_model.png "Neural_Model")




![Confusion_Matrix](/pictures/confusion_matrix.png "Confusion_Matrix")


Above is a picture of a confusion matrix created based on live sensor data and a taught neural network. 
The matrix shows predicted direction compared to user defined direction.
The same was done using K_Means but is not shown here.