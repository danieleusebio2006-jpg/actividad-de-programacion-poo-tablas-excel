class Calculadora:
    def __init__(self, numero1, numero2, fecha=None):
        self.numero1 = numero1
        self.numero2 = numero2
        self.fecha = fecha
        self.tipo_operacion = ""
        self.resultado = ""
        self.texto_tabla = ""
        self.resultado_suma = self.numero1.get_numero() + self.numero2.get_numero()
        self.resultado_resta = self.numero1.get_numero() - self.numero2.get_numero()
        self.resultado_multiplicacion = self.numero1.get_numero() * self.numero2.get_numero()
        self.resultado_division = self.numero1.get_numero() / self.numero2.get_numero() if self.numero2.get_numero() != 0 else "Error: División por cero"
          
    def get_fecha(self):
        return self.fecha
    def set_fecha(self,fecha):
        self.fecha = fecha
    
    def hacer_operacion(self,operacion):
        self.tipo_operacion = operacion
        if operacion == "suma":
            self.resultado = "Resultado de la suma"
        elif operacion == "resta":
            self.resultado = "Resultado de la resta"
        elif operacion == "multiplicacion":
            self.resultado = "Resultado de la multiplicación"
        elif operacion == "division":
            self.resultado = "Resultado de la división"
        else:
            self.resultado = "Operación no válida"
        return self.resultado
    
    def guardar_info(self, obj_usuario):
        self.texto_tabla += (
            f"{obj_usuario.get_cedula():<12}"
            f"{obj_usuario.get_nombre():<20}"
            f"{self.tipo_operacion:<15}"
            f"{self.resultado:<20}"
            f"\n"
        )
    
    def guardar_info(self, obj_usuario, numero1, numero2):
        self.info_tabla += (
            f"{obj_usuario.get_cedula():<30}"
            f"{obj_usuario.get_nombre():<15}"
            f"{self.tipo_operacion:<15}"
            f"{self.resultado:<30}"
            f"{numero1:<10}"
            f"{numero2:<8}"
            f"\n"
        )
    
    def imprimir_info(self):
        print("Cédula     Nombre              Operación       Resultado            Número 1   Número 2")
        print(self.info_tabla)
        