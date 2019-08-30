import numpy as np
a = np.arange(24).reshape(6,4)
print a
print a.shape #fila y columnas de la matriz
print a.mean(axis = 0).shape #valor medio de cada canal especificando el eje
print a.mean(axis = 1).shape #valor medio de cada canal especificando el eje
channel_means = a.mean(axis = 1)



