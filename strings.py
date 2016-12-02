mi_cadena = "Holo 'Python3'"

mi_texto = """Este es un texto muy largo 
que puede contener saltos de linea"""

curso = "Python3 "
nombre = "Rolando"

concatenacion = "Aprendiendo " + curso + " por " + nombre #Forma 1
concatenacion2 = "Aprendiendo %s por %s" %(curso, nombre) #Forma 2
concatenacion3 = "Aprendiendo {} por {}".format(curso, nombre) #Forma 3

#Imprimiendo strings
print(mi_cadena)
print(mi_texto)
print(concatenacion)
print(concatenacion2)
print(concatenacion3)
