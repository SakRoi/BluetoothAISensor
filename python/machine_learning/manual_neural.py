'''
Manual neural network. 
Lines to ignore: 0, 67, 196, 325
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow import keras
from tensorflow.keras import layers
'''
weightfile = open('weights.csv', 'r')
data = np.array([])
 
for i in weightfile:
    data = np.append(data, i)

ReLu_Bias = data[1:67]
ReLu_Weight = data[68:196]
Softmax_Weight = data[197:325]
Softmax_Bias = data[326:]

ReLu_Bias2 = np.array([])

for i in ReLu_Bias:
    ReLu_Bias2 = np.append(ReLu_Bias2, float(ReLu_Bias[i]))
print(ReLu_Bias2)

layer = np.array([]).reshape(3,0)


print('shapes:',ReLu_Weight.shape,ReLu_Bias.shape,Softmax_Weight.shape, Softmax_Bias.shape )

ReLu = [[ReLu_Weight],[ReLu_Bias]]
Softmax = [[Softmax_Weight],[Softmax_Bias]]
#weights = weights.reshape(-1,2)
'''

num_classes = 6
input_shape = (3)

'''
#model.layers[0].set_weights(ReLu)    
print(ReLu)
model.layers[0].set_weights(ReLu_Weight, ReLu_Bias)
#model.layers[1].set_weights([Softmax_Weight, Softmax_Bias])
'''
x = 1900
y = 1700
z = 1700

test_data = np.array([[x, y, z]])

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Dense(128, activation = "relu"),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()
model.load_weights('c:/CodeStuff/Projektikurssi/Product/Neural/.weights.h5', skip_mismatch=False)

true_labels = 0

'''
model.compile(loss=keras.losses.BinaryCrossentropy(),
                optimizer=keras.optimizers.Adam(), # use Adam instead of SGD
                metrics=['accuracy'])
'''
 





predictions = model.predict_on_batch(test_data)
predicted_labels = np.argmax(predictions, axis = 1)


failed_indices = np.where(predicted_labels != true_labels)[0]

succesful_indices = np.where(predicted_labels == true_labels)

print(len(failed_indices))
for idx in failed_indices:
    print(f"x_test {test_data[idx]}")
    print(f"Predicted: {predicted_labels[idx]}, Actual: {true_labels}")

print(len(succesful_indices))
for idx in succesful_indices:
    print(f"x_test {test_data[idx]}")
    print(f"Predicted: {predicted_labels[idx]}, Actual: {true_labels}")

