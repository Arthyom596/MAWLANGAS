from src.DAO.FinanzaDAO import consultar_finanzas

class ConsultaFinanzas:

    def obtener_finanzas(self):
        return consultar_finanzas()

    def calcular_totales(self, datos):
        ingresos = 0
        gastos = 0

        for fila in datos:
            _, _, tipo, monto, _ = fila
            if tipo.lower() == "venta":
                ingresos += monto
            elif tipo.lower() == "inversion":
                gastos += monto

        ganancia = ingresos - gastos
        recuperado = gastos if ingresos >= gastos else ingresos

        return ingresos, gastos, ganancia, recuperado
