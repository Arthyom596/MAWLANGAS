import datetime
from src.DAO.FinanzaDAO import agregar_finanza
from src.Modelo.Validaciones import validar_numero, validar_descripcion

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

        fecha = datetime.datetime.today().isoformat()
        tipo = "Ingreso"
        agregar_finanza(fecha, tipo, float(monto), descripcion)
        return True, "Ingreso registrado correctamente"

    def agregar_gasto(self, monto, descripcion):
        monto_valido, resultado_monto = validar_numero(monto)
        if not monto_valido:
            return False, resultado_monto

        descripcion_valida, resultado_descripcion = validar_descripcion(descripcion)
        if not descripcion_valida:
            return False, resultado_descripcion

        fecha = datetime.datetime.today().isoformat()
        tipo = "Gasto"
        agregar_finanza(fecha, tipo, float(monto), descripcion)
        return True, "Gasto registrado correctamente"
