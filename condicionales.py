fruta = "kiwi"

#Primera estructura
if fruta == "kiwi": #> < >= <= != == las condiciones
	print("El valor es Kiwi")
elif fruta == "manzana":
	print("Es una manzana")
elif fruta == "manzana":
	pass #Permite que la aplicacion continue sin tomar encuenta lo que no hay en esta linea
else:
	print("No es kiwi")

#Segunda Estructura
mensaje = "Es un Kiwi" if fruta == "kiwi" else "No es un Kiwi"
print(mensaje)

if False:
	print("Es verdad")
else:
	print("No es verdad")

#Todas las [listas],(tuplas),{Diccionarios}, 0, "", son falsos xq estan vacios

valor = None
valor_dos = 21

if valor and valor_dos > 20: #palabras claves
	print("Es verdad")		# and, or, xor
else:
	print("No es verdad")