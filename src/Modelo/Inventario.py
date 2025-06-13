# src/Modelo/Inventario.py
from src.DAO.InventarioDAO import crear_inventario, actualizar_inventario, obtener_cantidad_existente
from src.DAO.ProductosDAO import obtener_productos_id_nombre,obtener_precio_compra
from src.DAO.SaboresDAO import obtener_sabores_por_producto,obtener_nombre_sabor_por_id
from src.Modelo.Finanza import agregar_finanza
from src.Modelo.Validaciones import validar_numero, obtener_fecha_exacta_actual
from src.Modelo.Sesion import Sesion

class Inventario:
    def __init__(self, id_producto, id_sabor, cantidad):
        self.id_producto = id_producto
        self.id_sabor = id_sabor
        self.cantidad = cantidad
        self.fecha = obtener_fecha_exacta_actual()
        self.usuario=Sesion.obtener_usuario()

    def guardar(self):
        valido, mensaje = validar_numero(self.cantidad)
        if not valido:
            return False, mensaje

        crear_inventario(self.id_producto, self.id_sabor, self.cantidad, self.fecha,self.usuario)
        return True, "Producto registrado correctamente"

    def actualizar(self):
        valido, mensaje = validar_numero(self.cantidad)
        if not valido:
            return False, mensaje

        cantidad_existente, id_inventario = obtener_cantidad_existente(self.id_producto, self.id_sabor)
        nueva_cantidad = cantidad_existente + self.cantidad

        if id_inventario:
            actualizar_inventario(id_inventario, self.id_producto, self.id_sabor, nueva_cantidad, self.fecha,self.usuario)
            return True, "Producto agregado correctamente"
        else:
            return False, "El inventario no existe para este producto y sabor."

    def mermar_cantidad(self):
        # Validar cantidad
        valido, mensaje = validar_numero(self.cantidad)
        if not valido:
            return False, mensaje

        # Obtener inventario actual
        cantidad_existente, id_inventario = obtener_cantidad_existente(self.id_producto, self.id_sabor)

        if id_inventario is None:
            return False, "No hay inventario registrado para este producto y sabor."

        if self.cantidad > cantidad_existente:
            return False, "No hay suficiente inventario para realizar la merma."

        # Actualizar inventario
        nueva_cantidad = cantidad_existente - self.cantidad
        actualizar_inventario(id_inventario, self.id_producto, self.id_sabor, nueva_cantidad, self.fecha,self.usuario)

        # Registrar en finanzas
        precio_unitario = obtener_precio_compra(self.id_producto)
        perdida = self.cantidad * precio_unitario
        fecha = obtener_fecha_exacta_actual()

        # Obtener lista de productos y buscar nombre del producto actual
        productos = obtener_productos_id_nombre()
        nombre_producto = None
        for id_prod, nombre in productos:
            if id_prod == self.id_producto:
                nombre_producto = nombre
                break
        if nombre_producto is None:
            nombre_producto = "Producto desconocido"

        # Obtener nombre del sabor si existe
        nombre_sabor = obtener_nombre_sabor_por_id(self.id_sabor) if self.id_sabor else None

        # Generar descripción de la merma
        descripcion = f"Merma de {self.cantidad} {nombre_producto} {nombre_sabor or ''}".strip()
        agregar_finanza( "Merma", perdida, descripcion,fecha,self.usuario)

        return True, "Producto mermado correctamente"

    @staticmethod
    def obtener_productos():
        return obtener_productos_id_nombre()

    @staticmethod
    def obtener_sabores(id_producto):
        return obtener_sabores_por_producto(id_producto)
