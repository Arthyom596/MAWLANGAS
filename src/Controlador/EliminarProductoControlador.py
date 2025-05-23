import customtkinter as ctk
from src.Modelo.EliminarProducto import EliminarProducto
from src.Vista.Eliminar.EliminarProductoVista import EliminarProductoVista

class ProductoController:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.model = EliminarProducto()
        self.view = EliminarProductoVista()

        nombres = self.model.obtener_nombres_productos()
        self.view.combo_productos.configure(values=nombres)

        self.producto_actual = None

        self.view.boton_buscar.configure(command=self.buscar_producto)
        self.view.boton_eliminar.configure(command=self.eliminar_producto)

    def buscar_producto(self):
        nombre = self.view.combo_productos.get()
        if nombre not in self.model.id_por_nombre:
            self.view.mostrar_mensaje("Producto no encontrado.", "red")
            self.view.boton_eliminar.pack_forget()
            self.limpiar_datos()
            return

        datos = self.model.buscar_producto(nombre)
        if datos:
            self.producto_actual = datos
            self.view.labels_datos["ID"].configure(text=f"ID: {datos[0]}")
            self.view.labels_datos["Nombre"].configure(text=f"Nombre: {datos[1]}")
            self.view.labels_datos["Precio Compra"].configure(text=f"Precio Compra: ${datos[2]:.2f}")
            self.view.labels_datos["Precio Venta"].configure(text=f"Precio Venta: ${datos[3]:.2f}")
            self.view.boton_eliminar.pack(pady=20)
        else:
            self.view.mostrar_mensaje("Producto no encontrado.", "red")
            self.view.boton_eliminar.pack_forget()
            self.limpiar_datos()

    def eliminar_producto(self):
        if not self.producto_actual:
            return
        self.model.eliminar_producto(self.producto_actual[0])
        self.view.mostrar_mensaje("Producto eliminado exitosamente.", "green")
        self.view.boton_eliminar.pack_forget()
        self.producto_actual = None
        self.actualizar_combo()
        self.limpiar_datos()

    def actualizar_combo(self):
        nombres = self.model.obtener_nombres_productos()
        self.view.combo_productos.configure(values=nombres)
        self.view.combo_productos.set("")

    def limpiar_datos(self):
        for label in self.view.labels_datos.values():
            label.configure(text="")

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    app = ProductoController()
    app.run()
