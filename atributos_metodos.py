class Lapiz:
	#Atributos
	color = 'Amarillo'
	contiene_borrador = False
	usa_grafito = False
	pasta = False
	pluma = True
	#Metodos
	def dibujar(self):
		print('El lapiz esta dibujando')

	def borrar(self):
		if self.es_valido_borrar():
			print('El lapiz esta borrando')
		else:
			print('No es posible borrar')

	def es_valido_borrar(self):
		return self.contiene_borrador

lapiz_generico = Lapiz()
lapiz_generico.dibujar()
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()