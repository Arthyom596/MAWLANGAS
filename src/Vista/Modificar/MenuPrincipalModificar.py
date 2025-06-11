import customtkinter as ctk
from PIL import Image
from pathlib import Path

class ModificarVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro

        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="white")

        for i in range(3):
            self.frame.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.frame.grid_rowconfigure(i, weight=1)

        self.frame_superior = ctk.CTkFrame(self.frame, height=70, fg_color="#a8ad14", bg_color="#a8ad14")
        self.frame_superior.grid(row=0, column=0, sticky="new", columnspan=4)

        self.frame_derecho = ctk.CTkFrame(self.frame, width=80, fg_color="#a8ad14", bg_color="#a8ad14")
        self.frame_derecho.grid(row=0, column=11, sticky="ns", rowspan=12)

        self.frame_izquierda = ctk.CTkFrame(self.frame, width=80, fg_color="#a8ad14", bg_color="#a8ad14")
        self.frame_izquierda.grid(row=0, column=0, sticky="nws", rowspan=12)

        self.frame_inferior = ctk.CTkFrame(self.frame, height=80, fg_color="#a8ad14", bg_color="#a8ad14")
        self.frame_inferior.grid(row=11, column=0, sticky="sew", columnspan=4)

        self.etiqueta_titulo = ctk.CTkLabel(self.frame, text="Menú Modificar", font=("Arial", 28, "bold"))
        self.etiqueta_titulo.grid(row=0, column=1, pady=(90, 20), sticky="n")

        self.boton_productos = ctk.CTkButton(self.frame, text="Productos", width=200, height=50,fg_color="#054ac2",hover_color="#186afa",
                                             font=("Arial", 16, "bold"),corner_radius=50,command=self.controlador_maestro.modificar_productos)
        self.boton_productos.grid(row=1, column=2, pady=10)

        self.boton_sabores = ctk.CTkButton(self.frame, text="Sabores", width=200, height=50,fg_color="#054ac2",hover_color="#186afa",
                                           font=("Arial", 16, "bold"),corner_radius=50,command=self.controlador_maestro.modificar_sabores)
        self.boton_sabores.grid(row=2, column=2, pady=10)

        self.boton_usuarios = ctk.CTkButton(self.frame, text="Usuarios", width=200, height=50,
                                            font=("Arial", 16, "bold"),corner_radius=50,fg_color="#054ac2",hover_color="#186afa",
                                            command=self.controlador_maestro.modificar_usuarios)
        self.boton_usuarios.grid(row=3, column=2, pady=10)

        ruta_imagen = Path(__file__).resolve().parent.parent.parent.parent / "assets" / "modificar.png"
        imagen_gato_pequeno = ctk.CTkImage(Image.open(ruta_imagen), size=(320, 320))

        self.label_imagen1 = ctk.CTkLabel(self.frame, image=imagen_gato_pequeno, text="")
        self.label_imagen1.place(x=100,y=180)

        # Botón cancelar / regresar
        self.boton_cancelar = ctk.CTkButton(self.frame, text="Cancelar", font=("Arial", 14, "bold"),width=210,height=40,fg_color="#b81717",hover_color="#e70c0c",
                                            text_color="white",corner_radius=50, command=self.controlador_maestro.mostrar_menu_principal)
        self.boton_cancelar.grid(row=5, column=2, pady=20,padx=10)

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
