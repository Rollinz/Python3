class Lapiz:
	#si se le dan parametros con valores, estos seran por defecto, pero no impide que se puedan modificar en el constructor init
	def __init__(self, color = 'Amarillo', contiene_borrador = False, usa_grafito = False):
		self.color = color
		self.contiene_borrador = contiene_borrador
		self.usa_grafito = usa_grafito

	def dibujar(self):
		print('El lapiz esta dibujando')

	def borrar(self):
		if self.es_valido_para_borrar():
			print('El Lapiz esta borrando')
		else:
			print('No es posible borrar')

	def es_valido_para_borrar(self):
		return self.contiene_borrador

lapiz_generico = Lapiz('Rojo', True, True) #Se construye el objeto con valores determinados o por defecto
print(lapiz_generico.color)
lapiz_generico.dibujar()
lapiz_generico.borrar()