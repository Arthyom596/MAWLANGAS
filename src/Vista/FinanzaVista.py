import customtkinter as ctk
from src.Controlador.FinanzaControlador import FinanzaControlador


class FinanzasVista:
    def __init__(self,parent,controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.root=ctk.CTkFrame(parent)
        self.root.pack(fill="both", expand=True)


        ctk.set_appearance_mode("dark")

        # Configuración de columnas y filas
        # Asignamos peso a las columnas que contienen los Entry, para que se expandan con la ventana
        self.root.grid_columnconfigure(0, weight=0)  # Columna para el borde izquierdo
        self.root.grid_columnconfigure(1, weight=0)  # Columna para el botón y etiqueta
        self.root.grid_columnconfigure(2, weight=1)  # Columna para el Entry, que se expandirá
        self.root.grid_columnconfigure(3, weight=0)  # Columna para el botón de agregar
        self.root.grid_columnconfigure(4, weight=0)  # Columna para el borde derecho

        # Configuración de filas
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
        self.entrada_gasto.grid(row=1, column=2, padx=10, pady=10, sticky="ew")  # Se expande

        self.btn_agregar_gasto = ctk.CTkButton(self.root, text="Agregar", font=("Arial", 14, "bold"))
        self.btn_agregar_gasto.grid(row=1, column=3, padx=20, pady=10, sticky="ew")

        self.etiqueta_concepto_gasto = ctk.CTkLabel(self.root, text="CONCEPTO", font=("Arial", 14), text_color="white")
        self.etiqueta_concepto_gasto.grid(row=2, column=1, padx=20, pady=(5, 5), sticky="ew")

        self.entrada_concepto_gasto = ctk.CTkEntry(self.root, placeholder_text="Escriba el concepto")
        self.entrada_concepto_gasto.grid(row=2, column=2, columnspan=2, padx=10, pady=(5, 10), sticky="ew")  # Se expande

        # Sección Ingreso
        self.btn_ingreso = ctk.CTkButton(self.root, text="Agregar Ingreso", font=("Arial", 16, "bold"))
        self.btn_ingreso.grid(row=4, column=1, padx=20, pady=(40, 10), sticky="ew")

        self.entrada_ingreso = ctk.CTkEntry(self.root, placeholder_text="Cantidad", font=("Arial", 14),
                                            text_color="white")
        self.entrada_ingreso.grid(row=4, column=2, padx=10, pady=(40, 10), sticky="ew")  # Se expande

        self.btn_agregar_ingreso = ctk.CTkButton(self.root, text="Agregar", font=("Arial", 14, "bold"))
        self.btn_agregar_ingreso.grid(row=4, column=3, padx=20, pady=(40, 10), sticky="ew")

        self.etiqueta_concepto_ingreso = ctk.CTkLabel(self.root, text="CONCEPTO", font=("Arial", 14),
                                                      text_color="white")
        self.etiqueta_concepto_ingreso.grid(row=5, column=1, padx=20, pady=(5, 5), sticky="ew")

        self.entrada_concepto_ingreso = ctk.CTkEntry(self.root, placeholder_text="Escriba el concepto")
        self.entrada_concepto_ingreso.grid(row=5, column=2, columnspan=2, padx=10, pady=(5, 10), sticky="ew")  # Se expande

        self.etiqueta_dinamica = ctk.CTkLabel(self.root, text="", font=("Arial", 14), text_color="white")
        self.etiqueta_dinamica.grid(row=6, column=2, padx=20, pady=10, sticky="ew")

        self.controlador = FinanzaControlador(self)


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.geometry("700x600")
    root.title("Finanza Vista")
    FinanzasVista(root, controlador_maestro=None)
    root.mainloop()
