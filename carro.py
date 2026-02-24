class carro:
    def __init__(self,carro,placa,tipo,color):
        self.carro = carro
        self.placa = placa
        self.tipo = tipo
        self.color = color
        


    def get_carro(self):
        return self.carro

    def set_carro(self,nuevo_carro):
        self.carro = nuevo_carro

    def get_placa(self):
        return self.placa

    def set_placa(self,nueva_placa):
        self.placa = nueva_placa

    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self,nuevo_tipo):
        self.tipo = nuevo_tipo

    def get_color(self):
        return self.color

    def set_color(self,nuevo_color):
        self.color = nuevo_color

    def imprimir_info(self):
        print(f"la placa del carro es: {self.placa}")
        print(f"el tipo del carro es : {self.tipo}")
        print(f"el color del carro es : {self.color}")
        


