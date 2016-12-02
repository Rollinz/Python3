mi_funcion_lambda = lambda valor_uno, valor_dos : valor_uno + valor_dos

formato = lambda oracion : '¿{}?'.format(oracion)

no_valor = lambda : 10

no_resultado = lambda : print("Deben ejecutar una accion")

sentencia_resultado = formato('Esto es una pregunta')
resultado = mi_funcion_lambda(10,20)
resultado_no_valor = no_valor()
resultado_no_resultado = no_resultado()

print(resultado)
print(sentencia_resultado)
print(resultado_no_valor)
print(resultado_no_resultado)