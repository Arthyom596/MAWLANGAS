import customtkinter as ctk
from src.Controlador.FinanzaControlador import FinanzaControlador


class FinanzasVista:
    def __init__(self,parent,controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame=ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="white")


        self.frame.grid_columnconfigure(0, weight=0)
        self.frame.grid_columnconfigure(1, weight=0)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=0)
        self.frame.grid_columnconfigure(4, weight=0)

        for i in range(9):
            self.frame.grid_rowconfigure(i, weight=1)

        self.frame_superior = ctk.CTkFrame(self.frame, height=50, fg_color="#3a0488", bg_color="#3a0488")
        self.frame_superior.grid(row=0, column=0, sticky="new", columnspan=4)

        self.frame_superior.grid_columnconfigure(0, weight=1)
        self.frame_superior.grid_columnconfigure(1, weight=1)
        self.frame_superior.grid_columnconfigure(2, weight=1)
        self.frame_superior.grid_columnconfigure(3, weight=1)
        self.frame_superior.grid_columnconfigure(4, weight=1)

        self.etiqueta_titulo = ctk.CTkLabel(
            self.frame_superior, text="Finanzas", font=("Arial", 36, "bold",),text_color="white")
        self.etiqueta_titulo.grid(row=0, column=2, pady=(30, 20), sticky="n")

        self.btn_gasto = ctk.CTkLabel(self.frame, text="Agregar Gasto", font=("Arial", 20, "bold"))
        self.btn_gasto.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.entrada_gasto = ctk.CTkEntry(self.frame, placeholder_text="Cantidad", font=("Arial", 14),
                                          text_color="black")
        self.entrada_gasto.grid(row=1, column=2, padx=10, pady=10, sticky="ew")  # Se expande

        self.btn_agregar_gasto = ctk.CTkButton(self.frame, text="Agregar", font=("Arial", 14, "bold"),text_color="white",fg_color="#a75a03",hover_color="#f49a33")
        self.btn_agregar_gasto.grid(row=1, column=3, padx=20, pady=10, sticky="ew")

        self.etiqueta_concepto_gasto = ctk.CTkLabel(self.frame, text="CONCEPTO", font=("Arial", 14), text_color="black")
        self.etiqueta_concepto_gasto.grid(row=2, column=1, padx=20, pady=(5, 5), sticky="ew")

        self.entrada_concepto_gasto = ctk.CTkEntry(self.frame, placeholder_text="Escriba el concepto",text_color="black")
        self.entrada_concepto_gasto.grid(row=2, column=2, columnspan=2, padx=10, pady=(5, 10), sticky="ew")  # Se expande

        self.btn_ingreso = ctk.CTkLabel(self.frame, text="Agregar Ingreso", font=("Arial", 20, "bold"))
        self.btn_ingreso.grid(row=4, column=1, padx=20, pady=(40, 10), sticky="ew")

        self.entrada_ingreso = ctk.CTkEntry(self.frame, placeholder_text="Cantidad", font=("Arial", 14),
                                            text_color="black")
        self.entrada_ingreso.grid(row=4, column=2, padx=10, pady=(40, 10), sticky="ew")  # Se expande

        self.btn_agregar_ingreso = ctk.CTkButton(self.frame, text="Agregar", font=("Arial", 14, "bold"),text_color="white",fg_color="#009610",hover_color="#06e81e")
        self.btn_agregar_ingreso.grid(row=4, column=3, padx=20, pady=(40, 10), sticky="ew")

        self.etiqueta_concepto_ingreso = ctk.CTkLabel(self.frame, text="CONCEPTO", font=("Arial", 14),
                                                      text_color="black")
        self.etiqueta_concepto_ingreso.grid(row=5, column=1, padx=20, pady=(5, 5), sticky="ew")

        self.entrada_concepto_ingreso = ctk.CTkEntry(self.frame, placeholder_text="Escriba el concepto")
        self.entrada_concepto_ingreso.grid(row=5, column=2, columnspan=2, padx=10, pady=(5, 10), sticky="ew")  # Se expande

        self.etiqueta_dinamica = ctk.CTkLabel(self.frame, text="", font=("Arial", 14), text_color="white")
        self.etiqueta_dinamica.grid(row=6, column=2, padx=20, pady=10, sticky="ew")

        self.btn_regresar=ctk.CTkButton(self.frame, text="Cancelar", font=("Arial", 14, "bold"),fg_color="#be1010",
                                        text_color="white",hover_color="#fe0000", command=self.controlador_maestro.mostrar_menu_principal)
        self.btn_regresar.grid(row=7,column=2,padx=20,pady=10,sticky="ew")

        self.controlador = FinanzaControlador(self)


class ControladorMaestroFalso:
    def mostrar_menu_principal(self):
        print("Regresando al menu")

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("850x650")
    root.title("Productos")

    falso_maestro = ControladorMaestroFalso()
    FinanzasVista(root, controlador_maestro=falso_maestro)
    root.mainloop()