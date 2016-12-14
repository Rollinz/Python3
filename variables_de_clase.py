class Circulo:
	#Esta es una variable de clase, el guion es una convencion
	_pi = 3.1416

	def __init__(self, radio):
		self.radio = radio
		
	def area(self):
		return self.radio * self.radio * Circulo.pi


c1 = Circulo(4)
c2 = Circulo(3)

print(Circulo.pi) 
print(c1.radio)
print(c2.pi)
print(c1.area())
print(c1.__dict__)