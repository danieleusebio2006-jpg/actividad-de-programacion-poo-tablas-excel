class Numero:
    def __init__(self, numero):
        self.numero = numero

    def get_numero(self):
        return self.numero

    def set_numero(self, dato_numero):
        self.numero = dato_numero

    def mostrar_info(self):
        print(f"El numero es: {self.numero}")