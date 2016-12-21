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

class Mascota:
	nombre = '' #Todas las mascotas necesitan un nombre

	def mostrar_nombre(self):
		print(self.nombre)

class Gato(Felino, Mascota):
	def habla(self):
		print('Miau')

	
gato = Gato()
gato.nombre = "Tinto"
gato.mostrar_nombre()
print(gato.terrestre)