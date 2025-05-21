from src.Modelo.ConsultaFinanzas import ConsultaFinanzas
from src.Vista.ConsultaFinanzasVista import ConsultaFinanzasVista

class FinanzasController:

    def __init__(self):
        self.modelo = ConsultaFinanzas()
        self.vista = ConsultaFinanzasVista(self)
        self.vista.after(0, self.actualizar_datos)  # Actualizar al iniciar
        self.vista.mainloop()

    def actualizar_datos(self):
        datos = self.modelo.obtener_finanzas()
        ingresos, gastos, ganancia, recuperado = self.modelo.calcular_totales(datos)
        self.vista.mostrar_datos(datos, ingresos, gastos, ganancia, recuperado)

if __name__ == "__main__":
    FinanzasController()
