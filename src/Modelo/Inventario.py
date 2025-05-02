from datetime import datetime
from src.DAO.InventarioDAO import crear_inventario, actualizar_inventario, obtener_cantidad_existente
from src.DAO.ProductosDAO import obtener_productos_id_nombre
from src.DAO.SaboresDAO import obtener_sabores_por_producto
from src.Modelo.Validaciones import validar_numero,obtener_fecha_exacta_actual

class Inventario:
    def __init__(self, id_producto, id_sabor, cantidad):
        self.id_producto = id_producto
        self.id_sabor = id_sabor
        self.cantidad = cantidad
        self.fecha = obtener_fecha_exacta_actual()

    def guardar(self):
        valido, mensaje = validar_numero(self.cantidad)
        if not valido:
            print(mensaje)
            return False

        crear_inventario(self.id_producto, self.id_sabor, self.cantidad, self.fecha)
        return True

    def actualizar(self):
        valido, mensaje = validar_numero(self.cantidad)
        if not valido:
            print(mensaje)
            return False

        cantidad_existente, id_inventario = obtener_cantidad_existente(self.id_producto, self.id_sabor)
        nueva_cantidad = cantidad_existente + self.cantidad
        if id_inventario:
            actualizar_inventario(id_inventario, self.id_producto, self.id_sabor, nueva_cantidad, self.fecha)
            return True
        else:
            print("El inventario no existe para este producto y sabor.")
            return False

    def mermar_cantidad(self):
        valido, mensaje = validar_numero(self.cantidad)
        if not valido:
            print(mensaje)
            return False

        cantidad_existente, id_inventario = obtener_cantidad_existente(self.id_producto, self.id_sabor)

        if id_inventario is None:
            print("No hay inventario registrado para este producto y sabor.")
            return False

        if self.cantidad > cantidad_existente:
            print("Error: No hay suficiente inventario para realizar la merma.")
            return False

        nueva_cantidad = cantidad_existente - self.cantidad
        actualizar_inventario(id_inventario, self.id_producto, self.id_sabor, nueva_cantidad, self.fecha)
        return True

    @staticmethod
    def obtener_productos():
        return obtener_productos_id_nombre()

    @staticmethod
    def obtener_sabores(id_producto):
        return obtener_sabores_por_producto(id_producto)
