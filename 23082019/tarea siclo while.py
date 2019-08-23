given_list3 = [7,5,4,4,3,1,-2,-3,-5,-7]
i = 0
total = 0
while i <= 9:
	if given_list3[i] >= 0: # si el elemento de la lista es un valor positivo, lo rechazo
		print given_list3[i], "no me sirve"
		i += 1
	else: #si el elemento de la lista no es un valor positivo, entramos en este codigo
		total += given_list3[i] # aqui se suman los valores que el elemento i toma y se va actualizando el valor de la variable "total"
		i += 1
print total
