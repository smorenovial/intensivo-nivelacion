d = {}
d["George"] = 24 #le damos el valor 24 a la variable d["George"]
d["Tom"] = 32 #le damos el valor 32 a la variable d["Tom"]
d["Jenny"] = 16 #le damos el valor 16 a la variable d["Jenny"]
d["Jenny"] = 20
d[10] = 100

for key, value in d.iteritems():
	print ("key:")
	print (key)
	print ("value:")
	print(value)
	print("")	