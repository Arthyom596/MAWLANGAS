import customtkinter as ctk
from src.Controlador.VentaControlador import ControladorVenta

class Venta:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x600")
        self.app.title("Venta")

        # Configurar columnas y filas de la grilla
        for i in range(3):
            self.app.grid_columnconfigure(i, weight=1)
        for i in range(9):
            self.app.grid_rowconfigure(i, weight=1)

        # Título
        self.etiqueta_titulo = ctk.CTkLabel(self.app, text="Venta", font=("Arial", 36, "bold"), text_color="white")
        self.etiqueta_titulo.grid(row=0, column=1, pady=20, sticky="ew")

        # Selección de producto
        self.etiqueta_seleccion = ctk.CTkLabel(self.app, text="Seleccione su producto", font=("Arial", 16, "bold"))
        self.etiqueta_seleccion.grid(row=1, column=1, pady=(0, 5), sticky="n")

        self.combo_productos = ctk.CTkComboBox(self.app, values=[], width=200, command=self.actualizar_sabores)
        self.combo_productos.set("Producto")
        self.combo_productos.grid(row=2, column=1, pady=(0, 20), sticky="n")

        # Cantidad
        self.etiqueta_cantidad = ctk.CTkLabel(self.app, text="Cantidad", font=("Arial", 16, "bold"))
        self.etiqueta_cantidad.grid(row=3, column=1, pady=(10, 5), sticky="n")

        self.entrada_cantidad = ctk.CTkEntry(self.app, placeholder_text="Ingrese la cantidad", width=200)
        self.entrada_cantidad.grid(row=4, column=1, pady=(0, 20), sticky="n")

        # Toggle de sabor
        self.switch_sabor = ctk.CTkSwitch(self.app, text="¿Requiere sabor?", command=self.toggle_sabor)
        self.switch_sabor.grid(row=5, column=1, pady=(0, 10), sticky="n")

        # Sabor
        self.etiqueta_sabor = ctk.CTkLabel(self.app, text="Seleccione el sabor", font=("Arial", 16, "bold"))
        self.etiqueta_sabor.grid(row=6, column=1, pady=(10, 5), sticky="n")

        self.combo_sabor = ctk.CTkComboBox(self.app, values=[], width=200)
        self.combo_sabor.set("Sabor")
        self.combo_sabor.grid(row=7, column=1, pady=(0, 20), sticky="n")

        # Dinámica
        self.etiqueta_dinamica = ctk.CTkLabel(self.app, text="", font=("Arial", 16, "bold"))
        self.etiqueta_dinamica.grid(row=8, column=1)

        # Botón vender
        self.boton_venta = ctk.CTkButton(self.app, text="Vender", font=("Arial", 18, "bold"), fg_color="green", text_color="white", width=150)
        self.boton_venta.grid(row=9, column=1, pady=30, sticky="n")

        # Ocultar combo de sabor al inicio
        self.etiqueta_sabor.grid_remove()
        self.combo_sabor.grid_remove()

    def set_controlador(self, controlador):
        self.controlador = controlador
        self.controlador.vista = self

    def cargar_productos(self, productos):
        self.combo_productos.configure(values=productos)

    def cargar_sabores(self, sabores):
        self.combo_sabor.configure(values=sabores)

    def actualizar_sabores(self, event=None):
        producto_seleccionado = self.combo_productos.get()


        id_producto = self.controlador.obtener_id_producto()
        if id_producto:
            self.controlador.actualizar_sabores(id_producto)



    def toggle_sabor(self):
        if self.switch_sabor.get() == 1:
            self.etiqueta_sabor.grid()
            self.combo_sabor.grid()
        else:
            self.etiqueta_sabor.grid_remove()
            self.combo_sabor.grid_remove()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()

    venta = Venta(app)
    controlador = ControladorVenta(venta)
    venta.set_controlador(controlador)

    app.mainloop()
