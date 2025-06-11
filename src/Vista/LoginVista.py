import customtkinter as ctk
from PIL import Image
from pathlib import Path
from src.Controlador.LoginControlador import LoginControlador

class LoginVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro

        # Crear frame
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="black")

        self.controlador = LoginControlador(self, self.controlador_maestro)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        # Contenedor visual
        self.contenedor_visual = ctk.CTkFrame(self.frame, fg_color="#1E1E1E", corner_radius=0)
        self.contenedor_visual.grid(row=0, column=0, sticky="nsew")
        self.contenedor_visual.grid_columnconfigure(0, weight=1)
        self.contenedor_visual.grid_rowconfigure((0, 1), weight=1)

        # Imagen del gato
        ruta_imagen = Path(__file__).resolve().parent.parent.parent / "assets" / "Cat.png"
        imagen_gato = ctk.CTkImage(Image.open(ruta_imagen), size=(300, 300))
        self.imagen_label = ctk.CTkLabel(self.contenedor_visual, image=imagen_gato, text="")
        self.imagen_label.grid(row=0, column=0, pady=(60, 10))

        # Texto Mawlangas
        self.texto_mawlangas = ctk.CTkLabel(self.contenedor_visual, text="Mawlangas", font=("Arial", 30, "bold"), text_color="white")
        self.texto_mawlangas.grid(row=1, column=0)

        # Contenedor de datos
        self.contenedor_datos1 = ctk.CTkFrame(self.frame, fg_color="#1E1E1E", corner_radius=0)
        self.contenedor_datos1.grid(row=0, column=1, sticky="nsew")
        self.contenedor_datos1.grid_rowconfigure(0, weight=1)
        self.contenedor_datos1.grid_columnconfigure(0, weight=1)

        # Formulario
        self.contenedor_datos2 = ctk.CTkFrame(self.contenedor_datos1, fg_color="white", corner_radius=10)
        self.contenedor_datos2.grid(row=0, column=0, padx=20, pady=60, sticky="nsew")

        for i in range(7):
            self.contenedor_datos2.grid_rowconfigure(i, weight=1)
        self.contenedor_datos2.grid_columnconfigure(0, weight=1)

        # Título
        self.login_label = ctk.CTkLabel(self.contenedor_datos2, text="Iniciar Sesion", text_color="#1E1E1E", font=("Arial", 20, "bold"))
        self.login_label.grid(row=0, column=0, pady=(20, 10), sticky="w", padx=20)

        # Usuario
        self.user_entry = ctk.CTkEntry(self.contenedor_datos2, placeholder_text="Usuario", border_width=1, corner_radius=0)
        self.user_entry.grid(row=1, column=0, padx=20, sticky="ew")

        # Cargar imágenes del ojito
        ruta_ojito_abierto = Path(__file__).resolve().parent.parent.parent / "assets" / "ojito_abierto.png"
        ruta_ojito_cerrado = Path(__file__).resolve().parent.parent.parent / "assets" / "ojito_cerrado.png"
        self.ojito_abierto = ctk.CTkImage(Image.open(ruta_ojito_abierto), size=(20, 20))
        self.ojito_cerrado = ctk.CTkImage(Image.open(ruta_ojito_cerrado), size=(20, 20))

        # Frame contenedor de contraseña + ojito
        self.password_frame = ctk.CTkFrame(self.contenedor_datos2, fg_color="transparent")
        self.password_frame.grid(row=2, column=0, padx=20, sticky="ew")
        self.password_frame.grid_columnconfigure(0, weight=1)
        self.password_frame.grid_columnconfigure(1, weight=0)

        # Entrada de contraseña
        self.password_entry = ctk.CTkEntry(self.password_frame, placeholder_text="Contraseña", border_width=1, corner_radius=0, show="*")
        self.password_entry.grid(row=0, column=0, sticky="ew")

        # Botón de ojito
        self.ver_password = False
        self.ojito_button = ctk.CTkButton(
            self.password_frame,
            text="",
            image=self.ojito_cerrado,
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#d9d9d9",
            command=self.toggle_password
        )
        self.ojito_button.grid(row=0, column=1, padx=(5, 0))

        # Botón login
        self.login_button = ctk.CTkButton(
            self.contenedor_datos2,
            text="Iniciar Sesion",
            fg_color="white",
            text_color="black",
            hover_color="#e6e6e6",
            border_width=1,
            border_color="grey",
            corner_radius=10,
            command=self.login_usuario
        )
        self.login_button.grid(row=3, column=0, pady=(10, 0), padx=60)

        # Botón registro
        self.register_button = ctk.CTkButton(
            self.contenedor_datos2,
            text="Registrate",
            fg_color="white",
            text_color="black",
            hover_color="#e6e6e6",
            border_width=1,
            border_color="grey",
            corner_radius=10,
            command=self.ir_a_registro
        )
        self.register_button.grid(row=4, column=0, pady=10, padx=60)

        # Mensaje dinámico
        self.etiqueta_dinamica = ctk.CTkLabel(self.contenedor_datos2, text="", text_color="black", font=("Arial", 14))
        self.etiqueta_dinamica.grid(row=5, column=0, padx=20, pady=5, sticky="ew")

    def toggle_password(self):
        self.ver_password = not self.ver_password
        if self.ver_password:
            self.password_entry.configure(show="")
            self.ojito_button.configure(image=self.ojito_abierto)
        else:
            self.password_entry.configure(show="*")
            self.ojito_button.configure(image=self.ojito_cerrado)

    def ir_a_registro(self):
        self.controlador_maestro.mostrar_registro()

    def login_usuario(self):
        usuario = self.user_entry.get()
        contrasena = self.password_entry.get()
        self.controlador.login_usuario(usuario, contrasena)

    def mostrar_mensaje(self, mensaje, color):
        self.etiqueta_dinamica.configure(text=mensaje, text_color=color)


# Controlador de prueba
class ControladorMaestroFalso:
    def mostrar_menu_principal(self):
        print("menu principal")

    def mostrar_registro(self):
        print("registro")


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("850x650")
    root.title("Productos")

    falso_maestro = ControladorMaestroFalso()
    LoginVista(root, controlador_maestro=falso_maestro)

    root.mainloop()
