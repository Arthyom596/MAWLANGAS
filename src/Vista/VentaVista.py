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
        for i in range(8):
            self.app.grid_rowconfigure(i, weight=1)

        # Crear etiquetas y campos
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

        self.etiqueta_sabor = ctk.CTkLabel(self.app, text="Seleccione el sabor", font=("Arial", 16, "bold"))
        self.etiqueta_sabor.grid(row=5, column=1, pady=(10, 5), sticky="n")

        self.combo_sabor = ctk.CTkComboBox(self.app, values=[], width=200)
        self.combo_sabor.set("Sabor")
        self.combo_sabor.grid(row=6, column=1, pady=(0, 20), sticky="n")

        self.etiqueta_dinamica = ctk.CTkLabel(self.app, text="", font=("Arial", 16, "bold"))
        self.etiqueta_dinamica.grid(row=7, column=1)

        self.boton_venta = ctk.CTkButton(self.app, text="Vender", font=("Arial", 18, "bold"), fg_color="green", text_color="white", width=150)
        self.boton_venta.grid(row=8, column=1, pady=30, sticky="n")

    def set_controlador(self, controlador):
        self.controlador = controlador
        self.controlador.vista = self  # Establece la vista en el controlador

    def cargar_productos(self, productos):
        self.combo_productos.configure(values=productos)

    def cargar_sabores(self, sabores):
        self.combo_sabor.configure(values=sabores)

    def actualizar_sabores(self, event=None):
        # Esta es la función que se ejecutará cuando el usuario seleccione un producto
        producto_seleccionado = self.combo_productos.get()
        print(f"[DEBUG] Producto seleccionado: {producto_seleccionado}")

        # Obtener ID del producto basado en su nombre
        id_producto = self.controlador.obtener_id_producto()

        if id_producto:
            # Llamamos al controlador para cargar los sabores del producto seleccionado
            self.controlador.actualizar_sabores(
                id_producto)  # Llama al controlador para cargar los sabores del producto seleccionado
        else:
            print("[DEBUG] Producto seleccionado no válido.")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()

    # Crear la vista
    venta = Venta(app)

    # Instanciar el controlador y pasar la vista como argumento
    controlador = ControladorVenta(venta)

    # Asegúrate de que el controlador tiene acceso a la vista
    venta.set_controlador(controlador)

    app.mainloop()
