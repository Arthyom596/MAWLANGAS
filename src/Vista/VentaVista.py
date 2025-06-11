import customtkinter as ctk
from customtkinter import CTkFrame
from src.Controlador.VentaControlador import ControladorVenta  # Ajusta la ruta si es diferente

class VentaVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="white")

        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(10):
            self.frame.grid_rowconfigure(i, weight=1)

        self.frame_superior = ctk.CTkFrame(self.frame, height=50, fg_color="#027a7a", bg_color="#027a7a")
        self.frame_superior.grid(row=0, column=0, sticky="new", columnspan=4)

        self.frame_derecho = ctk.CTkFrame(self.frame, width=80, fg_color="#027a7a", bg_color="#027a7a")
        self.frame_derecho.grid(row=0,column=11, sticky="ns",rowspan=12)

        self.frame_izquierda = ctk.CTkFrame(self.frame, width=80, fg_color="#027a7a", bg_color="#027a7a")
        self.frame_izquierda.grid(row=0, column=0, sticky="nws", rowspan=12)

        self.etiqueta_titulo = ctk.CTkLabel(self.frame_superior, text="Venta", font=("Arial", 36, "bold"), text_color="white")
        self.etiqueta_titulo.grid(row=0, column=2,padx=350,pady=20)

        self.etiqueta_seleccion = ctk.CTkLabel(self.frame, text="Seleccione su producto", font=("Arial", 16, "bold"))
        self.etiqueta_seleccion.grid(row=1, column=1, sticky="n")

        self.combo_productos = ctk.CTkComboBox(self.frame, values=[], width=200,
                                               command=self.controlador_actualizar_sabores)
        self.combo_productos.grid(row=2, column=1, pady=(0, 20), sticky="n")
        self.combo_productos.set("Producto")

        self.etiqueta_cantidad = ctk.CTkLabel(self.frame, text="Cantidad", font=("Arial", 16, "bold"))
        self.etiqueta_cantidad.grid(row=3, column=1, pady=(10, 5), sticky="n")

        self.entrada_cantidad = ctk.CTkEntry(self.frame, placeholder_text="Ingrese la cantidad", width=200)
        self.entrada_cantidad.grid(row=4, column=1, pady=(0, 20), sticky="n")

        self.switch_sabor = ctk.CTkSwitch(self.frame, text="¿Requiere sabor?", command=self.toggle_sabor,progress_color="#009610")
        self.switch_sabor.grid(row=5, column=1, pady=(0, 10), sticky="n")

        self.etiqueta_sabor = ctk.CTkLabel(self.frame, text="Seleccione el sabor", font=("Arial", 16, "bold"))
        self.etiqueta_sabor.grid(row=6, column=1, pady=(10, 5), sticky="n")

        self.combo_sabor = ctk.CTkComboBox(self.frame, values=[], width=200)
        self.combo_sabor.grid(row=7, column=1, pady=(0, 20), sticky="n")

        self.etiqueta_dinamica = ctk.CTkLabel(self.frame, text="", font=("Arial", 16, "bold"))
        self.etiqueta_dinamica.grid(row=8, column=1)

        self.boton_venta = ctk.CTkButton(self.frame, text="Vender", font=("Arial", 18, "bold"),
                                         fg_color="green", text_color="white", width=150)
        self.boton_venta.grid(row=9, column=1, pady=10, sticky="n")

        self.boton_cancelar = ctk.CTkButton(self.frame, text="Cancelar", font=("Arial", 16, "bold"),
                                            fg_color="#D32F2F", hover_color="#B71C1C", width=150,
                                            command=self.controlador_maestro.mostrar_menu_principal)
        self.boton_cancelar.grid(row=10, column=1, pady=10, sticky="n")

        self.frame_inferior = ctk.CTkFrame(self.frame, height=80, fg_color="#027a7a", bg_color="#027a7a")
        self.frame_inferior.grid(row=11, column=0, sticky="sew", columnspan=4)

        self.controlador = ControladorVenta(self)

    def controlador_actualizar_sabores(self, producto_seleccionado):
        # Este método sólo llama al método del controlador para mantener separación de capas
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
        print("Sabores cargados:", sabores)

        if sabores:
            self.switch_sabor.configure(state="normal")
            self.switch_sabor.select()
            self.toggle_sabor()
        else:
            self.switch_sabor.deselect()
            self.switch_sabor.configure(state="disabled")
            self.toggle_sabor()


class ControladorMaestroFalso:
    def mostrar_menu_principal(self):
        print("Regresando al menú principal")


if __name__ == "__main__":
    ctk.set_appearance_mode("light")  # corregido: era "ligth"
    root = ctk.CTk()
    root.geometry("850x650")
    root.title("Productos")

    falso_maestro = ControladorMaestroFalso()
    VentaVista(root, controlador_maestro=falso_maestro)

    root.mainloop()
