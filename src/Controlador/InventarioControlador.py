from src.Modelo.Inventario import Inventario

class InventarioControlador:
    def __init__(self, vista):
        self.vista = vista
        self.vista.set_controlador(self)
        self.productos = Inventario.obtener_productos()
        self.vista.set_productos(self.productos)

    def obtener_id_producto(self):
        seleccionado = self.vista.combo_producto.get()
        return self.vista.productos_dict.get(seleccionado)

    def actualizar_sabores(self, _=None):
        id_producto = self.obtener_id_producto()
        if id_producto is not None:
            sabores = Inventario.obtener_sabores(id_producto)
            self.vista.set_sabores(sabores)

    def agregar_producto(self):
        id_producto = self.obtener_id_producto()
        nombre_sabor = self.vista.combo_sabores_agregar.get()
        id_sabor = self.vista.sabores_dict.get(nombre_sabor)
        cantidad = self.obtener_cantidad(self.vista.entrada_cantidad_agregar.get())

        if None in (id_producto, id_sabor, cantidad):
            self.vista.mostrar_mensaje("Faltan datos", "red")
            return

        modelo = Inventario(id_producto, id_sabor, cantidad)
        if modelo.actualizar():
            self.vista.mostrar_mensaje("Producto agregado correctamente")
        else:
            if modelo.guardar():
                self.vista.mostrar_mensaje("Producto registrado correctamente")
            else:
                self.vista.mostrar_mensaje("Error al guardar producto", "red")

    def mermar_producto(self):
        id_producto = self.obtener_id_producto()
        nombre_sabor = self.vista.combo_sabores_mermar.get()
        id_sabor = self.vista.sabores_dict.get(nombre_sabor)
        cantidad = self.obtener_cantidad(self.vista.entrada_cantidad_mermar.get())

        if None in (id_producto, id_sabor, cantidad):
            self.vista.mostrar_mensaje("Faltan datos", "red")
            return

        modelo = Inventario(id_producto, id_sabor, cantidad)
        if modelo.mermar_cantidad():
            self.vista.mostrar_mensaje("Producto mermado correctamente")
        else:
            self.vista.mostrar_mensaje("No se pudo mermar", "red")

    def obtener_cantidad(self, entrada: str):
        try:
            return int(entrada)
        except ValueError:
            return None
