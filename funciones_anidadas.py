def division(num_uno, num_dos):

	def validacion():
		return num_uno > 0 and num_dos > 0

	if validacion(): #Llamado de funcion
		return num_uno / num_dos

resultado = division(10,2)
print(resultado)


def crear_funcion(num_uno, num_dos): #Funcion closure crea una funcion

	def validacion():
		print("se ejecuta validacion")
		return num_uno > 0 and num_dos > 0

	return validacion

nueva_funcion = crear_funcion(10, 5)


def aplicar_funcion(func):
	resultado = func() #V o F
	print(resultado)

#algoritmo
print(nueva_funcion())
aplicar_funcion(nueva_funcion)

