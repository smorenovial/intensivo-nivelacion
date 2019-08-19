# se indican los datos de la persona (nombre, peso y estatura)
name = "YK"
height_m = 1.8
weight_kg = 80
# se desarrollo la formula para verificar si la persona esta en sobre peso o no
bmi = weight_kg / (height_m ** 2)
print "bmi:",bmi
#aqui se condiciona el valor del bmi para ver si la persona esta o no en sobrepeso
if bmi < 25:
	print name, "no esta en sobrepeso"
else:
	print name, "esta en sobrepeso"