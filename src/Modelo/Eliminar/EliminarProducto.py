
from src.DAO.ProductosDAO import obtener_productos_id_nombre, buscar_producto, eliminar_producto

class EliminarProducto:
    def obtener_nombres_productos(self):
        productos = obtener_productos_id_nombre()
        self.id_por_nombre = {nombre: id_ for id_, nombre in productos}
        return [nombre for _, nombre in productos]

    def buscar_producto(self, nombre):
        if nombre not in self.id_por_nombre:
            return None
        return buscar_producto(nombre)

    def eliminar_producto(self, id_producto):
        eliminar_producto(id_producto)
