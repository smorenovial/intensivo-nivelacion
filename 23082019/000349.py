given_list = [5,4,4,3,1,-2,-3,-5]

total3 = 0
i = 0
while given_list[i]> 0: #lo que ahce este siclo while es recorrer una lista, es decir, en la primera vuelta, el valor de i es 0, luego 1, luego 2 y a si sucesivamente.
	total3 += given_list[i] #va sumando los valores correspondientes a cada elemento de la lista mientras se recorre esta lista
	i+= 1
	print i
print total3