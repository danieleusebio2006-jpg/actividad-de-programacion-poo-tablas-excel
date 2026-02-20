from usuario import Usuario
from calculadora import Calculadora
from numero import Numero


usuario1 = Usuario("jhoysmell", "31777041")
numero1 = Numero(10)
numero2 = Numero(8)


calculadora1 = Calculadora(numero1, numero2)


suma = calculadora1.resultado_suma
resta = calculadora1.resultado_resta
multiplicacion = calculadora1.resultado_multiplicacion
division = calculadora1.resultado_division


fecha_actual = calculadora1.get_fecha()
fecha_cambiada = calculadora1.set_fecha("2023-17-06")


# imprimir resultados
print(usuario1.imprimir_info())
print(calculadora1.imprimir_info())
print(numero1.imprimir_info())
print(numero2.imprimir_info())
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Fecha de la calculadora (antes): {fecha_actual}")
print(f"Fecha de la calculadora (después): {fecha_cambiada}")