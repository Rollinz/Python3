class Usuario(object):
	def __init__(self, username, password, email):
		self.username = username
		self.__password = self.__generar_password(password) 				
		self.email = email

	def __generar_password(self, password):
		return password.upper()

	@property
	def password(self):
		return self.__password

	@password.setter
	def password(self, passw):
		self.__password = self.__generar_password(passw)

rolando = Usuario('Rolando', 'rolando123', 'rolando@email.com')
print(rolando.password)
rolando.password = 'nueva_password'
print(rolando.password)