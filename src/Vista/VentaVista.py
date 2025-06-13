import customtkinter as ctk
from customtkinter import CTkFrame
from src.Controlador.VentaControlador import ControladorVenta

class VentaVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = CTkFrame(parent, fg_color="white")
        self.frame.pack(fill="both", expand=True)



        # Configurar grilla con una columna centrada
        self.frame.grid_columnconfigure(0, weight=1)
        for i in range(9):
            self.frame.grid_rowconfigure(i, weight=1)

        self._crear_contenido()
        self.controlador = ControladorVenta(self)

    def _crear_contenido(self):
        col = 0

        ctk.CTkLabel(self.frame, text="Venta", font=("Arial", 36, "bold"), text_color="#027a7a")\
            .grid(row=0, column=col)

        ctk.CTkLabel(self.frame, text="Seleccione su producto", font=("Arial", 16, "bold"))\
            .grid(row=1, column=col)

        self.combo_productos = ctk.CTkComboBox(self.frame, values=[], width=220,
                                               command=self.controlador_actualizar_sabores)
        self.combo_productos.grid(row=2, column=col)
        self.combo_productos.set("Producto")

        ctk.CTkLabel(self.frame, text="Cantidad", font=("Arial", 16, "bold"))\
            .grid(row=3, column=col)

        self.entrada_cantidad = ctk.CTkEntry(self.frame, placeholder_text="Ingrese la cantidad", width=220)
        self.entrada_cantidad.grid(row=4, column=col)

        self.switch_sabor = ctk.CTkSwitch(self.frame, text="¿Requiere sabor?",
                                          command=self.toggle_sabor, progress_color="#009610")
        self.switch_sabor.grid(row=5, column=col)

        self.etiqueta_sabor = ctk.CTkLabel(self.frame, text="Seleccione el sabor", font=("Arial", 16, "bold"))
        self.etiqueta_sabor.grid(row=6, column=col)

        self.combo_sabor = ctk.CTkComboBox(self.frame, values=[], width=220)
        self.combo_sabor.grid(row=7, column=col)

        self.etiqueta_dinamica = ctk.CTkLabel(self.frame, text="", font=("Arial", 16, "bold"))
        self.etiqueta_dinamica.grid(row=8, column=col)

        botones_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        botones_frame.grid(row=9, column=col, pady=10)
        self.boton_venta = ctk.CTkButton(botones_frame, text="Vender", font=("Arial", 18, "bold"),
                                         fg_color="green", text_color="white", width=150)
        self.boton_venta.pack(side="left", padx=10)

        self.boton_cancelar = ctk.CTkButton(botones_frame, text="Cancelar", font=("Arial", 16, "bold"),
                                            fg_color="#D32F2F", hover_color="#B71C1C", width=150,
                                            command=self.controlador_maestro.mostrar_menu_principal)
        self.boton_cancelar.pack(side="right", padx=10)

    def controlador_actualizar_sabores(self, producto_seleccionado):
        self.controlador.actualizar_sabores(producto_seleccionado)

    def obtener_frame(self):
        return self.frame

    def toggle_sabor(self):
        if self.switch_sabor.get() == 1:
            self.etiqueta_sabor.grid()
            self.combo_sabor.grid()
        else:
            self.etiqueta_sabor.grid_remove()
            self.combo_sabor.grid_remove()

    def cargar_productos(self, productos):
        self.combo_productos.configure(values=productos)

    def cargar_sabores(self, sabores):
        self.combo_sabor.configure(values=sabores)
        if sabores:
            self.switch_sabor.configure(state="normal")
            self.switch_sabor.select()
            self.toggle_sabor()
        else:
            self.switch_sabor.deselect()
            self.switch_sabor.configure(state="disabled")
            self.toggle_sabor()
