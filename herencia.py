class Animal:
	@property
	def terrestre(self):
		return True

class Felino(Animal): #Clase padre
	@property
	def garras_retractiles(self):
		return True

	def cazar(self):
		print('El felino esta cazando')


class Gato(Felino):
	def habla(self):
		print('Miau')

class Jaguar(Felino):
	def habla(self):
		print('Grawwwwr')
	
gato = Gato()

jaguar = Jaguar()

print(gato.garras_retractiles)
print(jaguar.garras_retractiles)
print(gato.habla())
print(gato.terrestre)