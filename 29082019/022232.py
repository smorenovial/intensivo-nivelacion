from numpy impor loadtxt
data = loadtxt('wind.data')
dates = data[:, :3]
winds = data[:,3:]
print winds.mean(),winds.min(), winds.max(), winds.std() #aqui se imprime el promedio, el minimo, el maximo y la deesviacion standar
print winds.min() # imprime minimo
print winds.min(axis = 0) # imprime las columnas
print winds.min(axis=1) # imprime las filas
print winds.argmax(axis=1)
import numpy as np
rol, col = np.where(winds == winds.max())	
row, col = np.unravel_index(winds.argmax(), winds.shap)
row = winds.max(axis=1).argmax()
print dates[row]

january = dates[:, 1] == 1
winds[january, :].mean(axis = 0)