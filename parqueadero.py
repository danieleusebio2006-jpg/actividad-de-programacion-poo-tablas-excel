from datetime import datetime
class parqueadero:
    def __init__(self):
        self.puesto = None
        self.fecha_entrada = None
        self.hora_entrada = None
        self.hora_salida = None
        self.estado = "libre"
        self.cliente = None
        self.carro = None
        self.texto_tabla =""
    

    def get_puesto(self):
        return self.puesto

    def set_puesto(self,nuevo_puesto):
        self.puesto = nuevo_puesto

    def get_fecha_entrada(self):
        return self.fecha_entrada

    def set_fecha_entrada(self,nueva_fecha):
        self.fecha_entrada = nueva_fecha

    def get_hora_entrada(self):
        return self.hora_entrada

    def set_hora_entrada(self,nueva_hora_entrada):
        self.hora_entrada = nueva_hora_entrada

    def get_hora_salida(self):
        self.hora_salida

    def set_hora_salida(self,nueva_hora_salida):
        self.hora_salida = nueva_hora_salida

    def get_estado(self):
        return self.estado

    def set_estado(self,nuevo_estado):
        self.estado = nuevo_estado

    def get_cliente(self):
        return self.cliente
    
    def set_cliente(self,nuevo_cliente):
        self,cliente = nuevo_cliente

    def get_carro(self):
        return self.carro

    def set_cliente(self,nuevo_carro):
        self.carro = nuevo_carro

    def get_tabla_texto(self):
        return self.tabla_texto  

    def set_tabla_texto(self,nueva_tabla_texto):
        self.tabla_texto = nueva_tabla_texto

    def registrar_entrada(self,cliente,carro):
     self.cliente = cliente
     self.carro = carro
     hora = datetime.now()
     self.fecha_entrada = hora.date()
     self.hora_entrada = hora.time()
     self.estado = "ocupado"

    def registrar_salida(self, buscar_placa):
     if self.estado == "ocuapado" and self.carro.get_placa() == buscar_placa:
         
         hora = datetime.now()
         self.hora_salida = hora.time()
         self.estado = "Libre"

    def guardar(self):
        self.texto_tabla += f"\n_puesto: {self.puesto}" | |  estado: {self.estado} | | fecha entrada: {self.fecha_entrada} | | hora entrada: {self.hora_entrada} | | hora salida: {self.hora_salida}"

    def mostrar_info(self):
        print (self.texto_tabla)
        
