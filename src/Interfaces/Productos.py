import customtkinter as ctk

class Productos:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x750")
        self.app.title("Añadir Producto")

        self.app.grid_columnconfigure((0, 1), weight=1)
        self.app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.titulo = ctk.CTkLabel(
            self.app, text="Registro de Producto",
            font=("Arial", 28, "bold"),
            text_color="white"
        )
        self.titulo.grid(row=0, column=0, columnspan=2, pady=(30, 10))

        self.frame_producto = ctk.CTkFrame(self.app, corner_radius=20)
        self.frame_producto.grid(row=1, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
        self.frame_producto.grid_columnconfigure(1, weight=1)

        self.label_nombre = ctk.CTkLabel(self.frame_producto, text="Nombre del producto:", font=("Arial", 16))
        self.label_nombre.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.entry_nombre = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. Malanga", font=("Arial", 14))
        self.entry_nombre.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")

        self.label_precio_compra = ctk.CTkLabel(self.frame_producto, text="Precio de compra ($):", font=("Arial", 16))
        self.label_precio_compra.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="w")

        self.entry_precio_compra = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 12", font=("Arial", 14))
        self.entry_precio_compra.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="ew")

        self.label_precio_venta = ctk.CTkLabel(self.frame_producto, text="Precio de venta ($):", font=("Arial", 16))
        self.label_precio_venta.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="w")

        self.entry_precio_venta = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 18", font=("Arial", 14))
        self.entry_precio_venta.grid(row=2, column=1, padx=20, pady=(10, 20), sticky="ew")

        self.titulo_sabores = ctk.CTkLabel(
            self.app, text="Sabores del Producto",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        self.titulo_sabores.grid(row=2, column=0, columnspan=2, pady=(10, 5))

        self.frame_sabores = ctk.CTkFrame(self.app, corner_radius=20)
        self.frame_sabores.grid(row=3, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
        self.frame_sabores.grid_columnconfigure(0, weight=1)

        self.entry_sabor = ctk.CTkEntry(self.frame_sabores, placeholder_text="Agregar sabor (ej. Adobado)", font=("Arial", 14))
        self.entry_sabor.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.btn_agregar_sabor = ctk.CTkButton(self.frame_sabores, text="Añadir Sabor", font=("Arial", 14, "bold"))
        self.btn_agregar_sabor.grid(row=0, column=1, padx=20, pady=20)

        self.lista_sabores = ctk.CTkTextbox(self.frame_sabores, height=100, font=("Arial", 14))
        self.lista_sabores.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
        self.lista_sabores.insert("0.0", "Sabores añadidos:\n")

        self.btn_guardar = ctk.CTkButton(
            self.app, text="Guardar Producto y Sabores",
            font=("Arial", 16, "bold"),
            fg_color="#4CAF50", hover_color="#45A049"
        )
        self.btn_guardar.grid(row=4, column=0, columnspan=2, pady=30, padx=100, sticky="ew")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    productos = Productos(app)
    app.mainloop()
