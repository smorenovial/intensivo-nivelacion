import numpy as np
a = np.array([10,1,20])
print a
subset = a[[0,2]] # me devuelve los valores que toman la posicion 0 y 2 en la matriz a
print subset
print a.flags.owndata # chequeo mis banderas asi vemos que tenemos nuestros propios datos
print subset.flags.owndata
print a is subset # a nos es un subconjunto

#subset es una matris [10 20]
subset[0] = -1 # cambiamos el valor en la posicion 0 por -1
print subset
a[-1] = 100
print a


