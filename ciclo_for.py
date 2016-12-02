lista = [1,2,3,4,5,6,7,8,9,10]

for valor in lista:
	#print(valor)
	pass

nuevo_rango = range(0,100000)#lista de numeros desde un punto a otro
nuevo_rango_dos = range(20) #Lista de 19 numeros
nuevo_rango_tres = range(0,20,2)#va de 2 en 2

for valor in nuevo_rango:
	#print(valor)
	pass


for indice, valor in enumerate(lista): #Asigna el indice y el valor
	print("El indice ", indice, "tiene valor ", valor)

for valor in range(0,len(lista)):
	print(valor) #cantidad de elementos

for valor in "Rolando Andres Aburto Olivares":
	print(valor)


diccionario = {"a":10, "b":20, "c":300}
for llave, valor in diccionario.items():
	print("la llave", llave, "tiene el valor ", valor)