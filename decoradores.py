"""
Es una funcion que recibe como parametro otra funcion
y retorna una nueva funcion 
"""
def decorador(es_valido): #Argumento al decorador
	def _decorador(funcion):
		def antes_de_la_accion():
			print("Vamos a ejecutar la funcion")

		def despues_de_la_funcion():
			print("Se ejecuto la funcion")

		def nueva_funcion(*args, **kwargs): #recibe N argumentos
			#agrega codigo EJ:Abre conexion BD
			if es_valido:
				antes_de_la_accion()
			resultado = funcion(*args, **kwargs) #Ejecuto la funcion
			#agrega codigo EJ: Cierra conexion BD
			despues_de_la_funcion()
			return resultado
		return nueva_funcion
	return _decorador

@decorador(es_valido = False) #Se le asigna el decorador
def saluda():
	print("Holo Mundo")

@decorador(es_valido = True) #Se le asigna el decorador
def suma(num_uno, num_dos):
	return num_uno + num_dos

saluda()
resultado = suma(10, 45)
print(resultado)