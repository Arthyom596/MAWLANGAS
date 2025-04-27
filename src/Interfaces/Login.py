import customtkinter as ctk
from PIL import Image
from pathlib import Path
from src.Interfaces.Registro import Registro
from src.Logica.Login import verificar_usuario
from src.Modelos.Usuario import buscar_usuario


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("800x600")

        ctk.set_appearance_mode("dark")

        # Configura el grid para que la ventana se ajuste adecuadamente
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # Se crea el contenedor para la parte visual del login
        self.contenedor_visual = ctk.CTkFrame(self.master, fg_color="#1E1E1E", corner_radius=0)
        self.contenedor_visual.grid(row=0, column=0, sticky="nsew")
        self.contenedor_visual.grid_columnconfigure(0, weight=1)
        self.contenedor_visual.grid_rowconfigure((0, 1), weight=1)

        # Ruta de la imagen del mawlango
        ruta_imagen = Path(__file__).resolve().parent.parent.parent / "assets" / "Cat.png"
        imagen_gato = ctk.CTkImage(Image.open(ruta_imagen), size=(300, 300))

        # Se coloca la imagen del gato en el contenedor
        self.imagen_label = ctk.CTkLabel(self.contenedor_visual, image=imagen_gato, text="")
        self.imagen_label.grid(row=0, column=0, pady=(60, 10))

        # Se coloca el texto de la marca en el contenedor
        self.texto_mawlangas = ctk.CTkLabel(self.contenedor_visual, text="Mawlangas", font=("Arial", 30, "bold"),
                                            text_color="white")
        self.texto_mawlangas.grid(row=1, column=0)

        # Se crea el contenedor para los datos del login
        self.contenedor_datos1 = ctk.CTkFrame(self.master, fg_color="#1E1E1E", corner_radius=0)
        self.contenedor_datos1.grid(row=0, column=1, sticky="nsew")
        self.contenedor_datos1.grid_rowconfigure(0, weight=1)
        self.contenedor_datos1.grid_columnconfigure(0, weight=1)

        # Se crea el contenedor para el formulario de login
        self.contenedor_datos2 = ctk.CTkFrame(self.contenedor_datos1, fg_color="white", corner_radius=10)
        self.contenedor_datos2.grid(row=0, column=0, padx=20, pady=60, sticky="nsew")

        # Configura el grid del formulario de login
        for i in range(7):
            self.contenedor_datos2.grid_rowconfigure(i, weight=1)
        self.contenedor_datos2.grid_columnconfigure(0, weight=1)

        # Etiqueta de login
        self.login_label = ctk.CTkLabel(self.contenedor_datos2, text="LOGIN", text_color="#1E1E1E",
                                        font=("Arial", 20, "bold"))
        self.login_label.grid(row=0, column=0, pady=(20, 10), sticky="w", padx=20)

        # Campo de entrada para el usuario
        self.user_entry = ctk.CTkEntry(self.contenedor_datos2, placeholder_text="USER", border_width=1, corner_radius=0)
        self.user_entry.grid(row=1, column=0, padx=20, sticky="ew")

        # Campo de entrada para la contraseña
        self.password_entry = ctk.CTkEntry(self.contenedor_datos2, placeholder_text="PASSWORD", border_width=1,
                                           corner_radius=0, show="*")
        self.password_entry.grid(row=2, column=0, padx=20, sticky="ew")

        # Boton para hacer login
        self.login_button = ctk.CTkButton(self.contenedor_datos2, text="LOGIN", fg_color="white", text_color="black",
                                          hover_color="#e6e6e6", border_width=1, border_color="grey", corner_radius=10,
                                          command=self.login_usuario)
        self.login_button.grid(row=3, column=0, pady=(10, 0), padx=60)

        # Boton para registrar un nuevo usuario
        self.register_button = ctk.CTkButton(self.contenedor_datos2, text="REGISTER", fg_color="white",
                                             text_color="black",
                                             hover_color="#e6e6e6", border_width=1, border_color="grey",
                                             corner_radius=10, command=self.abrir_registro)
        self.register_button.grid(row=4, column=0, pady=10, padx=60)

        self.etiqueta_dinamica = ctk.CTkLabel(self.contenedor_datos2, text="", text_color="black", font=("Arial", 14))
        self.etiqueta_dinamica.grid(row=5, column=0, padx=20, pady=5, sticky="ew")

    # Función para abrir la ventana de registro
    def abrir_registro(self):
        self.master.withdraw()  # Oculta la ventana de Login
        toplevel = ctk.CTkToplevel(self.master)  # Crea la ventana de Registro
        app = Registro(toplevel)  # Carga la clase Registro

        # Vuelve a mostrar Login cuando se cierre la ventana de Registro
        toplevel.protocol("WM_DELETE_WINDOW", lambda: (self.master.deiconify(), toplevel.destroy()))

    def login_usuario(self):
        usuario = self.user_entry.get()  # Obtiene el usuario ingresado
        contrasena = self.password_entry.get()  # Obtiene la contraseña ingresada

        # Llama a la función buscar_usuario para obtener los datos del usuario
        usuario_encontrado = buscar_usuario(usuario)

        if usuario_encontrado:
            # Si el usuario existe, obtenemos el hash almacenado de la contraseña
            contrasena_almacenada = usuario_encontrado[2]  # Suponiendo que el campo de la contraseña es el tercero

            # Verificamos si la contraseña ingresada corresponde al hash almacenado usando la función
            if verificar_usuario(usuario, contrasena):  # Llamada correcta a verificar_usuario
                print("Login exitoso")
                self.etiqueta_dinamica.configure(text="Login exitoso", text_color="green")
            else:
                # Si la contraseña es incorrecta
                print("Contraseña incorrecta")
                self.etiqueta_dinamica.configure(text="Contraseña incorrecta", text_color="red")
        else:
            # Si el usuario no existe, muestra un mensaje
            print("Usuario no encontrado")
            self.etiqueta_dinamica.configure(text="Usuario no encontrado", text_color="red")


# Inicialización de la ventana
if __name__ == "__main__":
    root = ctk.CTk()
    app = Login(root)
    root.mainloop()
