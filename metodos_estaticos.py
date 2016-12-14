class Circulo:

	#Metodo Estatico
	@staticmethod
	def pi():
		return 3.1416

	def __init__(self, radio):
		self.radio = radio
		
	def area(self): #Metodos de Instancia
		return self.radio * self.radio * self.pi() #* Circulo._pi

print(Circulo.pi())
circulo_uno = Circulo(7)
print(circulo_uno.area())