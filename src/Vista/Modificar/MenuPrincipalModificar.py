import customtkinter as ctk
from PIL import Image
from pathlib import Path

class ModificarVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro



        # Frame exterior naranja
        self.frame = ctk.CTkFrame(parent, fg_color="#a8ad14")
        self.frame.pack(fill="both", expand=True)


        # Frame interior blanco que contendrá toda la interfaz
        self.frame_interior = ctk.CTkFrame(self.frame, fg_color="white", corner_radius=15)
        self.frame_interior.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.9, relheight=0.9)

        # Configuración de grilla interior (2 columnas, 5 filas)
        for i in range(2):
            self.frame_interior.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.frame_interior.grid_rowconfigure(i, weight=1)

        # Título centrado
        self.etiqueta_titulo = ctk.CTkLabel(self.frame_interior, text="Menú Modificar",
                                            font=("Arial", 28, "bold"))
        self.etiqueta_titulo.grid(row=0, column=0, sticky="nsew", padx=10, pady=(20, 10))

        # Imagen centrada debajo del título
        ruta_imagen = Path(__file__).resolve().parent.parent.parent.parent / "assets" / "modificar.png"
        imagen_modificar = ctk.CTkImage(Image.open(ruta_imagen), size=(280, 280))
        self.label_modificar = ctk.CTkLabel(self.frame_interior, image=imagen_modificar, text="")
        self.label_modificar.grid(row=1, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)

        # Botones en columna derecha
        self.boton_productos = ctk.CTkButton(self.frame_interior, text="Productos", width=200, height=50,
                                             fg_color="#054ac2", hover_color="#186afa",
                                             font=("Arial", 16, "bold"), corner_radius=50,
                                             command=self.controlador_maestro.modificar_productos)
        self.boton_productos.grid(row=1, column=1, pady=5, sticky="n")

        self.boton_sabores = ctk.CTkButton(self.frame_interior, text="Sabores", width=200, height=50,
                                           fg_color="#054ac2", hover_color="#186afa",
                                           font=("Arial", 16, "bold"), corner_radius=50,
                                           command=self.controlador_maestro.modificar_sabores)
        self.boton_sabores.grid(row=2, column=1, pady=5, sticky="n")

        self.boton_usuarios = ctk.CTkButton(self.frame_interior, text="Usuarios", width=200, height=50,
                                            fg_color="#054ac2", hover_color="#186afa",
                                            font=("Arial", 16, "bold"), corner_radius=50,
                                            command=self.controlador_maestro.modificar_usuarios)
        self.boton_usuarios.grid(row=3, column=1, pady=5, sticky="n")

        self.boton_cancelar = ctk.CTkButton(self.frame_interior, text="Cancelar", font=("Arial", 14, "bold"),
                                            width=210, height=40, fg_color="#b81717", hover_color="#e70c0c",
                                            text_color="white", corner_radius=50,
                                            command=self.controlador_maestro.mostrar_menu_principal)
        self.boton_cancelar.grid(row=4, column=1, pady=10, sticky="n")

    def set_controlador(self, controlador):
        self.boton_productos.configure(command=controlador.modificar_producto)
        self.boton_sabores.configure(command=controlador.modificar_sabor)
        self.boton_usuarios.configure(command=controlador.modificar_usuario)
