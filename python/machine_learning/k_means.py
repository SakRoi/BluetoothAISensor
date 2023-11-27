import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def is_cluster_empty(clusterArray):
    if clusterArray.size == 0:
        return True
    else: 
        return False

# Tee data
df = pd.read_csv('data.csv')

direction = [0, 1, 2, 3]

test_data_1 = np.array([[1, 1, 1],[1, 2, 1],[1, 3, 1],
                      [2, 1, 1],[2, 3, 1],
                      [3, 1, 1], [3, 2, 1], [3, 3, 1],
                      [6, 4, 3],[6, 5, 3],[6, 6, 3],
                      [7, 4, 3],[7, 6, 3],
                      [8, 4, 3], [8, 5, 3], [8, 6, 3]])

test_data_2 = np.array([])

for k in df.index:
    if df.loc[k, "direction"] in direction:
        test_data_2 = np.append(test_data_2, float(df.loc[k, "x"]))
        test_data_2 = np.append(test_data_2, float(df.loc[k, "y"]))
        test_data_2 = np.append(test_data_2, float(df.loc[k, "z"]))

test_data_2 = test_data_2.reshape(-1, 3)
print(test_data_2)
print(test_data_2.shape)
     

fig, ax = plt.subplots(1, 2)

ax[0].scatter(test_data_2[:, 0], test_data_2[:, 1])
ax[1].scatter(test_data_2[:, 1], test_data_2[:, 2])


# Tee keskipisteet

centroid = np.random.rand(2, 3)
centroid[0, :] = centroid[0, :] + np.array([[1000, 1000, 1000]])
centroid[1, :] = centroid[1, :] + np.array([[1000, 1000, 1000]])
print(centroid)
ax[0].scatter(centroid[:, 0], centroid[:, 1])
ax[1].scatter(centroid[:, 1], centroid[:, 2])


# Laske keskipisteiden etäisyys dataan
for j in range(0, 20):
    cluster_1 = np.array([]).reshape(0, 3)
    cluster_2 = np.array([]).reshape(0, 3)

    for i in range(len(test_data_2)):
            distance_center_1 = np.linalg.norm(centroid[0] - test_data_2[i])
            distance_center_2 = np.linalg.norm(centroid[1] - test_data_2[i])

            if distance_center_1 < distance_center_2:
                cluster_2 = np.vstack((cluster_2, test_data_2[i]))
            else:
                cluster_1 = np.vstack((cluster_1, test_data_2[i]))

    print(f" cluster 1: {cluster_1}")
    print(f" cluster 2: {cluster_2}")

    #turn into it's own function
    for i in range(centroid.shape[1]):
        print(i)
        centroid[0, i] = np.mean(cluster_1[:, i]) #get mean of cordinates of the cluster_1
        centroid[1, i] = np.mean(cluster_2[:, i]) #get mean of cordinates of the cluster_2

    if is_cluster_empty(cluster_1):
        centroid[0] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
    if is_cluster_empty(cluster_2):
        centroid[1] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))

print(centroid)
ax[0].scatter(centroid[:, 0], centroid[:, 1])
ax[1].scatter(centroid[:, 1], centroid[:, 2])

plt.show()


# Laske datalla uudet keskipisteet

#repeat