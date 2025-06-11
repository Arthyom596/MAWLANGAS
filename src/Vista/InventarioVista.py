import customtkinter as ctk
from src.Controlador.InventarioControlador import InventarioControlador

class InventarioVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro

        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="white")

        self.productos_dict = {}
        self.sabores_dict = {}

        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(10):
            self.frame.grid_rowconfigure(i, weight=1)

        self.etiqueta_titulo = ctk.CTkLabel(self.frame, text="Administración del Inventario", font=("Arial", 32, "bold"))
        self.etiqueta_titulo.grid(row=1, column=1, pady=10, sticky="n")

        self.frame_superior = ctk.CTkFrame(self.frame, height=50, fg_color="#1c67f3",bg_color="#1c67f3")
        self.frame_superior.grid(row=0, column=0,sticky="new",columnspan=4)

        self.etiqueta_producto = ctk.CTkLabel(self.frame, text="Seleccione producto:", font=("Arial", 16))
        self.etiqueta_producto.grid(row=2, column=1, sticky="s", pady=5)

        self.combo_producto = ctk.CTkComboBox(self.frame, values=[], width=290, font=("Arial", 14),height=50)
        self.combo_producto.grid(row=3, column=1, pady=5)
        self.combo_producto.set("Producto")

        self.switch_usar_sabor = ctk.CTkSwitch(self.frame, text="¿Usa sabor?", font=("Arial", 14), command=self.toggle_sabor,fg_color="#7a7877",progress_color="#0e8e27")
        self.switch_usar_sabor.grid(row=3, column=1, pady=10)
        self.switch_usar_sabor.select()

        self.etiqueta_agregar = ctk.CTkLabel(self.frame, text="Agregar Productos", font=("Arial", 18, "bold"))
        self.etiqueta_agregar.grid(row=4, column=1, pady=5)

        self.frame_agregar = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.frame_agregar.grid(row=5, column=1, pady=5)

        self.combo_sabores_agregar = ctk.CTkComboBox(self.frame_agregar, values=[], width=140, font=("Arial", 14))
        self.combo_sabores_agregar.grid(row=0, column=0, padx=5)
        self.combo_sabores_agregar.set("Sabor")

        self.entrada_cantidad_agregar = ctk.CTkEntry(self.frame_agregar, placeholder_text="Cantidad", width=100, font=("Arial", 14))
        self.entrada_cantidad_agregar.grid(row=0, column=1, padx=5)

        self.boton_agregar = ctk.CTkButton(self.frame_agregar, text="Agregar",text_color="white", width=100, font=("Arial", 14, "bold"),fg_color="#0a4aa5",hover_color="#0a6cf8")
        self.boton_agregar.grid(row=0, column=2, padx=5)

        self.etiqueta_mermar = ctk.CTkLabel(self.frame, text="Mermar Productos", font=("Arial", 18, "bold"))
        self.etiqueta_mermar.grid(row=6, column=1, pady=5)

        self.frame_mermar = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.frame_mermar.grid(row=7, column=1, pady=5)

        self.combo_sabores_mermar = ctk.CTkComboBox(self.frame_mermar, values=[], width=140, font=("Arial", 14))
        self.combo_sabores_mermar.grid(row=0, column=0, padx=5)
        self.combo_sabores_mermar.set("Sabor")

        self.entrada_cantidad_mermar = ctk.CTkEntry(self.frame_mermar, placeholder_text="Cantidad", width=100, font=("Arial", 14))
        self.entrada_cantidad_mermar.grid(row=0, column=1, padx=5)

        self.boton_mermar = ctk.CTkButton(self.frame_mermar, text="Mermar",text_color="white", width=100, font=("Arial", 14, "bold"),fg_color="#bd5d09",hover_color="#fc7701")
        self.boton_mermar.grid(row=0, column=2, padx=5)

        self.etiqueta_mensaje = ctk.CTkLabel(self.frame, text="", font=("Arial", 14))
        self.etiqueta_mensaje.grid(row=9, column=1, pady=10, sticky="n")
        self.btn_regresar = ctk.CTkButton(self.frame, text="Cancelar", font=("Arial", 14, "bold"),fg_color="#b20a0a",
                                          text_color="white",hover_color="#ff0000", command=self.controlador_maestro.mostrar_menu_principal)
        self.btn_regresar.grid(row=10, column=1, padx=20, pady=10, sticky="ew")

        self.frame_inferior = ctk.CTkFrame(self.frame, height=50, fg_color="#1c67f3",bg_color="#1c67f3")
        self.frame_inferior.grid(row=11, column=0, sticky="new", columnspan=4)

        self.controlador = InventarioControlador(self)

    def habilitar_sabores(self, estado: bool):
        if estado:
            self.combo_sabores_agregar.grid()
            self.combo_sabores_mermar.grid()
        else:
            self.combo_sabores_agregar.grid_remove()
            self.combo_sabores_mermar.grid_remove()

    def toggle_sabor(self):
        estado = self.switch_usar_sabor.get()
        self.habilitar_sabores(estado)

    def set_productos(self, productos: list):
        self.productos_dict = {nombre: id_ for id_, nombre in productos}
        self.combo_producto.configure(values=list(self.productos_dict.keys()))
        self.combo_producto.set("Producto")

    def set_sabores(self, sabores: list):
        self.sabores_dict = {nombre: id_ for id_, nombre in sabores}
        nombres = list(self.sabores_dict.keys())
        self.combo_sabores_agregar.configure(values=nombres)
        self.combo_sabores_agregar.set("Sabor")
        self.combo_sabores_mermar.configure(values=nombres)
        self.combo_sabores_mermar.set("Sabor")

    def mostrar_mensaje(self, texto: str, color="lightgreen"):
        self.etiqueta_mensaje.configure(text=texto, text_color=color)

    def resetear_campos(self):
        self.combo_producto.set("Producto")
        self.combo_sabores_agregar.set("Sabor")
        self.combo_sabores_mermar.set("Sabor")
        self.entrada_cantidad_agregar.delete(0, "end")
        self.entrada_cantidad_mermar.delete(0, "end")
        self.switch_usar_sabor.select()
        self.habilitar_sabores(True)

    def set_controlador(self, controlador):
        self.controlador = controlador
        self.combo_producto.configure(command=self.controlador.actualizar_sabores)
        self.boton_agregar.configure(command=self.controlador.agregar_producto)
        self.boton_mermar.configure(command=self.controlador.mermar_producto)

class ControladorMaestroFalso:
    def mostrar_menu_principal(self):
        print("Regresando al menu")

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("850x650")
    root.title("Productos")

    falso_maestro = ControladorMaestroFalso()
    InventarioVista(root, controlador_maestro=falso_maestro)

    root.mainloop()