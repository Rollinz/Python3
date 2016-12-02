"""
lista = [] #falso

for valor in range(0,100001):
	lista.append(valor)
	print(lista)
"""

lista = [valor for valor in range(0,101) if valor % 2 == 0] #Se agregan la cantidad de elementos que se quieran en un valor para la lista en 1 linea
#Que se necesita
#1-Valor a agregar a la lista
#2- Un ciclo, for

tupla = tuple((valor for valor in range(0,101) if valor % 2 != 0))

diccionario = {indice:valor for indice, valor in enumerate(lista) if indice < 10}
print(tupla)
print(lista)
print(diccionario) |

