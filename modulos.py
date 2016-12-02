#! C:\Python35\python

"""
Aqui colocamos todo lo que hace el modulo y a que contexto le corresponde
"""

__author__ = "Rolando Andres Aburto Olivares"
__copyright__ = "Copyright 2016, Holo Tech"
__credits__ = "Holo Tech"

__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Rolando Andres Aburto Olivares"
__email__ = "raburtolivares@gmail.com"
__status__ = "Developer"


def adicion(num_uno, num_dos):	
	"""Suma 2 numeros y lo retorna"""
	return num_uno + num_dos

def sustraccion(num_uno, num_dos):	
	"""Resta 2 numeros y lo retorna"""
	return num_uno - num_dos

def multiplicacion(num_uno, num_dos):
	"""Multiplica 2 numeros y lo retorna"""
	return num_uno * num_dos	

def division(num_uno, num_dos):	
	"""Divide 2 numeros y lo retorna"""
	return num_uno + num_dos

def saluda():
	print("Saluda")

if __name__ == "__main__":
	saluda()

#help(modulos) para ver su documentacion