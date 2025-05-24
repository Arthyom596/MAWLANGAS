import customtkinter as ctk

class ModificarVista:
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
        self.etiqueta_titulo = ctk.CTkLabel(self.frame, text="Menú Modificar", font=("Arial", 28, "bold"))
        self.etiqueta_titulo.grid(row=0, column=1, pady=(40, 20), sticky="n")

        # Botón Productos
        self.boton_productos = ctk.CTkButton(self.frame, text="Productos", width=200, height=50,
                                             font=("Arial", 16, "bold"),command=self.controlador_maestro.modificar_productos)
        self.boton_productos.grid(row=1, column=1, pady=10)

        # Botón Sabores
        self.boton_sabores = ctk.CTkButton(self.frame, text="Sabores", width=200, height=50, font=("Arial", 16, "bold"))
        self.boton_sabores.grid(row=2, column=1, pady=10)

        # Botón Usuarios
        self.boton_usuarios = ctk.CTkButton(self.frame, text="Usuarios", width=200, height=50,
                                            font=("Arial", 16, "bold"),
                                            command=self.controlador_maestro.modificar_usuarios)
        self.boton_usuarios.grid(row=3, column=1, pady=10)

        # Botón cancelar / regresar
        self.boton_cancelar = ctk.CTkButton(self.frame, text="Cancelar", font=("Arial", 14, "bold"),
                                            text_color="white", command=self.controlador_maestro.mostrar_menu_principal)
        self.boton_cancelar.grid(row=5, column=1, pady=20, sticky="ew")

    def set_controlador(self, controlador):
        self.boton_productos.configure(command=controlador.modificar_producto)
        self.boton_sabores.configure(command=controlador.modificar_sabor)
        self.boton_usuarios.configure(command=controlador.modificar_usuario)





# Clase de prueba para simular el controlador maestro
class ControladorMaestroFalso:
    def mostrar_menu_principal(self):
        print("Volver al menú principal")



class ControladorModificarFalso:
    def modificar_producto(self):
        print("Producto modificado")

    def modificar_sabor(self):
        print("Sabor modificado")

    def modificar_usuario(self):
        print("Usuario modificado")


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("850x650")
    root.title("Modificar")

    controlador_maestro = ControladorMaestroFalso()
    vista = ModificarVista(root, controlador_maestro=controlador_maestro)

    controlador_modificar = ControladorModificarFalso()
    vista.set_controlador(controlador_modificar)

    root.mainloop()
