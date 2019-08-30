import numpy as np
a = np.arange(36).reshape(6,6)
print a
print a[[0,1,2,3,4],[1,2,3,4,5]] #el primer corchete contiene las coordenadas i de los valores que quiero obtener y el segundo corchete contiene las coordenadas j
print a[3:, [0,2,5]] # debido al 3 se imprimen todas las  filas desde la 3 en adelante pero con el corchete [0,2,5] hace que se impriman las columnas 0, 2,5
mask = np.array([1,0,1,0,0,1], dtype = bool) #en el arreglo anterior, si el numero es 1 lo imprime y si el numero es cro no lo imprime
print a[mask, 2] #aqui se usa la condicion anterior y se aplica a la columna 2





