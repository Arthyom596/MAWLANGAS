# src/Controlador/FinanzaControlador.py

from src.Modelo.Finanza import Finanza

class FinanzaControlador:
    def __init__(self, vista):
        self.vista = vista
        self.finanza = Finanza()

        # Asociar botones con métodos del controlador
        self.vista.btn_agregar_ingreso.configure(command=self.agregar_ingreso)
        self.vista.btn_agregar_gasto.configure(command=self.agregar_gasto)

    def agregar_ingreso(self):
        monto = self.vista.entrada_ingreso.get()
        descripcion = self.vista.entrada_concepto_ingreso.get()

        exito, mensaje = self.finanza.agregar_ingreso(monto, descripcion)
        self.vista.etiqueta_dinamica.configure(text=mensaje)

        if exito:
            self.vista.entrada_ingreso.delete(0, "end")
            self.vista.entrada_concepto_ingreso.delete(0, "end")

    def agregar_gasto(self):
        monto = self.vista.entrada_gasto.get()
        descripcion = self.vista.entrada_concepto_gasto.get()

        exito, mensaje = self.finanza.agregar_gasto(monto, descripcion)
        self.vista.etiqueta_dinamica.configure(text=mensaje)

        if exito:
            self.vista.entrada_gasto.delete(0, "end")
            self.vista.entrada_concepto_gasto.delete(0, "end")
