
from src.Modelo.Validaciones import validar_numero
from src.DAO.VentasDAO import crear_venta
import datetime


class Venta:
    def __init__(self):
       pass

    def realizar_venta(self,cantidad):
        cantidad_valida,resultado=validar_numero(cantidad)
        if not cantidad_valida:
            return False,resultado

        fecha=datetime.datetime.today().isoformat()


