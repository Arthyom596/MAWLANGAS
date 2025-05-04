
from src.Modelo.Producto import agregar_sabor, eliminar_ultimo_sabor, guardar_producto

class ProductoControlador:
    def __init__(self, vista): #El constructor espera a ProductoVista como parametro
        self.vista = vista #Se crea una instancia de ProductosVista
        self.sabores = [] #Se crea una lista vacia para los sabores

    def agregar_sabor(self, sabor):
        self.sabores, mensaje = agregar_sabor(sabor, self.sabores)
        self.vista.mostrar_mensaje(mensaje)
        self.vista.actualizar_textbox_sabores(self.sabores)
        self.vista.limpiar_entry_sabor()
        self.vista.actualizar_estado_boton(self.sabores)

    def eliminar_sabor(self):
        self.sabores = eliminar_ultimo_sabor(self.sabores)
        mensaje = "Último sabor eliminado." if self.sabores else "No hay sabores para eliminar."
        self.vista.mostrar_mensaje(mensaje)
        self.vista.actualizar_textbox_sabores(self.sabores)
        self.vista.actualizar_estado_boton(self.sabores)

    def guardar_producto(self, nombre, precio_compra, precio_venta, usar_sabores):
        sabores_a_guardar = self.sabores if usar_sabores else []

        if not nombre.strip():
            self.vista.mostrar_mensaje("El nombre no puede estar vacío")
            return

        exito, mensaje = guardar_producto(nombre, precio_compra, precio_venta, sabores_a_guardar)
        self.vista.mostrar_mensaje(mensaje)

        if exito:
            self.sabores.clear()
            self.vista.reiniciar_formulario()
            self.vista.actualizar_textbox_sabores(self.sabores)  # limpiar textbox
            self.vista.actualizar_estado_boton(self.sabores)
