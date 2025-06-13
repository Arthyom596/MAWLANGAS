from pathlib import Path
import customtkinter as ctk
from PIL import Image

class ConsultasMenuVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        ruta_imagen = Path(__file__).resolve().parent.parent.parent.parent / "assets" / "Cat.png"
        imagen_gato_pequeno = ctk.CTkImage(Image.open(ruta_imagen), size=(120, 120))

        # Configurar grid general del frame principal
        for col in range(4):
            self.frame.columnconfigure(col, weight=1)
        for row in range(7):
            self.frame.rowconfigure(row, weight=1)

        # FRAME SUPERIOR (header)
        self.frame_superior = ctk.CTkFrame(self.frame, height=150, fg_color="midnightblue", border_width=5, border_color="white")
        self.frame_superior.grid(row=0, column=0, columnspan=4, sticky="ew", padx=10, pady=10)
        self.frame_superior.grid_propagate(False)

        # Configurar columnas del frame superior para centrar el título entre las imágenes
        for col in range(4):
            self.frame_superior.columnconfigure(col, weight=1)

        self.label_imagen1 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen1.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.mawlangas = ctk.CTkLabel(self.frame_superior, text="CONSULTAS", text_color="white", font=("Forte Normal", 60, "bold"))
        self.mawlangas.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="ew")

        self.label_imagen2 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen2.grid(row=0, column=3, padx=20, pady=10, sticky="e")

        # Texto de bienvenida centrado horizontalmente
        self.bienvenido = ctk.CTkLabel(
            self.frame,
            text="¡Bienvenido a Consultas!\nAqui podrás manejar todas las opciones del programa.",
            font=("Arial", 20, "bold"),
            justify="center"
        )
        self.bienvenido.grid(row=1, column=0, columnspan=4, pady=10, sticky="ew")

        # CONTENEDOR PARA EL FRAME INFERIOR para centrarlo
        self.frame_contenedor = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.frame_contenedor.grid(row=3, column=0, columnspan=4, sticky="nsew", pady=20)
        self.frame_contenedor.columnconfigure(0, weight=1)
        self.frame_contenedor.rowconfigure(0, weight=1)

        # FRAME INFERIOR (botones) centrado dentro del contenedor
        self.frame_inferior = ctk.CTkFrame(self.frame_contenedor, width=700, height=450, border_width=5, border_color="midnightblue", fg_color="white")
        self.frame_inferior.grid(row=0, column=0, sticky="n")
        self.frame_inferior.grid_propagate(False)

        for col in range(4):
            self.frame_inferior.columnconfigure(col, weight=1)
        for row in range(7):
            self.frame_inferior.rowconfigure(row, weight=1)

        botones_info = [
            ("Inventario", "blue", self.controlador_maestro.consultar_inventario),
            ("Finanzas", "limegreen", self.controlador_maestro.consultar_finanzas),
            ("Productos", "yellow", self.controlador_maestro.consultar_producto),
            ("Usuarios", "purple", self.controlador_maestro.consultar_usuarios),
            ("Sabores", "orange", self.controlador_maestro.consultar_sabores),
            ("Ventas", "pink", self.controlador_maestro.consultar_ventas),
            ("Menu Principal", "red", self.controlador_maestro.mostrar_menu_principal)
        ]

        hover_colors = {
            "blue": "#00008B",       # dark blue
            "limegreen": "#228B22",  # forest green
            "yellow": "goldenrod",   # goldenrod para amarillo
            "purple": "#4B0082",     # índigo
            "orange": "#FF8C00",     # dark orange
            "pink": "#C71585",       # medium violet red
            "red": "#8B0000"         # dark red
        }

        for i, (texto, color, cmd) in enumerate(botones_info):
            boton = ctk.CTkButton(
                self.frame_inferior, text=texto, text_color="white",
                font=("Arial", 25, "bold"),
                fg_color=color, height=50, width=150,
                hover_color=hover_colors.get(color, color),
                corner_radius=100,
                command=cmd
            )
            boton.grid(row=i, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)
