#import modulos
from modulos import sustraccion as resta #renombrar la funcion
from modulos import adicion
from modulos import __name__ as __name__modulo__

resultado = resta(58,12)
print(resultado)

print(__name__)
print(__name__modulo__)

"""
Un script solo por importarlo ejecuta todas
las funciones que no tienen identacion


por otra parte la funcion principal tiene el
atributo __name__ como __main__
si uno pregunta si es el script principal solo se ejecutara
las funciones que no tengan la pregunta
"""

