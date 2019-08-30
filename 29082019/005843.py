import numpy as np
a = np.array([3,-1,-2,4,-6,8])
print a
print a < 0

negatives = a < 0 #genera una nueva matriz con los valore negativos de a
print a[negatives]
print a[a < 0] # otra forma de generar una mtriz con los valores negativos de a

a[a < 0] = 0 # todosl os valores negativos de la matriz a los cambia por ceros
print a 

print a < 8
print a > 3

print (a < 8).any()
print (a > 3) & (a < 8) # valores de la matriz a que estan entre 3 y 8

print a



f = 6
g = 9
print f + g
print f.__add__(g)
print negatives
print (a > 3) & (a < 8)
print negatives
print np.nonzero(negatives) #devuelve la posicion de los valores de la matriz a 
print a.sort()
print a


a = np.array([10,1,20])
b = np.array([2,3,20])
print a > b #se compara el elemento de la posicion i de a con el de b
print np.nonzero(a > b) #me imprime un cero debido a que no hay ceros






