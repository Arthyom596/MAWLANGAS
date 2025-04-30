import customtkinter as ctk


class FinanzasApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Finanzas")

        ctk.set_appearance_mode("dark")

        # Configurar columnas y filas
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)

        for i in range(9):
            self.root.grid_rowconfigure(i, weight=1)

        # Título principal
        self.etiqueta_titulo = ctk.CTkLabel(
            self.root, text="Finanzas", font=("Arial", 36, "bold")
        )
        self.etiqueta_titulo.grid(row=0, column=1, columnspan=3, pady=(30, 20), sticky="n")

        # Sección Gasto
        self.btn_gasto = ctk.CTkButton(self.root, text="Agregar Gasto", font=("Arial", 16, "bold"))
        self.btn_gasto.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.entrada_gasto = ctk.CTkEntry(self.root, placeholder_text="Cantidad", font=("Arial", 14),
                                          text_color="white")
        self.entrada_gasto.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.btn_agregar_gasto = ctk.CTkButton(self.root, text="Agregar", font=("Arial", 14, "bold"))
        self.btn_agregar_gasto.grid(row=1, column=3, padx=20, pady=10, sticky="ew")

        self.etiqueta_concepto_gasto = ctk.CTkLabel(self.root, text="CONCEPTO", font=("Arial", 14), text_color="white")
        self.etiqueta_concepto_gasto.grid(row=2, column=1, padx=20, pady=(5, 5), sticky="ew")

        self.entrada_concepto_gasto = ctk.CTkEntry(self.root, placeholder_text="Escriba el concepto")
        self.entrada_concepto_gasto.grid(row=2, column=2, columnspan=2, padx=10, pady=(5, 10), sticky="ew")

        # Sección Ingreso
        self.btn_ingreso = ctk.CTkButton(self.root, text="Agregar Ingreso", font=("Arial", 16, "bold"))
        self.btn_ingreso.grid(row=4, column=1, padx=20, pady=(40, 10), sticky="ew")

        self.entrada_ingreso = ctk.CTkEntry(self.root, placeholder_text="Cantidad", font=("Arial", 14),
                                            text_color="white")
        self.entrada_ingreso.grid(row=4, column=2, padx=10, pady=(40, 10), sticky="ew")

        self.btn_agregar_ingreso = ctk.CTkButton(self.root, text="Agregar", font=("Arial", 14, "bold"))
        self.btn_agregar_ingreso.grid(row=4, column=3, padx=20, pady=(40, 10), sticky="ew")

        self.etiqueta_concepto_ingreso = ctk.CTkLabel(self.root, text="CONCEPTO", font=("Arial", 14),
                                                      text_color="white")
        self.etiqueta_concepto_ingreso.grid(row=5, column=1, padx=20, pady=(5, 5), sticky="ew")

        self.entrada_concepto_ingreso = ctk.CTkEntry(self.root, placeholder_text="Escriba el concepto")
        self.entrada_concepto_ingreso.grid(row=5, column=2, columnspan=2, padx=10, pady=(5, 10), sticky="ew")


if __name__ == "__main__":
    root = ctk.CTk()
    app = FinanzasApp(root)
    root.mainloop()
