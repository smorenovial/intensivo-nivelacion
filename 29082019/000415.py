a = [1,2,3,4]
b = [10,11,12,13]
print a + b

output = []
for item1, item2 in zip(a,b): 
	output.append(item1 + item2) # con este ciclo for se suma el pirmer valor de la lista a con el primer valor de la lista b y los mismo con los siguientes valores
print output


g = list(range(1000000))
#%timeit sum(g)


import numpy as np
a = np.array([1,2,3,4])
b = np.array([10,11,12,13])
print a + b
print a * b
print a / b
print a** b
print a 
print a.ndim
print a.shape

f = 5
print type(f) # la funcion type me devuelve el tipo de f, en este caso un int

f = (5,6)
print type(f) # en este caso una tupla, la tupla lo indica la coma. siguientes lineas de codigo lo explican

f = (10)
print type(f)

f = (10,) # tupla
print type(f)

#volviendo a las matrices a y b:
print a * 10 # multiplico cada valor de a por 10
print a * 100 # multiplico cada valor de a por 100
print np.sin(a) # imprime el seno de cada valor de la matriz a
print np.exp(a) # imprime el exponencial de cada valor de a
print np.log(a) # imprime el logaritmo de cada valor de a
print np.log #funcion python
print np.sum # funcion numpy
print a.dtype # a es tipo int
a = np.array([1,2,3,4.0])
print a.dtype # a es tipo float ya qeu tiene un elemento que no es int
a = np.array([1,2,3,4.0+1j]) # a es tipo complex y que tiene un elemento complejo
print a.dtype

a = np.array([1,2,3,4.0], dtype ='int64') # cambia el dtype de a
print a.dtype
c = np.array([[10,11,12],[20,21,22]])
print c.dtype
print c.ndim # dimencion de la matriz
print c.shape # nunmero de filas y columnas
print a.T 
print c.size #numero de elemnentos de la matriz c
print c.nbytes # para ver cuanta memoria esta usando la matriz c
print a[0] #el elemento en la posicion 0 de la matriz a
a[0] = 10 #se cambia el elemento de la posicion cero por un 10
print a
print c
print c[0,0] # la matriz c es de dos dimenciones por lo tnato se trata como un eje de coordenadas para llamar a sus elementos, en este caso el elemento 0,0
print c[0][0] # otra notacion para realizar lo anterior


g = np.arange(25).reshape(5,5)
print g
print g[:,1::2] #imprime una matriz con los elementos de la columna 1 y 3
print g[1::2,:-1:2] # agarra los elementos partiendo desde la fila 1 yendo de 2 en 2 y lo tro dice lo mismo solo que el tres dice qu lo hagas hasta la columna 3 sin incluirla
print g[4,:] # imprime la fila 4 de la matriz

red = g[:,1::2]
red[-1,-1] = 0 # cambia el valor que toma la posicion de la ultima fila con la ultima columna po run cero
print red
print g # al cambiar el valor anterior, esto tambien pruce ese cambio en la matriz original g

# las matrices poseen un ID

print id(g)
print id(red)
print red.flags #datos bandera
print g.data # datos que son una especie de punteros
print red.copy()






