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

        # Botones con texto negro manualmente
        self.boton_inventario = ctk.CTkButton(
            self.frame_inferior, text="Inventario", text_color="black",
            font=("Arial", 25, "bold"),
            fg_color="blue", height=50, width=150,
            hover_color="#00008B",
            corner_radius=100,
            command=self.controlador_maestro.consultar_inventario
        )
        self.boton_inventario.grid(row=0, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.boton_finanzas = ctk.CTkButton(
            self.frame_inferior, text="Finanzas", text_color="black",
            font=("Arial", 25, "bold"),
            fg_color="limegreen", height=50, width=150,
            hover_color="#228B22",
            corner_radius=100,
            command=self.controlador_maestro.consultar_finanzas
        )
        self.boton_finanzas.grid(row=1, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.boton_productos = ctk.CTkButton(
            self.frame_inferior, text="Productos", text_color="black",
            font=("Arial", 25, "bold"),
            fg_color="yellow", height=50, width=150,
            hover_color="goldenrod",
            corner_radius=100,
            command=self.controlador_maestro.consultar_producto
        )
        self.boton_productos.grid(row=2, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.boton_usuarios = ctk.CTkButton(
            self.frame_inferior, text="Usuarios", text_color="black",
            font=("Arial", 25, "bold"),
            fg_color="purple", height=50, width=150,
            hover_color="#4B0082",
            corner_radius=100,
            command=self.controlador_maestro.consultar_usuarios
        )
        self.boton_usuarios.grid(row=3, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.boton_sabores = ctk.CTkButton(
            self.frame_inferior, text="Sabores", text_color="black",
            font=("Arial", 25, "bold"),
            fg_color="orange", height=50, width=150,
            hover_color="#FF8C00",
            corner_radius=100,
            command=self.controlador_maestro.consultar_sabores
        )
        self.boton_sabores.grid(row=4, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.boton_ventas = ctk.CTkButton(
            self.frame_inferior, text="Ventas", text_color="black",
            font=("Arial", 25, "bold"),
            fg_color="pink", height=50, width=150,
            hover_color="#C71585",
            corner_radius=100,
            command=self.controlador_maestro.consultar_ventas
        )
        self.boton_ventas.grid(row=5, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)

        self.boton_menu_principal = ctk.CTkButton(
            self.frame_inferior, text="Menu Principal", text_color="black",
            font=("Arial", 25, "bold"),
            fg_color="red", height=50, width=150,
            hover_color="#8B0000",
            corner_radius=100,
            command=self.controlador_maestro.mostrar_menu_principal
        )
        self.boton_menu_principal.grid(row=6, column=0, sticky="nsew", padx=20, pady=10, columnspan=4)
