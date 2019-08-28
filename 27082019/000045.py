import numpy as np
a = np.zeros(3) #crea una lista de 3 elementos con puros ceros
print a
z = np.zeros(10)
z.shape #la funcion shape muestra la cantidad de columnas
z.shape = (10,1) 
print z
z = np.ones(10) #lista con 10 valores y puros unos
print z
z = np.empty(3) #lista con 3 valores y puros ceros
print z
z = np.linspace(2,10,5) #lista la cual empieza con el 2 y termina con el 10 y tiene que tener 5 valores incluidos los extremos
print z
z = np.array([10,20]) #entrega un arreglo con los valores indicados (10,20)
print z
a_list = [1,2,3,4,5,6,7]
z = np.array([a_list]) #transforma una lista en un arreglo
print z
type(z) #misma funcion que np.array
print z
b_list = [[9,8,7,6,5,4,3],[1,2,3,4,5,6,7]]
z = np.array([b_list]) #transforma una lista de listas en una 'matriz'
print z
z.shape # misma funcion que la anterior
print z
np.random.seed(0)
z1 = np.random.randint(10,size=6)
print z1
print z1[0] #imprime el pirmer elemento de la lisa z1
print z1[0:2] #para obtener un rango
print z1[-1] #imprime el ultimo element ode la lista z1
