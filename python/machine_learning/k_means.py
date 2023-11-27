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

direction = [0, 1, 2, 3, 4, 5]

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
     

fig = plt.figure(figsize = (10, 7))
ax = fig.add_subplot(121, projection='3d')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.scatter(test_data_2[:, 0], test_data_2[:, 1], test_data_2[:, 2], c="r")


# Tee keskipisteet

centroid = np.random.rand(6, 3)
for i in range(centroid.shape[0]):
    centroid[i] = centroid[i] * 1000 + np.array([1200, 1200, 1200])

print(centroid)

ax.scatter(centroid[:, 0], centroid[:, 1], centroid[:, 2], c="gray")


# Laske keskipisteiden etäisyys dataan
for k in range(0, 30):

    #This is horrible, but using 3-dimensional array doesn't work for
    #some god damn reason

    cluster_1 = np.array([]).reshape(0, 3)
    cluster_2 = np.array([]).reshape(0, 3)
    cluster_3 = np.array([]).reshape(0, 3)
    cluster_4 = np.array([]).reshape(0, 3)
    cluster_5 = np.array([]).reshape(0, 3)
    cluster_6 = np.array([]).reshape(0, 3)

    distance_centers = np.zeros((6, 1))

    for i in range(len(test_data_2)):
            
            for j in range(distance_centers.shape[0]):
                distance_centers[j] = np.linalg.norm(centroid[j] - test_data_2[i])
            
            distance_centers_min = min(distance_centers)

            '''
            for j in range(distance_centers.shape[0]):
                if distance_centers[j] == distance_centers_min:
                    print(f"old cluster: {clusters[j]}, ind = {j}")
                    clusters[j] = np.vstack(clusters[j], test_data_2[i])
                    print(f"new cluster: {clusters[j]}, ind = {j}")
                    break
            '''
            if distance_centers[0] == distance_centers_min:
                cluster_1 = np.vstack((cluster_1, test_data_2[i]))

            elif distance_centers[1] == distance_centers_min:
                cluster_2 = np.vstack((cluster_2, test_data_2[i]))

            elif distance_centers[2] == distance_centers_min:
                cluster_3 = np.vstack((cluster_3, test_data_2[i]))

            elif distance_centers[3] == distance_centers_min:
                cluster_4 = np.vstack((cluster_4, test_data_2[i]))

            elif distance_centers[4] == distance_centers_min:
                cluster_5 = np.vstack((cluster_5, test_data_2[i]))

            else:
                cluster_6 = np.vstack((cluster_6, test_data_2[i]))

    #print(f" cluster 1: {clusters[0]}")
    #print(f" cluster 2: {clusters[1]}")

    #turn into it's own function
    for i in range(centroid.shape[1]):
        print(i)
        centroid[0, i] = np.mean(cluster_1[:, i])
        centroid[1, i] = np.mean(cluster_2[:, i])
        centroid[2, i] = np.mean(cluster_3[:, i])
        centroid[3, i] = np.mean(cluster_4[:, i])
        centroid[4, i] = np.mean(cluster_5[:, i])
        centroid[5, i] = np.mean(cluster_6[:, i])

    if is_cluster_empty(cluster_1):
        centroid[0] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
    if is_cluster_empty(cluster_2):
        centroid[1] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
    if is_cluster_empty(cluster_3):
        centroid[2] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
    if is_cluster_empty(cluster_4):
        centroid[3] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
    if is_cluster_empty(cluster_5):
        centroid[4] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
    if is_cluster_empty(cluster_6):
        centroid[5] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))

print(centroid)
ax.scatter(centroid[:, 0], centroid[:, 1], centroid[:, 2], s=300.0, c="green")

plt.show()


# Laske datalla uudet keskipisteet

#repeat