def palindromo(frase):
	frase = frase.replace(" ","") #Varibale local
	return frase == frase[::-1]

frase = "anita lava la tina" #Variables Globales, estan pueden ser accedidas desde una funcion
resultado = palindromo(frase)
print(resultado)

def palindromo():
	nuevo_valor = frase.replace(" ","") #Varibale local
	return nuevo_valor == nuevo_valor[::-1]

resultado = palindromo()
print(resultado)


#para definir una variable global o modificarla se usa la palabra reservada global
def valor_global(): 
	global varibale_global 
	varibale_global = "Cambio de valor"

def mostrar_global():
	print(varibale_global)

def crear_global():
	global nueva_variable_global
	nueva_variable_global = "Esto es una variable global"

varibale_global="variable global"
mostrar_global()
valor_global()
print(varibale_global)

crear_global()
print(nueva_variable_global)