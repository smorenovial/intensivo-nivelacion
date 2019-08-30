import numpy as np
a = np.arange(25).reshape(5,5)
print a
print a % 3 # se le calcula el modulo o resto a cada elemento de la matriz

#asi podemos ver que cuando  el resto es cero, el element0o es divisible por 3

#creamos una especie de mascara:
print a % 3 == 0 # aqui se puede ver cual cumple y cual no
print a[a % 3 == 0] #luego aqui me devuelve los valores que cumplen (que son divisibles por 3)


print np.nan

output = np.empty_like(a)
print output

output.fill(np.nan)
print output

output = np.empty_like(a, dtype = 'float')
print output

output.fill(np.nan)
print output
print a

mask = a % 3 == 0
output[mask] = a[mask]
print output

np.where(a % 3 == 0, a,np.nan)

print a[mask]
print output[mask]
print np.full_like(a, np.nan, dtype = 'float64')


print a
b = np.array([2,3,20])
print b

print np.nan + 6
print np.sum([1, np.nan, 9])
print np.nansum([1, np.nan, 9])
print a[a % 3 == 0].sum()

a = np.array([1,2,3])