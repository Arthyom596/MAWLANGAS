from pathlib import Path
import customtkinter as ctk
from PIL import Image

class MenuPrincipal:
    def __init__(self, parent, controlador_maestro=None):
        self.controlador_maestro = controlador_maestro
        self.frame = ctk.CTkFrame(parent, fg_color="#b5c9fe")
        self.frame.pack(fill="both", expand=True)

        self.frame_superior = ctk.CTkFrame(self.frame, fg_color="#0b104b",bg_color="#0b104b")
        self.frame_superior.grid(row=0, column=0, sticky="new",columnspan=3)

        ruta_imagen = Path(__file__).resolve().parent.parent.parent / "assets" / "Cat.png"
        imagen_gato_pequeno = ctk.CTkImage(Image.open(ruta_imagen), size=(120, 120))

        self.label_imagen1 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen1.grid(row=0, column=0, padx=35, pady=10, sticky="nsew")

        self.frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.titulo = ctk.CTkLabel(self.frame, text="Menú Principal", font=("Helvetica", 46, "bold"), text_color="white",bg_color="#0b104b")
        self.titulo.grid(row=0, column=1,columnspan=2, padx=10, pady=5, sticky="w")

        self.btn_inventario = ctk.CTkButton(self.frame, text="📦 Inventario", font=("Arial", 18, "bold"),
                                            height=60, width=250, corner_radius=50,
                                            fg_color="#2c40bf", hover_color="#001bff",command=self.controlador_maestro.mostrar_inventario)
        self.btn_inventario.grid(row=1, column=0, padx=20, pady=15)

        self.btn_finanzas = ctk.CTkButton(self.frame, text="💰 Finanzas", font=("Arial", 18, "bold"),
                                          height=60, width=250, corner_radius=50,text_color="#ffffff",
                                          fg_color="#2c40bf", hover_color="#001bff",command=self.controlador_maestro.mostrar_finanzas)
        self.btn_finanzas.grid(row=1, column=1, padx=20, pady=15)

        self.btn_ventas = ctk.CTkButton(self.frame, text="🛒 Iniciar Venta", font=("Arial", 18, "bold"),
                                        height=60, width=250, corner_radius=50,text_color="#ffffff",
                                        fg_color="#0aa507", hover_color="#1bee17",command=self.controlador_maestro.mostrar_ventas)
        self.btn_ventas.grid(row=1, column=2, padx=20, pady=15)

        self.btn_productos = ctk.CTkButton(self.frame, text="🧾 Productos", font=("Arial", 18, "bold"),
                                           height=60, width=250, corner_radius=50,text_color="#ffffff",
                                           fg_color="#2c40bf", hover_color="#001bff",command=self.controlador_maestro.mostrar_productos)
        self.btn_productos.grid(row=2, column=0, padx=20, pady=15)

        self.btn_modificar = ctk.CTkButton(self.frame, text="✏️ Modificar", font=("Arial", 18, "bold"),
                                           height=60, width=250, corner_radius=50,text_color="#ffffff",
                                           fg_color="#2c40bf", hover_color="#001bff",
                                           command=self.controlador_maestro.menu_modificar)
        self.btn_modificar.grid(row=2, column=1, padx=20, pady=15)

        self.btn_eliminar = ctk.CTkButton(self.frame, text="🗑️ Eliminar", font=("Arial", 18, "bold"),
                                          height=60, width=250, corner_radius=50,text_color="#ffffff",
                                          fg_color="#cb2525", hover_color="#ff0000",
                                          command=self.controlador_maestro.menu_eliminar)
        self.btn_eliminar.grid(row=2, column=2, padx=20, pady=15)

        self.btn_consultas = ctk.CTkButton(self.frame, text="🔍 Consultas", font=("Arial", 18, "bold"),
                                           height=60, width=250, corner_radius=50,text_color="#ffffff",
                                           fg_color="#2c40bf", hover_color="#001bff",
                                           command=self.controlador_maestro.mostrar_menu_consultas)
        self.btn_consultas.grid(row=3, column=1, padx=20, pady=15)

        self.frame_inferior = ctk.CTkFrame(self.frame, width=600, height=400,fg_color="#0b104b",bg_color="#0b104b")
        self.frame_inferior.grid(row=5, column=0,columnspan=3,sticky="nsew")

        self.frame_inferior.grid_columnconfigure(0, weight=1)
        self.frame_inferior.grid_columnconfigure(1, weight=1)
        self.frame_inferior.grid_columnconfigure(2, weight=1)

        self.etiqueta_bienvenido = ctk.CTkLabel(self.frame_inferior, text="Bienvenido {}",
                                                font=("Helvetica", 46,"bold"), text_color="white")
        self.etiqueta_bienvenido.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.etiqueta_bienvenido.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    def ocultar(self):
        self.frame.pack_forget()

    def actualizar_bienvenida(self, nombre):
        self.etiqueta_bienvenido.configure(text=f"Bienvenido {nombre}")


