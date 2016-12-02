mi_lista = ["strings", 15, 16.4, True]

mi_lista.append(6) #ingresa en la ultima posicion
mi_lista.insert(0, "primero") #Definimos en que posicion
mi_lista.remove(15)#Remueve

mis_numeros = [4,2,5,7,1,3,6,9,8] 
mis_numeros_dos = [0,10]

mis_numeros.extend(mis_numeros_dos) #UNE una lista con otra lista

mis_numeros.sort()# funciona con un parametro tambien ... reverse = True

print(mis_numeros)

ultimo_valor = mi_lista.pop()#Toma el ultimo valor de la lista y lo elimina
print(mi_lista)#se aplica la regla de los corchetes
print(ultimo_valor)