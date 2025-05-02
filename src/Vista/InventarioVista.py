import customtkinter as ctk
from src.Controlador.InventarioControlador import InventarioControlador
from src.Modelo.Inventario import InventarioModelo


class InventarioVista:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x600")
        self.app.title("Administración del Inventario")

        # Diccionarios auxiliares para mapear nombres a IDs
        self.productos_dict = {}
        self.sabores_dict = {}

        for i in range(3):
            self.app.grid_columnconfigure(i, weight=1)
        for i in range(9):
            self.app.grid_rowconfigure(i, weight=1)

        # Etiqueta principal
        self.etiqueta_titulo = ctk.CTkLabel(self.app, text="Administración del Inventario", font=("Arial", 36, "bold"))
        self.etiqueta_titulo.grid(row=0, column=1, pady=10, sticky="n")

        # Sección de selección de producto
        self.etiqueta_producto = ctk.CTkLabel(self.app, text="Escoja el producto:", font=("Arial", 16))
        self.etiqueta_producto.grid(row=1, column=1, sticky="n", pady=5)

        self.combo_producto = ctk.CTkComboBox(self.app, values=[], width=200, font=("Arial", 14))
        self.combo_producto.grid(row=2, column=1, pady=5)
        self.combo_producto.set("Producto")

        # Sección para agregar productos
        self.etiqueta_agregar = ctk.CTkLabel(self.app, text="Agregar Productos", font=("Arial", 18, "bold"))
        self.etiqueta_agregar.grid(row=3, column=1, pady=10, sticky="n")

        self.frame_agregar = ctk.CTkFrame(self.app, fg_color="transparent")
        self.frame_agregar.grid(row=4, column=1, pady=5)

        self.combo_sabores_agregar = ctk.CTkComboBox(self.frame_agregar, values=[], width=140, font=("Arial", 14))
        self.combo_sabores_agregar.grid(row=0, column=0, padx=5)
        self.combo_sabores_agregar.set("Sabor")

        self.entrada_cantidad_agregar = ctk.CTkEntry(self.frame_agregar, placeholder_text="Cantidad", width=100, font=("Arial", 14))
        self.entrada_cantidad_agregar.grid(row=0, column=1, padx=5)

        self.boton_agregar = ctk.CTkButton(self.frame_agregar, text="Agregar", width=100, font=("Arial", 14, "bold"))
        self.boton_agregar.grid(row=0, column=2, padx=5)

        # Sección para mermar productos
        self.etiqueta_mermar = ctk.CTkLabel(self.app, text="Mermar Productos", font=("Arial", 18, "bold"))
        self.etiqueta_mermar.grid(row=5, column=1, pady=10, sticky="n")

        self.frame_mermar = ctk.CTkFrame(self.app, fg_color="transparent")
        self.frame_mermar.grid(row=6, column=1, pady=5)

        self.combo_sabores_mermar = ctk.CTkComboBox(self.frame_mermar, values=[], width=140, font=("Arial", 14))
        self.combo_sabores_mermar.grid(row=0, column=0, padx=5)
        self.combo_sabores_mermar.set("Sabor")

        self.entrada_cantidad_mermar = ctk.CTkEntry(self.frame_mermar, placeholder_text="Cantidad", width=100, font=("Arial", 14))
        self.entrada_cantidad_mermar.grid(row=0, column=1, padx=5)

        self.boton_mermar = ctk.CTkButton(self.frame_mermar, text="Mermar", width=100, font=("Arial", 14, "bold"))
        self.boton_mermar.grid(row=0, column=2, padx=5)

        # Etiqueta para mensajes
        self.etiqueta_mensaje = ctk.CTkLabel(self.app, text="", font=("Arial", 14))
        self.etiqueta_mensaje.grid(row=8, column=1, pady=10, sticky="n")

    # Métodos para enlazar funciones externas
    def set_controlador(self, controlador):
        self.controlador = controlador
        self.combo_producto.configure(command=self.controlador.actualizar_sabores)
        self.boton_agregar.configure(command=self.controlador.agregar_producto)
        self.boton_mermar.configure(command=self.controlador.mermar_producto)

    def set_productos(self, productos: list):
        # productos = [(id, nombre), ...]
        self.productos_dict = {nombre: id_ for id_, nombre in productos}
        nombres = list(self.productos_dict.keys())
        self.combo_producto.configure(values=nombres)
        self.combo_producto.set("Producto")

    def set_sabores(self, sabores: list):
        # sabores = [(id, nombre), ...]
        self.sabores_dict = {nombre: id_ for id_, nombre in sabores}
        nombres = list(self.sabores_dict.keys())
        self.combo_sabores_agregar.configure(values=nombres)
        self.combo_sabores_agregar.set("Sabor")
        self.combo_sabores_mermar.configure(values=nombres)
        self.combo_sabores_mermar.set("Sabor")

    def mostrar_mensaje(self, texto: str, color="lightgreen"):
        self.etiqueta_mensaje.configure(text=texto, text_color=color)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = InventarioVista(root)
    controlador = InventarioControlador(app)  # Conecta vista y lógica
    root.mainloop()
