curso = "Curso"
mi_string = "Codigo Facilito!"

"""Formato"""
result = "{a} de {b}".format(a = curso, b= mi_string) #Modifica el orden con el metodo format
#result = result.lower() #Minusculas o upper para mayusculas
#result = result.title()

"""Busqueda"""

posicion = result.find("Facilito")#Busca desde que posicion parte la palabra
contar = result.count("o")
nuevo_string = result.replace("o", "x")
nuevo_string2 = result.split(" ")

print(contar)
print(posicion)
print(result)
print(nuevo_string)
print(nuevo_string2)


