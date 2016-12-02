def multiplicacion(valor_uno, valor_dos=10):
	return valor_uno * valor_dos

def mostrar_resultado(funcion): #Recibe una funcion como argumento
	print(funcion(6)) #Imprime la funcion


mi_variable = multiplicacion #Inserta una funcion completa en una variable
mostrar_resultado(mi_variable)

#tambien funciona de esta manera

"""
def mostrar_resultado(funcion):
	print(funcion)


mi_variable = multiplicacion
mostrar_resultado(mi_variable(6,8))
"""