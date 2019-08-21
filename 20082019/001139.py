#parametros de la persona como nombre, pedo y altura
name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160

#definimos la funcion para calcular si la persona esta o no en sobrepeso
def bmi_calculator(name, height_m, weight_kg):
	bmi = weight_kg / (height_m ** 2)
	print "bmi: ", bmi
	if bmi < 25:
		return name + " no esta en sobrepeso"
	else:
		return name + " esta en sobrepeso"
#creamos las variables que entregaran los resultados para luego poder llamar a estas varibales que poseen las funciones y asi poder obtener los resultados
result1 = bmi_calculator(name1,height_m1,weight_kg1)
result2 = bmi_calculator(name2,height_m2,weight_kg2)
result3 = bmi_calculator(name3,height_m3,weight_kg3)

print result1
print result2
print result3