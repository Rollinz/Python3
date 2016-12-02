import random #libreria random
import datetime #Fecha, ver el video de codigofacilito de fecha
import sys #libreria del sistema
import time

"""
valor = random.randint(0,10)
lista = [True,"String",9]
valor = random.choice(lista)
print(lista)
random.shuffle(lista)
print(lista)
"""

print(datetime.datetime.now())

for i in range(100):
	time.sleep(0.5)
	sys.stdout.write("\r%d %%" % i)
	sys.stdout.flush()