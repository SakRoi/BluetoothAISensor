import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def h_write(centroids):
    '''Write the k-means centroids into a C-compatible header file'''

    with open("k_means.h", "w", newline='') as data:
        j = f"#ifndef KMEANS_HEADER_FILE\n#define KMEANS_HEADER_FILE\nfloat k_means[{centroids.shape[0]}][{centroids.shape[1]}] = {{"
        data.write(j)

        for i in centroids:
            data.write("{")
            for j in i:
                data.write(f"{j},")
            data.write("},")

        j = "};\n#endif"
        data.write(j)

def is_cluster_empty(clusterArray):
    '''Check if centroids cluster is empty'''
    if clusterArray.size == 0:
        return True
    else: 
        return False



#   test_data_1 = np.array([[1, 1, 1],[1, 2, 1],[1, 3, 1],
#                      [2, 1, 1],[2, 3, 1],
#                     [3, 1, 1], [3, 2, 1], [3, 3, 1],
#                      [6, 4, 3],[6, 5, 3],[6, 6, 3],
#                      [7, 4, 3],[7, 6, 3],
#                      [8, 4, 3], [8, 5, 3], [8, 6, 3]])
if '__main__':
    '''Use k-means to create centroids for the given data
    and then output it as a c-compatible header file'''

    df = pd.read_csv('data.csv')
    direction = [0, 1, 2, 3, 4, 5]
    test_data = np.array([])
    
    for k in df.index:
        if df.loc[k, "direction"] in direction:
            test_data = np.append(test_data, float(df.loc[k, "x"]))
            test_data = np.append(test_data, float(df.loc[k, "y"]))
            test_data = np.append(test_data, float(df.loc[k, "z"]))

    test_data = test_data.reshape(-1, 3)
    #print(test_data)
    #print(test_data.shape)

    fig = plt.figure(figsize = (10, 7))
    ax = fig.add_subplot(121, projection='3d')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.scatter(test_data[:, 0], test_data[:, 1], test_data[:, 2], c="r")

    #Create centroids and set their starting locations
    centroids = np.random.rand(6, 3)
    for i in range(centroids.shape[0]):
        centroids[i] = centroids[i] * 1000 + np.array([1200, 1200, 1200])
    ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c="gray")
    #print(centroids)


    #Compare centroids to data points and create clusters.
    for k in range(0, 30):

        #We create each cluster as a different array due to 3-dimensional arrays not working for our use case.

        cluster_1 = np.array([]).reshape(0, 3)
        cluster_2 = np.array([]).reshape(0, 3)
        cluster_3 = np.array([]).reshape(0, 3)
        cluster_4 = np.array([]).reshape(0, 3)
        cluster_5 = np.array([]).reshape(0, 3)
        cluster_6 = np.array([]).reshape(0, 3)

        distance_centers = np.zeros((6, 1))

        for i in range(len(test_data)):
                
                #Get distance from data point i to centroid j
                for j in range(distance_centers.shape[0]):
                    distance_centers[j] = np.linalg.norm(centroids[j] - test_data[i])
                
                distance_centers_min = min(distance_centers)

                if distance_centers[0] == distance_centers_min:
                    cluster_1 = np.vstack((cluster_1, test_data[i]))

                elif distance_centers[1] == distance_centers_min:
                    cluster_2 = np.vstack((cluster_2, test_data[i]))

                elif distance_centers[2] == distance_centers_min:
                    cluster_3 = np.vstack((cluster_3, test_data[i]))

                elif distance_centers[3] == distance_centers_min:
                    cluster_4 = np.vstack((cluster_4, test_data[i]))

                elif distance_centers[4] == distance_centers_min:
                    cluster_5 = np.vstack((cluster_5, test_data[i]))

                else:
                    cluster_6 = np.vstack((cluster_6, test_data[i]))

        
        #Calculate new centroid cordinates
        for i in range(centroids.shape[1]):
            #print(i)
            centroids[0, i] = np.mean(cluster_1[:, i])
            centroids[1, i] = np.mean(cluster_2[:, i])
            centroids[2, i] = np.mean(cluster_3[:, i])
            centroids[3, i] = np.mean(cluster_4[:, i])
            centroids[4, i] = np.mean(cluster_5[:, i])
            centroids[5, i] = np.mean(cluster_6[:, i])

        #Check if clusters are empty and randomize new cordinates for empty centroids
        if is_cluster_empty(cluster_1):
            centroids[0] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
        if is_cluster_empty(cluster_2):
            centroids[1] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
        if is_cluster_empty(cluster_3):
            centroids[2] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
        if is_cluster_empty(cluster_4):
            centroids[3] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
        if is_cluster_empty(cluster_5):
            centroids[4] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))
        if is_cluster_empty(cluster_6):
            centroids[5] = (np.random.rand(1, 3) * 1000 + np.array([1200, 1200, 1200]))

    print(centroids)
    ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], s=300.0, c="green")

    plt.show()

    h_write(centroids)