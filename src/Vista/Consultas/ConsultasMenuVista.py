from pathlib import Path
import customtkinter as ctk
from PIL import Image

class ConsultasMenuVista:
    def __init__(self, parent,controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)


        ruta_imagen = Path(__file__).resolve().parent.parent.parent.parent / "assets" / "Cat.png"
        imagen_gato_pequeno = ctk.CTkImage(Image.open(ruta_imagen), size=(120, 120))

        for col in (0, 1, 2, 3):
            self.frame.columnconfigure(col, weight=1)
        for row in (0, 1, 2, 3, 4, 5):
            self.frame.rowconfigure(row, weight=1)

        # FRAME SUPERIOR
        self.frame_superior = ctk.CTkFrame(self.frame, width=850, height=20, fg_color="midnightblue", border_width=5, border_color="white")
        self.frame_superior.grid(row=0, column=0, sticky="ew")
        self.frame_superior.grid_propagate(True)

        self.mawlangas = ctk.CTkLabel(self.frame_superior, text="CONSULTAS", text_color="white", font=("Forte Normal", 60, "bold"))
        self.mawlangas.grid(row=0, column=2, padx=60, pady=10)

        self.label_imagen1 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen1.grid(row=0, column=0, padx=35, pady=10, sticky="w")

        self.label_imagen2 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen2.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.bienvenido = ctk.CTkLabel(
            self.frame,
            text="¡Bienvenido a Consultas!\n Aqui podrás manejar todas las opciones del programa.",
            font=("Arial", 20, "bold")
        )
        self.bienvenido.grid(row=1, column=0, padx=20, sticky="n")

        # FRAME INFERIOR QUE CONTIENE LOS BOTONES
        self.frame_inferior = ctk.CTkFrame(self.frame, width=700, height=400, border_width=5, border_color="midnightblue", fg_color="white")
        self.frame_inferior.grid(row=3, column=0)
        self.frame_inferior.grid_propagate(False)

        for col in (0, 1, 2, 3):
            self.frame_inferior.columnconfigure(col, weight=1)
        for row in (0, 1, 2, 3, 4, 5):
            self.frame_inferior.rowconfigure(row, weight=1)

        self.botton_inventario = ctk.CTkButton(
            self.frame_inferior, text="Inventario", text_color="white", font=("Arial", 25, "bold"),
            fg_color="blue", height=50, width=150, hover_color="darkblue", corner_radius=100
        )
        self.botton_inventario.grid(row=0, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.botton_finanzas = ctk.CTkButton(
            self.frame_inferior, text="Finanzas", text_color="white", font=("Arial", 25, "bold"),
            fg_color="limegreen", height=50, width=150, hover_color="green", corner_radius=100,
            command= self.controlador_maestro.consultar_finanzas
        )
        self.botton_finanzas.grid(row=1, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.botton_productos = ctk.CTkButton(
            self.frame_inferior, text="Productos", text_color="white", font=("Arial", 25, "bold"),
            fg_color="yellow", height=50, width=150, hover_color="goldenrod", corner_radius=100
        )
        self.botton_productos.grid(row=2, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.botton_usuarios = ctk.CTkButton(
            self.frame_inferior, text="Usuarios", text_color="white", font=("Arial", 25, "bold"),
            fg_color="purple", height=50, width=150, hover_color="indigo", corner_radius=100
        )
        self.botton_usuarios.grid(row=3, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.botton_sabores = ctk.CTkButton(
            self.frame_inferior, text="Sabores", text_color="white", font=("Arial", 25, "bold"),
            fg_color="orange", height=50, width=150, hover_color="darkorange", corner_radius=100
        )
        self.botton_sabores.grid(row=4, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.botton_menu = ctk.CTkButton(
            self.frame_inferior, text="Menu Principal", text_color="white", font=("Arial", 25, "bold"),
            fg_color="red", height=50, width=150, hover_color="darkred", corner_radius=100,
            command=self.controlador_maestro.mostrar_menu_principal
        )
        self.botton_menu.grid(row=5, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)



