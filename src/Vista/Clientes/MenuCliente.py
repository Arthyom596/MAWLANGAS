import customtkinter as ctk
from pathlib import Path
from PIL import Image
class MenuCliente:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro

        # Frame principal dentro del parent
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        # Configuración de filas y columnas
        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.frame.grid_rowconfigure(i, weight=1)

        # Etiqueta del título
        self.etiqueta_titulo = ctk.CTkLabel(self.frame, text="Menú Clientes", font=("Arial", 28, "bold"))
        self.etiqueta_titulo.grid(row=0, column=1, pady=(40, 20), sticky="n")

        # Botón Productos
        self.agregar_cliente = ctk.CTkButton(self.frame, text="Agregar Cliente", width=200, height=50,
                                             font=("Arial", 16, "bold"))
        self.agregar_cliente.grid(row=1, column=0, pady=10)

        # Botón Sabores
        self.btn_consultar_cliente = ctk.CTkButton(self.frame, text="Consultar Clientes ", width=200, height=50,
                                                   font=("Arial", 16, "bold"))
        self.btn_consultar_cliente.grid(row=1, column=1, pady=10)

        # Botón Usuarios
        self.btn_mapa = ctk.CTkButton(self.frame, text="Mapa de Clientes", width=200, height=50,
                                      font=("Arial", 16, "bold"))
        self.btn_mapa.grid(row=1, column=2, pady=10)

        ruta_imagen = Path (__file__).resolve().parent.parent.parent.parent / "assets"
        ruta_cliente = ruta_imagen / "cliente.png"
        ruta_consulta =ruta_imagen / "consultar_cliente.png"
        ruta_mapa = ruta_imagen / "mapa.png"

        imagen_cliente = ctk.CTkImage(Image.open(ruta_cliente), size=(200, 200))
        imagen_consulta = ctk.CTkImage(Image.open(ruta_consulta), size=(200, 200))
        imagen_mapa = ctk.CTkImage(Image.open(ruta_mapa), size=(200, 200))

        self.label_cliente = ctk.CTkLabel(self.frame, image=imagen_cliente, text="")
        self.label_cliente.grid(row=2, column=0, pady=10)

        self.label_consulta = ctk.CTkLabel(self.frame, image=imagen_consulta, text="")
        self.label_consulta.grid(row=2, column=1, pady=10)

        self.label_mapa = ctk.CTkLabel(self.frame, image=imagen_mapa, text="")
        self.label_mapa.grid(row=2, column=2, pady=10)








        # Botón cancelar / regresar
        self.boton_cancelar = ctk.CTkButton(self.frame, text="Cancelar", font=("Arial", 14, "bold"),
                                            text_color="white", command=self.controlador_maestro.mostrar_menu_principal)
        self.boton_cancelar.grid(row=5, column=1, pady=20, sticky="ew")




