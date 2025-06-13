import customtkinter as ctk

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
        self.boton_productos = ctk.CTkButton(self.frame, text="Agregar Cliente", width=200, height=50,
                                             font=("Arial", 16, "bold"),command=self.controlador_maestro.eliminar_productos)
        self.boton_productos.grid(row=1, column=0, pady=10)

        # Botón Sabores
        self.btn_consultar_cliente = ctk.CTkButton(self.frame, text="Consultar Clientes ", width=200, height=50,
                                                   font=("Arial", 16, "bold"), command=self.controlador_maestro.eliminar_sabores)
        self.btn_consultar_cliente.grid(row=1, column=1, pady=10)

        # Botón Usuarios
        self.btn_mapa = ctk.CTkButton(self.frame, text="Mapa de Clientes", width=200, height=50,
                                      font=("Arial", 16, "bold"), command=self.controlador_maestro.eliminar_usuarios)
        self.btn_mapa.grid(row=1, column=2, pady=10)

        # Botón cancelar / regresar
        self.boton_cancelar = ctk.CTkButton(self.frame, text="Cancelar", font=("Arial", 14, "bold"),
                                            text_color="white", command=self.controlador_maestro.mostrar_menu_principal)
        self.boton_cancelar.grid(row=5, column=1, pady=20, sticky="ew")

    #def set_controlador(self, controlador):
       # self.boton_productos.configure(command=controlador.eliminar_producto)
        #self.btn_consultar_cliente.configure(command=controlador.eliminar_sabor)
       # self.btn_mapa.configure(command=controlador.eliminar_usuario)


