import customtkinter as ctk

class MenuPrincipal:
    def __init__(self, parent, controlador_maestro=None):
        self.controlador_maestro = controlador_maestro
        self.frame = ctk.CTkFrame(parent, fg_color="#87CEEB")
        self.frame.pack(fill="both", expand=True)

        self.frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.titulo = ctk.CTkLabel(self.frame, text="Menú Principal", font=("Helvetica", 36, "bold"), text_color="white")
        self.titulo.grid(row=0, column=0, columnspan=3, pady=(30, 20))

        self.btn_inventario = ctk.CTkButton(self.frame, text="📦 Inventario", font=("Arial", 18, "bold"),
                                            height=60, width=250, corner_radius=20,
                                            fg_color="#3B8ED0", hover_color="#2F6BA8",command=self.controlador_maestro.mostrar_inventario)
        self.btn_inventario.grid(row=1, column=0, padx=20, pady=15)

        self.btn_finanzas = ctk.CTkButton(self.frame, text="💰 Finanzas", font=("Arial", 18, "bold"),
                                          height=60, width=250, corner_radius=20,
                                          fg_color="#3B8ED0", hover_color="#2F6BA8",command=self.controlador_maestro.mostrar_finanzas)
        self.btn_finanzas.grid(row=1, column=1, padx=20, pady=15)

        self.btn_ventas = ctk.CTkButton(self.frame, text="🛒 Iniciar Venta", font=("Arial", 18, "bold"),
                                        height=60, width=250, corner_radius=20,
                                        fg_color="#4CAF50", hover_color="#3E8E41",command=self.controlador_maestro.mostrar_ventas)
        self.btn_ventas.grid(row=1, column=2, padx=20, pady=15)

        self.btn_productos = ctk.CTkButton(self.frame, text="🧾 Productos", font=("Arial", 18, "bold"),
                                           height=60, width=250, corner_radius=20,
                                           fg_color="#3B8ED0", hover_color="#2F6BA8",command=self.controlador_maestro.mostrar_productos)
        self.btn_productos.grid(row=2, column=0, padx=20, pady=15)

        self.btn_modificar = ctk.CTkButton(self.frame, text="✏️ Modificar", font=("Arial", 18, "bold"),
                                           height=60, width=250, corner_radius=20,
                                           fg_color="#3B8ED0", hover_color="#2F6BA8",
                                           command=self.controlador_maestro.menu_modificar)
        self.btn_modificar.grid(row=2, column=1, padx=20, pady=15)

        self.btn_eliminar = ctk.CTkButton(self.frame, text="🗑️ Eliminar Elementos", font=("Arial", 18, "bold"),
                                          height=60, width=250, corner_radius=20,
                                          fg_color="#FF4C4C", hover_color="#CC3C3C",
                                          command=self.controlador_maestro.menu_eliminar)
        self.btn_eliminar.grid(row=2, column=2, padx=20, pady=15)

        self.btn_consultas = ctk.CTkButton(self.frame, text="🔍 Consultas", font=("Arial", 18, "bold"),
                                           height=60, width=250, corner_radius=20,
                                           fg_color="#3B8ED0", hover_color="#2F6BA8",
                                           command=self.controlador_maestro.mostrar_menu_consultas)
        self.btn_consultas.grid(row=3, column=1, padx=20, pady=15)

        self.etiqueta_version = ctk.CTkLabel(self.frame, text="Versión 10.0 • Desarrollado por Los Hombres del Progreso",
                                             font=("Arial", 12), text_color="gray")
        self.etiqueta_version.grid(row=5, column=0, columnspan=3, pady=20)

    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    def ocultar(self):
        self.frame.pack_forget()

