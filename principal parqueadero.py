from cliente import cliente # type: ignore
from carro import carro # type: ignore
from parqueadero import parqueadero # type: ignore

nombre = input (" ingrese nombre del cliente:")
cedula = input (" ingrese cedula del cliente:")
tipo_usuario = input (" ingrese tipo de usuario:")
obj_usuario = cliente(nombre,cedula,tipo_usuario)

placa = input ("ingrese placa del carro:")
tipo = input ("ingrese el tipo de carro:")
color = input (" ingrese el color del carro:")
obj_carro = carro(placa,tipo,color)

registrar_salida = input("¿le gustaria ingresar la salida de un carro?[si/no]")

if registrar_salida.lower() == "si":

    placa = input("ingrese la placa del carro para poder dar salida:")




