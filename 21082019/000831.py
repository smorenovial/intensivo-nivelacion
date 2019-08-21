b = ["banana", "apple", "microsoft"] #crear una lista
print b 
print b[0] #me indica el primer elemento de la lista
temp = b[0] # a la vrialbe temp le asingo el primer elemento de la lista
b[0] = b[2] # al primer elemento de la lista le asigno el ultimo elemento de la lista
b[2] = temp # al ultimo elemento de la lista le asingo el elemento que se le habia asignado en un principio a la variable temp
print b
b[2] , b[0] = b[0] , b[2] # al elemento 2 de la lista le asigno el elemnto 0 de la lista y al elemneto 0 de la lista le asigno el elemento 2 de la lista
print b 