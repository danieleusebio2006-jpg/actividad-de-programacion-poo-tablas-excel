class usuario:
    def __init__(self,nombre,cedula,tipo_usuario):
        self.nombre_usuario = nombre
        self.cedula_usuario = cedula
        self.tipo_usuario = tipo_usuario

    def get_nombre_usuario(self):
        return self.nombre_usuario

    def get_cedula_usuario(self):
        return self.cedula_usuario

    def set_cedula_usuario (self,nueva_cedula):
        self.cedula_usuario = nueva_cedula

    def get_tipo_usuario(self):
        return self.tipo_usuario

    def set_tipo_usuario(self,nuevo_usuario):
        self.tipo_usuario = nuevo_usuario

    def imprimir_datos(self):
        print(f"nombre del usuario: {self.nombre_usuario}")
        print(f"cedula del usuario: {self.cedula_usuario}")