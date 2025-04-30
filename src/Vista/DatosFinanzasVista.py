import customtkinter as ctk


class DatosFinanzas:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Finanzas")

        ctk.set_appearance_mode("dark")

        # Configurar columnas y filas
        for i in range(3):
            self.root.columnconfigure(i, weight=1)

        for i in range(7):
            self.root.rowconfigure(i, weight=1)

        # Título principal
        self.etiqueta_finanzas = ctk.CTkLabel(self.root, text="Finanzas", font=("Helvetica", 36, "bold"),
                                              text_color="white")
        self.etiqueta_finanzas.grid(row=0, column=1, sticky="nsew")

        # Etiqueta para selección de producto
        self.etiqueta_seleccion = ctk.CTkLabel(self.root, text="Seleccione su producto", font=("Arial", 14, "bold"))
        self.etiqueta_seleccion.grid(row=1, column=1, pady=(10, 0), sticky="n")

        # ComboBox con opciones
        self.combo_productos = ctk.CTkComboBox(self.root, values=["Malangas", "Maicitos"])
        self.combo_productos.grid(row=2, column=1, pady=(0, 20), sticky="n")

        self.etiqueta_ganancia = ctk.CTkLabel(self.root, text="Ganancia Total")
        self.etiqueta_ganancia.grid(row=2, column=0, sticky="nsew")

        self.etiqueta_cantidad_total = ctk.CTkLabel(self.root, text="Cantidad: ")
        self.etiqueta_cantidad_total.grid(row=3, column=0, sticky="nsew")

        self.etiqueta_restante = ctk.CTkLabel(self.root, text="Inversion Restante")
        self.etiqueta_restante.grid(row=2, column=2, sticky="nsew")

        self.etiqueta_cantidad_restante = ctk.CTkLabel(self.root, text="Cantidad: ")
        self.etiqueta_cantidad_restante.grid(row=3, column=2, sticky="nsew")

        self.etiqueta_gasto = ctk.CTkLabel(self.root, text="Gasto Total")
        self.etiqueta_gasto.grid(row=4, column=0, sticky="nsew")

        self.dinero_total = ctk.CTkLabel(self.root, text="Dinero Total")
        self.dinero_total.grid(row=4, column=1, sticky="nsew")

        self.saldo_total = ctk.CTkLabel(self.root, text="Saldo Total")
        self.saldo_total.grid(row=5, column=1, sticky="nsew")

        self.etiqueta_cantidad_vendido = ctk.CTkLabel(self.root, text="Cantidad: ")
        self.etiqueta_cantidad_vendido.grid(row=5, column=0, sticky="nsew")

        self.etiqueta_merma = ctk.CTkLabel(self.root, text="Merma")
        self.etiqueta_merma.grid(row=4, column=2, sticky="nsew")

        self.etiqueta_cantidad_mermado = ctk.CTkLabel(self.root, text="Cantidad: ")
        self.etiqueta_cantidad_mermado.grid(row=5, column=2, sticky="nsew")


if __name__ == "__main__":
    root = ctk.CTk()
    app = DatosFinanzas(root)
    root.mainloop()
