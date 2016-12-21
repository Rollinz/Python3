class Animal:
	volador = True

class Cocodrilo(Animal):

	def __init__(self, nombre):
		self.nombre = nombre

	@classmethod #Pueden acceder los atributos y metodos de clases
	def new(cls, nombre):
		cls.volador = False
		return Cocodrilo(nombre)

cocodrilo = Cocodrilo.new('Coco')
print(cocodrilo.nombre)
print(cocodrilo.volador)