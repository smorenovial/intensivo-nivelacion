#otra manera de ponerle leyendas al grafico
from matplotlib import pyplot as plt

# Mediam Developer Salaries by Age

ages_x = [25,26,27,28,29,30,31,32,33,34,35] #valores de la variable x
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752] #valores de la variable y

# Mediam Python Developer Salaries by Age
py_dev_y = [45372,48876,53850,57278,63016,65998,70003,70000,71496,75370,83640]

# Mediam JavaScript Developer Salaries by Age
js_dev_y = [37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]

#para hacwer el codigo mas legible, podemos ponerle nombre a cada modificacion de grafico que hacemos en el ploteo

plt.plot(ages_x,dev_y, color = 'k', linestyle = '--', marker = '.', label = 'All Devs') # el label es otra manera de ponerle leyendas al grafico y el k-- es para asignarle un estilo de linea
plt.plot(ages_x,py_dev_y, color = 'b', marker = 'o', label = 'Python') # el b es para asignarle un color a la linea
plt.xlabel('Ages') #para ponerle nombre al eje x
plt.ylabel('Median Salary (USD)') #para ponerle nombre al eje y
plt.title('Mediam Salary (USD) by Age') #para ponerle titulo al grafico
plt.legend() #ponerle leyendas al grafico
plt.show() #este comando es para que grafique, como el print pero oara graficos