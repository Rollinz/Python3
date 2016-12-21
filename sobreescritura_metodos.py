class Animal:
	pass

class Felino(Animal): #Clase padre
	@property
	def garras_retractiles(self):
		return True

class Mascota:
	def __init__(self, nombre):
		self.nombre = nombre

	def mostrar_nombre(self):
		print(self.nombre)

class Gato(Felino, Mascota):
	def __init__(self, nombre_gato):
		Mascota.__init__(self, nombre_gato) #Llamar al metodo de clase padre
		self.nombre_gato = nombre_gato

	def caza(self):
		self.cazar()

	def mostrar_nombre(self): #Sobre escritura de metodos
		Mascota.mostrar_nombre(self)
		print('El nombre del gato es: {}'.format(self.nombre))


gato = Gato('Poto')
gato.nombre = 'Gaspar'
gato.mostrar_nombre()