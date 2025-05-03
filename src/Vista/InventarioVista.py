import customtkinter as ctk
from src.Controlador.InventarioControlador import InventarioControlador
from src.Modelo.Inventario import Inventario


class InventarioVista:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x600")
        self.app.title("Administración del Inventario")

        # Diccionarios auxiliares
        self.productos_dict = {}
        self.sabores_dict = {}

        for i in range(3):
            self.app.grid_columnconfigure(i, weight=1)
        for i in range(10):
            self.app.grid_rowconfigure(i, weight=1)

        # Título
        self.etiqueta_titulo = ctk.CTkLabel(self.app, text="Administración del Inventario", font=("Arial", 32, "bold"))
        self.etiqueta_titulo.grid(row=0, column=1, pady=10, sticky="n")

        # Producto
        self.etiqueta_producto = ctk.CTkLabel(self.app, text="Seleccione producto:", font=("Arial", 16))
        self.etiqueta_producto.grid(row=1, column=1, sticky="s", pady=5)

        self.combo_producto = ctk.CTkComboBox(self.app, values=[], width=200, font=("Arial", 14))
        self.combo_producto.grid(row=2, column=1, pady=5)
        self.combo_producto.set("Producto")

        # Switch de sabor
        self.switch_usar_sabor = ctk.CTkSwitch(self.app, text="¿Usa sabor?", font=("Arial", 14), command=self.toggle_sabor)
        self.switch_usar_sabor.grid(row=3, column=1, pady=5)
        self.switch_usar_sabor.select()

        # Agregar producto
        self.etiqueta_agregar = ctk.CTkLabel(self.app, text="Agregar Productos", font=("Arial", 18, "bold"))
        self.etiqueta_agregar.grid(row=4, column=1, pady=5)

        self.frame_agregar = ctk.CTkFrame(self.app, fg_color="transparent")
        self.frame_agregar.grid(row=5, column=1, pady=5)

        self.combo_sabores_agregar = ctk.CTkComboBox(self.frame_agregar, values=[], width=140, font=("Arial", 14))
        self.combo_sabores_agregar.grid(row=0, column=0, padx=5)
        self.combo_sabores_agregar.set("Sabor")

        self.entrada_cantidad_agregar = ctk.CTkEntry(self.frame_agregar, placeholder_text="Cantidad", width=100, font=("Arial", 14))
        self.entrada_cantidad_agregar.grid(row=0, column=1, padx=5)

        self.boton_agregar = ctk.CTkButton(self.frame_agregar, text="Agregar", width=100, font=("Arial", 14, "bold"))
        self.boton_agregar.grid(row=0, column=2, padx=5)

        # Mermar producto
        self.etiqueta_mermar = ctk.CTkLabel(self.app, text="Mermar Productos", font=("Arial", 18, "bold"))
        self.etiqueta_mermar.grid(row=6, column=1, pady=5)

        self.frame_mermar = ctk.CTkFrame(self.app, fg_color="transparent")
        self.frame_mermar.grid(row=7, column=1, pady=5)

        self.combo_sabores_mermar = ctk.CTkComboBox(self.frame_mermar, values=[], width=140, font=("Arial", 14))
        self.combo_sabores_mermar.grid(row=0, column=0, padx=5)
        self.combo_sabores_mermar.set("Sabor")

        self.entrada_cantidad_mermar = ctk.CTkEntry(self.frame_mermar, placeholder_text="Cantidad", width=100, font=("Arial", 14))
        self.entrada_cantidad_mermar.grid(row=0, column=1, padx=5)

        self.boton_mermar = ctk.CTkButton(self.frame_mermar, text="Mermar", width=100, font=("Arial", 14, "bold"))
        self.boton_mermar.grid(row=0, column=2, padx=5)

        # Mensajes
        self.etiqueta_mensaje = ctk.CTkLabel(self.app, text="", font=("Arial", 14))
        self.etiqueta_mensaje.grid(row=9, column=1, pady=10, sticky="n")

    def toggle_sabor(self):
        estado = self.switch_usar_sabor.get()
        if estado:
            self.combo_sabores_agregar.grid()
            self.combo_sabores_mermar.grid()
        else:
            self.combo_sabores_agregar.grid_remove()
            self.combo_sabores_mermar.grid_remove()

    def set_controlador(self, controlador):
        self.controlador = controlador
        self.combo_producto.configure(command=self.controlador.actualizar_sabores)
        self.boton_agregar.configure(command=self.controlador.agregar_producto)
        self.boton_mermar.configure(command=self.controlador.mermar_producto)

    def set_productos(self, productos: list):
        self.productos_dict = {nombre: id_ for id_, nombre in productos}
        nombres = list(self.productos_dict.keys())
        self.combo_producto.configure(values=nombres)
        self.combo_producto.set("Producto")

    def set_sabores(self, sabores: list):
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
    controlador = InventarioControlador(app)
    root.mainloop()
