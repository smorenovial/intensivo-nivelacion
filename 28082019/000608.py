import numpy as np
a = np.array([2,3,4]) # se crea una matriz
print a 
a = np.arange(1,12,2) # primer valor indica el numero con el cual empieza la matriz, segunod valor indica en que numero termina la matriz excluyendo dicho numero y el tercer valor indica el espaciamiento entre cada valor de la matriz
print a
a = np.linspace(1,12,6) # primer valor indica el numero con el cual empieza la matriz, segunod valor indica en que numero termina la matriz incluyendo dicho numero y el tercer valor indica la cantidad de numeros que tendra la matriz
print a
a.reshape(3,2)
print a
a = a.reshape(3,2)  # genera una matriz de 3x2 con los valores de a
print a
print a.size # numero de elementos de la matriz
print a.shape # numero de filas y columnas de la matriz
print a.dtype # entrega el tipo de dato
print a.itemsize # cuanta memoria en bits esta usando la matriz
b = np.array([(1.5,2,3),(4,5,6)]) #genera una matriz con los valores del primer parentesis redondo en la primera fila y los valores del segundo corchete rodnodo en la segunda fila
print b
print a < 4 # imprime la matriz a pero con true o false dependiendo si el valor de la matriz a cumple o no la condcion
print a*3 # multiplica por tres cada valor de la matriz a
a *= 3 #cambia los valores de la matriz a multiplicando cada valor por 3
print a
a = np.zeros((3,4)) #genera una matriz de puros ceros de dimenciones 3x4
print a
a = np.ones((2,3)) # genera una matriz de puros unos de dimenciones 2x3
print a
a = np.ones((10)) # genera una matriz de puros unos de dimenciones 1x10
print a
a = np.array([2,3,4], dtype = np.int16)
print a 
print a.dtype #tipo de dato que deseamos
print a.itemsize # la cantidad de espacios de memoria
a = np.random.random((2,3)) # matriz de 2x3 con numeros aleatorios entre cero y uno
print a
np.set_printoptions(precision = 2, suppress = True) # la precision hace que los valores de la matriz a tengan solo 2 decimales y el suppress los pone en notacion cientifica
print a
a = np.random.randint(0,10,5) # matriz aleatorria con numeros enteros de dimencion 1x5, los valores 1 y 10 indican que los numeros aleatorios van de 1 a 10 y el valor 5 indica que se imprimiran 5 valores
print a
print a.sum() # suma los valores de la matriz a
print a.min() # minimo valor de la matriz a
print a.max() # maximo valor de la matriz a
print a.mean() # promedio de valores de la matriz a
print a.var() # varianza de los valores de la matriz a
print a.std() # desviacion standar de los valores de la matriz


a = np.random.randint(1,10,6)
print a
a = a.reshape(3,2) # los valores de a lo ordena en una matriz de 3x2
print a
print a.sum(axis=1) # me devuelve las sumas de cada fila de la matriz a
print a.sum(axis=0) # me devuelve las sumas de cada columna de la matriz a
data = np.loadtxt("data.txt", dtype = np.uint8, delimiter = ",", skiprows = 1) # llama al archivo data (archivo de texto), el cual tiene numeros delimitados por comas
print data

a = np.arange(10) # imprime una matriz de 1x10 con valores de 0 a 9
print a
np.random.shuffle(a) # pone de forma aleatoria los valores de la matriz anterior
print a
print np.random.choice(a) # imprime un valor de la matriz a al azar
a = np.random.random_integers(5,10,2) # el 2 indica que se imprime una matriz de solo dos valores y el 5 y el 10 indican que los valores que iran dentro de la matriz estaran en el rango 5,10
print a










