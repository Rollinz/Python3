diccionario = {"a" : 55, 5 : "Esto es un string", (1,2):False} #Las claves se pueden reemplazar y su contenido siempre sera el ultimo
diccionario["c"] = "Nuevo string" #Crea una nueva clave/valor
diccionario["a"] = False #reemplaza
#valor = diccionario["a"]
valor = diccionario.get('z', (12,2))
del diccionario[(1,2)] #Borrar
print(diccionario)
print(valor)

llaves = list(diccionario.keys()) #Objeto iterable
valores = list(diccionario.values()) #En vez de list puede ser tuple
diccionario_dos = {1:3,4:"poto"}
diccionario.update(diccionario_dos)
print(llaves)
print(valores)
print(diccionario)