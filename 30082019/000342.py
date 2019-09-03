from matplotlib import pyplot as plt
dev_x = [25,26,27,28,29,30,31,32,33,34,35] #valores de la variable x
dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752] #valores de la variable y
plt.plot(dev_x, dev_y) #esto es para que plotee
plt.xlabel('Ages') #para ponerle nombre al eje x
plt.ylabel('Median Salary (USD)') #para ponerle nombre al eje y
plt.title('Mediam Salary (USD) by Age') #para ponerle titulo al grafico
plt.show() #este comando es para que grafique, como el print pero oara graficos