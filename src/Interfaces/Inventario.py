import customtkinter as ctk

class AdministracionInventario:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x600")
        self.app.title("Administración del Inventario")

        for i in range(3):
            self.app.grid_columnconfigure(i, weight=1)

        for i in range(9):
            self.app.grid_rowconfigure(i, weight=1)

        self.opciones_producto = ["Malangas", "Maicitos"]
        self.sabores_malanga = ["Takis Rojo", "Takis azul", "Adobadas", "Habanero", "Especias", "Jalapeño"]
        self.sabores_maicito = ["Ranchero", "Queso", "Takis", "Jalapeño", "Natural"]

        self.actualizar_sabores("Malangas")

        self.etiqueta_titulo = ctk.CTkLabel(self.app, text="Administración del Inventario", font=("Arial", 36, "bold"))
        self.etiqueta_titulo.grid(row=0, column=1, pady=10, sticky="n")

        self.etiqueta_producto = ctk.CTkLabel(self.app, text="Escoja el producto:", font=("Arial", 16))
        self.etiqueta_producto.grid(row=1, column=1, sticky="n", pady=5)

        self.combo_producto = ctk.CTkComboBox(self.app, values=self.opciones_producto, command=self.actualizar_sabores, width=200, font=("Arial", 14))
        self.combo_producto.grid(row=2, column=1, pady=5)
        self.combo_producto.set("Malangas")

        self.etiqueta_agregar = ctk.CTkLabel(self.app, text="Agregar Productos", font=("Arial", 18, "bold"))
        self.etiqueta_agregar.grid(row=3, column=1, pady=10, sticky="n")

        self.frame_agregar = ctk.CTkFrame(self.app, fg_color="transparent")
        self.frame_agregar.grid(row=4, column=1, pady=5)

        self.combo_sabores_agregar = ctk.CTkComboBox(self.frame_agregar, values=self.sabores_malanga, width=140, font=("Arial", 14))
        self.combo_sabores_agregar.grid(row=0, column=0, padx=5)

        self.entrada_cantidad_agregar = ctk.CTkEntry(self.frame_agregar, placeholder_text="Cantidad", width=100, font=("Arial", 14))
        self.entrada_cantidad_agregar.grid(row=0, column=1, padx=5)

        self.boton_agregar = ctk.CTkButton(self.frame_agregar, text="Agregar", width=100, font=("Arial", 14, "bold"))
        self.boton_agregar.grid(row=0, column=2, padx=5)

        self.etiqueta_mermar = ctk.CTkLabel(self.app, text="Mermar Productos", font=("Arial", 18, "bold"))
        self.etiqueta_mermar.grid(row=5, column=1, pady=10, sticky="n")

        self.frame_mermar = ctk.CTkFrame(self.app, fg_color="transparent")
        self.frame_mermar.grid(row=6, column=1, pady=5)

        self.combo_sabores_mermar = ctk.CTkComboBox(self.frame_mermar, values=self.sabores_malanga, width=140, font=("Arial", 14))
        self.combo_sabores_mermar.grid(row=0, column=0, padx=5)

        self.entrada_cantidad_mermar = ctk.CTkEntry(self.frame_mermar, placeholder_text="Cantidad", width=100, font=("Arial", 14))
        self.entrada_cantidad_mermar.grid(row=0, column=1, padx=5)

        self.boton_mermar = ctk.CTkButton(self.frame_mermar, text="Mermar", width=100, font=("Arial", 14, "bold"))
        self.boton_mermar.grid(row=0, column=2, padx=5)

    def actualizar_sabores(self, seleccion):
        if seleccion == "Malangas":
            self.combo_sabores_agregar.configure(values=self.sabores_malanga)
            self.combo_sabores_agregar.set(self.sabores_malanga[0])
            self.combo_sabores_mermar.configure(values=self.sabores_malanga)
            self.combo_sabores_mermar.set(self.sabores_malanga[0])
        elif seleccion == "Maicitos":
            self.combo_sabores_agregar.configure(values=self.sabores_maicito)
            self.combo_sabores_agregar.set(self.sabores_maicito[0])
            self.combo_sabores_mermar.configure(values=self.sabores_maicito)
            self.combo_sabores_mermar.set(self.sabores_maicito[0])

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    app_instance = AdministracionInventario(app)
    app.mainloop()
