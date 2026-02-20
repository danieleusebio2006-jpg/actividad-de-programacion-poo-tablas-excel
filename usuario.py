class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre 
        self.cedula = cedula
        
    def get_nombre(self):
        return self.nombre
        
    def set_nombre(self,nombre):
        self.nombre = nombre
            
    def get_cedula(self):
        return self.cedula
    
    def get_cedula(self):
        return self.cedula
            
    def set_cedula(self, cedula):
        self.cedula = cedula
                
    def imprimir_info(self):
        return f"usuario: {self.nombre}, cedula: {self.cedula}"
        