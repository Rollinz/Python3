try:
	print(2/0)
	lista = [1,2]
	print(lista[9])
except IndexError as e:
	print(e)
	print('Sobrepasas el indice')
except ZeroDivisionError as e:
	print(e)
	print('No es posible dividir por 0')
except Exception as e:
	print(e)
	print('No es bueno esto, no se qu es')
finally: #se ejecuta si o si
	print('Se termino el script')