import numpy as np

kontti_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
kontti_2 = np.array([[1,2,8],[4,5,9],[7,8,100]])
kontti_3 = np.array([[666,2,3],[4,500,6],[7,8,77]])
kontti_4 = np.array([[666,2,3],[4,500,6],[77,77,77]])
kaljalava = np.array([kontti_1, kontti_2, kontti_3])
kaljalava[0]= kontti_1
kaljalava[1]= kontti_2
kaljalava[2]= kontti_3

print(kaljalava[0])

kaljalava[:] = np.vstack((kaljalava[0], kontti_4[:]))

print(kaljalava[0])