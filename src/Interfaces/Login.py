import customtkinter as ctk
from PIL import Image
from pathlib import Path
from src.Logica.Login import verificar_usuario
from src.Modelos.Usuario import buscar_usuario

class Login(ctk.CTk):
    def __init__(self, abrir_registro_callback):
        super().__init__()

        # Guardamos el callback que se pasa desde Main
        self.abrir_registro_callback = abrir_registro_callback

        # Configuración de la ventana
        ctk.set_appearance_mode("dark")
        self.geometry("800x500")
        self.title("Mawlangas Login")

        # Configuración de la grilla de la ventana
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Contenedor visual
        self.contenedor_visual = ctk.CTkFrame(self, fg_color="#1E1E1E", corner_radius=0)
        self.contenedor_visual.grid(row=0, column=0, sticky="nsew")
        self.contenedor_visual.grid_columnconfigure(0, weight=1)
        self.contenedor_visual.grid_rowconfigure((0, 1), weight=1)

        # Imagen
        ruta_imagen = Path(__file__).resolve().parent.parent.parent / "assets" / "Cat.png"
        imagen_gato = ctk.CTkImage(Image.open(ruta_imagen), size=(300, 300))
        self.imagen_label = ctk.CTkLabel(self.contenedor_visual, image=imagen_gato, text="")
        self.imagen_label.grid(row=0, column=0, pady=(60, 10))

        # Texto "Mawlangas"
        self.texto_mawlangas = ctk.CTkLabel(self.contenedor_visual, text="Mawlangas", font=("Arial", 30, "bold"), text_color="white")
        self.texto_mawlangas.grid(row=1, column=0)

        # Contenedor de datos
        self.contenedor_datos1 = ctk.CTkFrame(self, fg_color="#1E1E1E", corner_radius=0)
        self.contenedor_datos1.grid(row=0, column=1, sticky="nsew")
        self.contenedor_datos1.grid_rowconfigure(0, weight=1)
        self.contenedor_datos1.grid_columnconfigure(0, weight=1)

        # Segundo contenedor para el formulario
        self.contenedor_datos2 = ctk.CTkFrame(self.contenedor_datos1, fg_color="white", corner_radius=10)
        self.contenedor_datos2.grid(row=0, column=0, padx=20, pady=60, sticky="nsew")

        for i in range(7):
            self.contenedor_datos2.grid_rowconfigure(i, weight=1)
        self.contenedor_datos2.grid_columnconfigure(0, weight=1)

        # Campo de texto "Login"
        self.login_label = ctk.CTkLabel(self.contenedor_datos2, text="LOGIN", text_color="#1E1E1E", font=("Arial", 20, "bold"))
        self.login_label.grid(row=0, column=0, pady=(20, 10), sticky="w", padx=20)

        # Inputs para usuario y contraseña
        self.user_entry = ctk.CTkEntry(self.contenedor_datos2, placeholder_text="USER", border_width=1, corner_radius=0)
        self.user_entry.grid(row=1, column=0, padx=20, sticky="ew")

        self.password_entry = ctk.CTkEntry(self.contenedor_datos2, placeholder_text="PASSWORD", border_width=1, corner_radius=0, show="*")
        self.password_entry.grid(row=2, column=0, padx=20, sticky="ew")

        # Botón de login
        self.login_button = ctk.CTkButton(self.contenedor_datos2, text="LOGIN", fg_color="white", text_color="black", hover_color="#e6e6e6", border_width=1, border_color="grey", corner_radius=10, command=self.login_usuario)
        self.login_button.grid(row=3, column=0, pady=(10, 0), padx=60)

        # Botón de registro
        self.register_button = ctk.CTkButton(self.contenedor_datos2, text="REGISTER", fg_color="white", text_color="black", hover_color="#e6e6e6", border_width=1, border_color="grey", corner_radius=10, command=self.abrir_registro_callback)
        self.register_button.grid(row=4, column=0, pady=10, padx=60)

        # Etiqueta para mostrar mensajes dinámicos
        self.etiqueta_dinamica = ctk.CTkLabel(self.contenedor_datos2, text="", text_color="black", font=("Arial", 14))
        self.etiqueta_dinamica.grid(row=5, column=0, padx=20, pady=5, sticky="ew")

    def login_usuario(self):
        usuario = self.user_entry.get()
        contrasena = self.password_entry.get()

        usuario_encontrado = buscar_usuario(usuario)

        if usuario_encontrado:
            contrasena_almacenada = usuario_encontrado[2]

            if verificar_usuario(usuario, contrasena):
                print("Login exitoso")
                self.etiqueta_dinamica.configure(text="Login exitoso", text_color="green")
            else:
                print("Contraseña incorrecta")
                self.etiqueta_dinamica.configure(text="Contraseña incorrecta", text_color="red")
        else:
            print("Usuario no encontrado")
            self.etiqueta_dinamica.configure(text="Usuario no encontrado", text_color="red")

