from tkinter import messagebox
import customtkinter as ctk
from src.Logica.Validaciones import *
from src.Logica.Otp import manejar_otp
from src.Modelos.Usuario import crear_usuario


class Registro:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Registro")

        ctk.set_appearance_mode("dark")

        # Se configura la ventana principal
        for i in range(3):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(1):
            self.master.grid_rowconfigure(i, weight=1)

        # Se crea el contenedor principal
        self.contenedor = ctk.CTkFrame(self.master, fg_color="white", corner_radius=10)
        self.contenedor.grid(row=0, column=0, columnspan=3, rowspan=10, padx=100, pady=40, sticky="nsew")

        # Se configura el grid del formulario
        for i in range(10):
            self.contenedor.grid_rowconfigure(i, weight=1)
        for i in range(3):
            self.contenedor.grid_columnconfigure(i, weight=1)

        # Etiqueta de registro
        self.etiqueta_registro = ctk.CTkLabel(self.contenedor, text="REGISTRO", text_color="black",
                                              font=("Arial", 20, "bold"))
        self.etiqueta_registro.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky="nsew")

        # Etiqueta de usuario
        self.etiqueta_usuario = ctk.CTkLabel(self.contenedor, text="Usuario", text_color="black", font=("Arial", 14))
        self.etiqueta_usuario.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        # Entry para el usuario
        self.entrada_usuario = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10)
        self.entrada_usuario.grid(row=1, column=1, padx=20, pady=5, sticky="ew")

        # Etiqueta contrasena
        self.etiqueta_contrasena = ctk.CTkLabel(self.contenedor, text="Contrasena", text_color="black",
                                                font=("Arial", 14))
        self.etiqueta_contrasena.grid(row=2, column=0, padx=20, pady=5, sticky="w")

        # Entry para la contrasena
        self.entrada_contrasena = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10, show="*")
        self.entrada_contrasena.grid(row=2, column=1, padx=20, pady=5, sticky="ew")

        # Etiqueta para el nombre
        self.etiqueta_nombre = ctk.CTkLabel(self.contenedor, text="Nombres", text_color="black", font=("Arial", 14))
        self.etiqueta_nombre.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        self.entrada_nombre = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10)
        self.entrada_nombre.grid(row=3, column=1, padx=20, pady=5, sticky="ew")

        # Etiqueta apellido paterno
        self.etiqueta_apellido_paterno = ctk.CTkLabel(self.contenedor, text="Apellido Paterno", text_color="black",
                                                      font=("Arial", 14))
        self.etiqueta_apellido_paterno.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        self.entrada_apellido_paterno = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10)
        self.entrada_apellido_paterno.grid(row=4, column=1, padx=20, pady=5, sticky="ew")

        # Etiqueta apellido materno
        self.etiqueta_apellido_materno = ctk.CTkLabel(self.contenedor, text="Apellido Materno", text_color="black",
                                                      font=("Arial", 14))
        self.etiqueta_apellido_materno.grid(row=5, column=0, padx=20, pady=5, sticky="w")
        self.entrada_apellido_materno = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10)
        self.entrada_apellido_materno.grid(row=5, column=1, padx=20, pady=5, sticky="ew")

        # Etiqueta correo electronico
        self.etiqueta_correo = ctk.CTkLabel(self.contenedor, text="Correo Electronico", text_color="black",
                                            font=("Arial", 14))
        self.etiqueta_correo.grid(row=6, column=0, padx=20, pady=5, sticky="w")
        self.entrada_correo = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10)
        self.entrada_correo.grid(row=6, column=1, padx=20, pady=5, sticky="ew")

        # Boton para enviar el codigo OTP al correo
        self.boton_enviar_codigo = ctk.CTkButton(self.contenedor, text="Enviar codigo", corner_radius=10,
                                                 command=lambda: manejar_otp(self.entrada_correo.get()))
        self.boton_enviar_codigo.grid(row=7, column=1, pady=10, padx=20, sticky="nsew")

        # Campo para ingresar el codigo OTP
        self.etiqueta_otp = ctk.CTkLabel(self.contenedor, text="Codigo OTP", text_color="black", font=("Arial", 14))
        self.etiqueta_otp.grid(row=8, column=0, padx=20, pady=5, sticky="w")
        self.entrada_otp = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10)
        self.entrada_otp.grid(row=8, column=1, padx=20, pady=5, sticky="ew")

        # Muestra mensajes dinamicos
        self.etiqueta_dinamica = ctk.CTkLabel(self.contenedor, text="", text_color="black", font=("Arial", 14))
        self.etiqueta_dinamica.grid(row=9, column=1, padx=20, pady=5, sticky="ew")

        # Boton para registrar al usuario
        self.boton_registrar = ctk.CTkButton(self.contenedor, text="Registrar", corner_radius=10,
                                             command=self.registrar_usuario)
        self.boton_registrar.grid(row=10, column=0, padx=20, pady=10)

        # Boton para cancelar el registro
        self.boton_cancelar = ctk.CTkButton(self.contenedor, text="Cancelar", corner_radius=10)
        self.boton_cancelar.grid(row=10, column=1, padx=20, pady=10, sticky="e")

    def registrar_usuario(self):
        # Obtener entradas
        datos = {
            "usuario": self.entrada_usuario.get(),
            "contrasena": self.entrada_contrasena.get(),
            "nombre": self.entrada_nombre.get(),
            "apellido_p": self.entrada_apellido_paterno.get(),
            "apellido_m": self.entrada_apellido_materno.get(),
            "correo": self.entrada_correo.get()
        }

        # Lista de validaciones
        validaciones = [
            ("usuario", validar_usuario),
            ("contrasena", validar_contraseña),
            ("nombre", validar_nombre),
            ("apellido_p", validar_nombre),
            ("apellido_m", validar_nombre),
            ("correo", validar_correo)
        ]

        resultados = {}

        for clave, funcion in validaciones:
            valido, valor = funcion(datos[clave])
            if not valido:
                self.etiqueta_dinamica.configure(text=valor, text_color="red")
                messagebox.showerror("Error", valor)
                return
            resultados[clave] = valor

        try:
            crear_usuario(
                resultados["usuario"],
                resultados["contrasena"],
                resultados["nombre"],
                resultados["apellido_p"],
                resultados["apellido_m"],
                resultados["correo"]
            )

            self.etiqueta_dinamica.configure(text="Registro exitoso ✅", text_color="green")
            messagebox.showinfo("Registro", "Usuario registrado correctamente")

            for entrada in (self.entrada_usuario, self.entrada_contrasena, self.entrada_nombre,
                            self.entrada_apellido_paterno, self.entrada_apellido_materno,
                            self.entrada_correo):
                entrada.delete(0, "end")
        except Exception as e:
            self.etiqueta_dinamica.configure(text=f"Error: {e}", text_color="red")
            messagebox.showerror("Error", f"Hubo un problema al registrar al usuario: {e}")


# Inicializacion de la ventana
if __name__ == "__main__":
    root = ctk.CTk()
    app = Registro(root)
    root.mainloop()
