import customtkinter as ctk

class Venta:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x600")
        self.app.title("Venta")

        for i in range(3):
            self.app.grid_columnconfigure(i, weight=1)
        for i in range(10):
            self.app.grid_rowconfigure(i, weight=1)

        self.etiqueta_titulo = ctk.CTkLabel(self.app, text="Venta", font=("Arial", 36, "bold"), text_color="white")
        self.etiqueta_titulo.grid(row=0, column=1, pady=20, sticky="ew")

        self.etiqueta_seleccion = ctk.CTkLabel(self.app, text="Seleccione su producto", font=("Arial", 16, "bold"))
        self.etiqueta_seleccion.grid(row=1, column=1, pady=(0, 5), sticky="n")

        self.combo_productos = ctk.CTkComboBox(self.app, values=["Malangas", "Maicitos"], width=200)
        self.combo_productos.grid(row=2, column=1, pady=(0, 20), sticky="n")

        self.etiqueta_cantidad = ctk.CTkLabel(self.app, text="Cantidad", font=("Arial", 16, "bold"))
        self.etiqueta_cantidad.grid(row=3, column=1, pady=(10, 5), sticky="n")

        self.entrada_cantidad = ctk.CTkEntry(self.app, placeholder_text="Ingrese la cantidad", width=200)
        self.entrada_cantidad.grid(row=4, column=1, pady=(0, 20), sticky="n")

        self.etiqueta_sabor = ctk.CTkLabel(self.app, text="Seleccione el sabor", font=("Arial", 16, "bold"))
        self.etiqueta_sabor.grid(row=5, column=1, pady=(10, 5), sticky="n")

        self.combo_sabor = ctk.CTkComboBox(self.app, values=["Queso", "Picante", "Natural", "Tocineta"], width=200)
        self.combo_sabor.grid(row=6, column=1, pady=(0, 20), sticky="n")

        self.boton_venta = ctk.CTkButton(self.app, text="Vender", font=("Arial", 18, "bold"), fg_color="green", text_color="white", width=150)
        self.boton_venta.grid(row=7, column=1, pady=30, sticky="n")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    venta = Venta(app)
    app.mainloop()
