contador = 0
bandera = True

while bandera:
	print(contador)
	contador+=1

	if contador==5:
		print("Estamos en el numero 5")
		continue #break

	if contador==6:
		bandera = False
else:
	print("El ciclo while a terminado")
