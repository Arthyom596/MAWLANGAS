import customtkinter as ctk
from customtkinter import CTkFrame

from src.Controlador.VentaControlador import ControladorVenta

class Venta:
    def __init__(self, parent,controlador_maestro):
        self.app = CTkFrame(parent)
        self.app.pack(fill="both", expand=True)
        for i in range(3):
            self.app.grid_columnconfigure(i, weight=1)
        for i in range(9):
            self.app.grid_rowconfigure(i, weight=1)

        self.etiqueta_titulo = ctk.CTkLabel(self.app, text="Venta", font=("Arial", 36, "bold"), text_color="white")
        self.etiqueta_titulo.grid(row=0, column=1, pady=20, sticky="ew")

        self.etiqueta_seleccion = ctk.CTkLabel(self.app, text="Seleccione su producto", font=("Arial", 16, "bold"))
        self.etiqueta_seleccion.grid(row=1, column=1, pady=(0, 5), sticky="n")

        self.combo_productos = ctk.CTkComboBox(self.app, values=[], width=200, command=self.actualizar_sabores)
        self.combo_productos.set("Producto")
        self.combo_productos.grid(row=2, column=1, pady=(0, 20), sticky="n")

        self.etiqueta_cantidad = ctk.CTkLabel(self.app, text="Cantidad", font=("Arial", 16, "bold"))
        self.etiqueta_cantidad.grid(row=3, column=1, pady=(10, 5), sticky="n")

        self.entrada_cantidad = ctk.CTkEntry(self.app, placeholder_text="Ingrese la cantidad", width=200)
        self.entrada_cantidad.grid(row=4, column=1, pady=(0, 20), sticky="n")

        self.switch_sabor = ctk.CTkSwitch(self.app, text="¿Requiere sabor?", command=self.toggle_sabor)
        self.switch_sabor.grid(row=5, column=1, pady=(0, 10), sticky="n")

        self.etiqueta_sabor = ctk.CTkLabel(self.app, text="Seleccione el sabor", font=("Arial", 16, "bold"))
        self.etiqueta_sabor.grid(row=6, column=1, pady=(10, 5), sticky="n")

        self.combo_sabor = ctk.CTkComboBox(self.app, values=[], width=200)
        self.combo_sabor.set("Sabor")
        self.combo_sabor.grid(row=7, column=1, pady=(0, 20), sticky="n")

        self.etiqueta_dinamica = ctk.CTkLabel(self.app, text="", font=("Arial", 16, "bold"))
        self.etiqueta_dinamica.grid(row=8, column=1)

        self.boton_venta = ctk.CTkButton(self.app, text="Vender", font=("Arial", 18, "bold"), fg_color="green", text_color="white", width=150)
        self.boton_venta.grid(row=9, column=1, pady=30, sticky="n")



    def set_controlador(self, controlador):
        self.controlador = controlador
        self.controlador.vista = self

    def cargar_productos(self, productos):
        self.combo_productos.configure(values=productos)

    def cargar_sabores(self, sabores):
        # Limpia y recarga los sabores correctamente
        self.combo_sabor.set("")
        self.combo_sabor.configure(values=[])
        self.combo_sabor.configure(values=sabores)
        self.combo_sabor.set("Sabor")

        if sabores:
            self.switch_sabor.configure(state="normal")
            self.switch_sabor.select()
            self.toggle_sabor()
        else:
            self.switch_sabor.deselect()
            self.switch_sabor.configure(state="disabled")
            self.toggle_sabor()

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
