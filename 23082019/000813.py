given_list2 = [5,4,4,3,1,-2,-3,-5]

total4 = 0
for element in given_list2:
	if element <= 0: #aqui se recorre la lista given_list2 con el ciclo for en el cual tiene la condicion de que si el elemento de la lista es menor o igual a 0, se deja de recorrer la lista y se imprime lo pedido
		break
	total4 += element
print total4