import datetime
from src.DAO.FinanzaDAO import agregar_finanza
from src.Modelo.Validaciones import validar_numero, validar_descripcion, obtener_fecha_exacta_actual
from src.Modelo.Sesion import Sesion


class Finanza:
    def __init__(self):
        pass


    def agregar_ingreso(self, monto, descripcion):
        monto_valido, resultado_monto = validar_numero(monto)
        if not monto_valido:
            return False, resultado_monto

        descripcion_valida, resultado_descripcion = validar_descripcion(descripcion)
        if not descripcion_valida:
            return False, resultado_descripcion

        fecha = obtener_fecha_exacta_actual()
        tipo = "Ingreso"
        self.usuario = Sesion.obtener_usuario()

        agregar_finanza(tipo, float(monto), descripcion,fecha,self.usuario)
        return True, "Ingreso registrado correctamente"

    def agregar_gasto(self, monto, descripcion):
        monto_valido, resultado_monto = validar_numero(monto)
        if not monto_valido:
            return False, resultado_monto

        descripcion_valida, resultado_descripcion = validar_descripcion(descripcion)
        if not descripcion_valida:
            return False, resultado_descripcion

        fecha = obtener_fecha_exacta_actual()
        tipo = "Gasto"
        self.usuario = Sesion.obtener_usuario()
        agregar_finanza( tipo, float(monto), descripcion,fecha,self.usuario)
        return True, "Gasto registrado correctamente"
