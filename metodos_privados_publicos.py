class Usuario(object):
	def __init__(self, username, password, email):
		self.username = username
		#Doble guion bajo es un atributo privado para el interprete Python
		self.__password = self.__generar_password(password) 				
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	def get_password(self):
		return self.__password


rolando = Usuario('Rolando', 'rolando123', 'rolando@email.com')

print(rolando.username)
print(rolando.email)
print(rolando.get_password())
