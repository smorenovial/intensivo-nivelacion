from skimage import io
photo = io.imread('IMG_0462.jpg')
photo.shape
import matplotlib.pyplot as plt
plt.imshow(photo) #llamar imagen
plt.imshow(photo[::-1]) #llamar imagen invertida
plt.imshow(photo[:, ::-1]) #se invierten las columanas de la matriz por lo que se obtiene una imganen tipo espejo
plt.imshow(photo[50:150,150:280]) #se selleciona una seccion de la imagen, en este caso x pertenenceinte al intervalo [50,150] e y perteneciente al intervalo [150,200]
plt.imshow(photo[::2,::2]) #se hace un zoom de la imagen
photo
photo_sin = np.sin(photo)
photo_sin
print(np.sum(photo)) #tomar la suma de al matriz
print(np.prod(photo)) #tomar el producto de al matriz
print(np.mean(photo)) #tomar la media de al matriz
print(np.std(photo)) #tomar la desviacion standar de al matriz
print(np.var(photo)) #tomar la varianza de al matriz
print(np.min(photo)) #tomar el minimo de al matriz
print(np.max(photo)) #tomar el maximo de al matriz
print(np.argmin(photo)) #tomar el argminimo de al matriz
print(np.argmax(photo)) #tomar el argmaximo de al matriz
z = np.array([1,2,3,4,5]) 
z < 3 # que valores del arreglo son menores a 3 (responde con true or false)
z > 3 # que valores del arreglo son mayores a 3 (responde con true or false)
z[z > 3] # devuelve los valores del arreglo que son amyores a 3
photo_masked = np.where(photo > 100, 255, 0) #valores mayores a 100 los cambia por 255 y los menores los cambia por 0
plt.imshow(photo_masked)

a_array = np.array([1,2,3,4,5])
b_array = np.array([6,7,8,9,10])
a_array + b_array #se suma cada elemnto del arreglo a con el arreglo b ojo: se suma el primer elemento de a con el primer elemento de b y asi se sigue con el segundo y tercer y....
a_array + 30 #se le suma 30 a cada elemento del arreglo a
a_array * b_array # lo mismo que en a_array + b_array pero con la multiplicacion
a_array * 10 #se le multiplica un 10 a cada elemento del arreglo a
a_array @ b_array # nos devuelve el producto punto de los arreglos

plt.imshow(photo[:,:,0].T) #transpone una matriz
x = np.array([2,1,4,3,5])
np.sort(x) #ordena los elementos del arreglo de menor a mayor