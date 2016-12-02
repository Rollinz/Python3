def factorial_numero(numero):
	factorial = 1
	while numero > 0:
		factorial = factorial * numero
		numero-=1
	return factorial

def suma(valor_uno, valor_dos, valor_tres):
	return valor_uno+valor_dos+valor_tres

def division(valor_uno, valor_dos):
	return valor_uno / valor_dos

def multiplicacion(valor_uno, valor_dos=10): #se le puede asigmar un valor default pero se puede modificar al llamar
	return valor_uno * valor_dos

def multiples_valores():
	return "String", 1, True


def mostrar_funcion(funcion):
	print(funcion(6,8))


resultado = factorial_numero(3)
resultado_suma = suma(10,20,30)
resultado_division = division(valor_uno=10, valor_dos=100)#se le puede asignar el orden de los argumentos
resultado_multiplicacion = multiplicacion(6)
string, entero, boleano = multiples_valores() #asigna valores x posicion


print(resultado_multiplicacion)
print(resultado)
print(resultado_suma)
print(resultado_division)


def resta(*args):
	resultado = 0
	for valor in args:
		resultado = resultado + valor
	return resultado

def ejemplo(**kwargs):
	valor = kwargs.get("valor", "No contiene valor")
	print(valor)
resultado_resta = resta(10, 5, 7, 9, 4)
resultado_ejemplo = ejemplo(valor="ROlando", x = 2, y = 9)
print(resultado_resta)