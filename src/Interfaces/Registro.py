from tkinter import messagebox
import customtkinter as ctk
from src.Logica.Validaciones import *
from src.Logica.Otp import *
from src.Modelos.Usuario import crear_usuario

ctk.set_appearance_mode("dark")

# Configura la ventana principal
app = ctk.CTk()
app.geometry("800x600")
app.title("Registro")

# Define la estructura de columnas y filas
for i in range(3):
    app.grid_columnconfigure(i, weight=1)
for i in range(11):
    app.grid_rowconfigure(i, weight=1)

# Crea el contenedor principal
contenedor = ctk.CTkFrame(app, fg_color="white", corner_radius=10)
contenedor.grid(row=0, column=0, columnspan=3, rowspan=10, padx=100, pady=40, sticky="nsew")

# Configura la rejilla del contenedor
for i in range(10):
    contenedor.grid_rowconfigure(i, weight=1)
contenedor.grid_columnconfigure(0, weight=0)
contenedor.grid_columnconfigure(1, weight=1)
contenedor.grid_columnconfigure(2, weight=0)

def registrar_usuario():
    # Obtiene los datos ingresados por el usuario
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    nombre = entrada_nombre.get()
    apellido_p = entrada_apellido_paterno.get()
    apellido_m = entrada_apellido_materno.get()
    correo = entrada_correo.get()

    # Valida los datos con sus respectivos mensajes
    validaciones = [
        (validar_usuario(usuario),
         "El nombre de usuario debe tener entre 5 y 50 caracteres y solo puede contener letras y números"),
        (validar_contraseña(contrasena),
         "La contraseña debe tener entre 8 y 50 caracteres y contener al menos un número y un carácter especial"),
        (validar_nombre(nombre), "El nombre no puede estar vacío y solo debe contener letras"),
        (validar_nombre(apellido_p), "El apellido paterno no puede estar vacío y solo debe contener letras"),
        (validar_nombre(apellido_m), "El apellido materno no puede estar vacío y solo debe contener letras"),
        (validar_correo(correo), "Correo electrónico inválido"),
    ]

    # Muestra mensaje de error si alguna validación falla
    for valido, mensaje in validaciones:
        if not valido:
            etiqueta_dinamica.configure(text=mensaje, text_color="red")
            return

    try:
        #Crea el usuario si es valido
        crear_usuario(usuario, contrasena, nombre, apellido_p, apellido_m, correo)

        # Muestra mensaje de éxito
        etiqueta_dinamica.configure(text="Registro exitoso ✅", text_color="green")
        messagebox.showinfo("Registro", "¡Usuario registrado correctamente!")

        # Limpia todos los campos del formulario
        for entrada in (entrada_usuario, entrada_contrasena, entrada_nombre,
                        entrada_apellido_paterno, entrada_apellido_materno,
                        entrada_correo):
            entrada.delete(0, "end")
    except Exception as e:
        # Muestra mensaje de error en caso de excepción
        etiqueta_dinamica.configure(text=f"Error: {e}", text_color="red")
        messagebox.showerror("Error", f"Hubo un problema al registrar al usuario: {e}")

# Agrega etiquetas y campos de entrada
etiqueta_registro = ctk.CTkLabel(contenedor, text="REGISTRO", text_color="#1E1E1E", font=("Arial", 20, "bold"))
etiqueta_registro.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky="nsew")

etiqueta_nombre = ctk.CTkLabel(contenedor, text="Nombre(s)", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_nombre.grid(row=1, column=0, padx=20, pady=5, sticky="w")
entrada_nombre = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_nombre.grid(row=1, column=1, padx=20, pady=5, sticky="ew")

etiqueta_apellido_paterno = ctk.CTkLabel(contenedor, text="Apellido Paterno", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_apellido_paterno.grid(row=2, column=0, padx=20, pady=5, sticky="w")
entrada_apellido_paterno = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_apellido_paterno.grid(row=2, column=1, padx=20, pady=5, sticky="ew")

etiqueta_apellido_materno = ctk.CTkLabel(contenedor, text="Apellido Materno", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_apellido_materno.grid(row=3, column=0, padx=20, pady=5, sticky="w")
entrada_apellido_materno = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_apellido_materno.grid(row=3, column=1, padx=20, pady=5, sticky="ew")

etiqueta_usuario = ctk.CTkLabel(contenedor, text="Usuario", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_usuario.grid(row=4, column=0, padx=20, pady=5, sticky="w")
entrada_usuario = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_usuario.grid(row=4, column=1, padx=20, pady=5, sticky="ew")

etiqueta_contrasena = ctk.CTkLabel(contenedor, text="Contraseña", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_contrasena.grid(row=5, column=0, padx=20, pady=5, sticky="w")
entrada_contrasena = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10, show="*")
entrada_contrasena.grid(row=5, column=1, padx=20, pady=5, sticky="ew")

etiqueta_correo = ctk.CTkLabel(contenedor, text="Correo Electrónico", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_correo.grid(row=6, column=0, padx=20, pady=5, sticky="w")
entrada_correo = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_correo.grid(row=6, column=1, padx=20, pady=5, sticky="ew")

# Botón para enviar el código OTP al correo
boton_enviar_codigo = ctk.CTkButton(contenedor, text="Enviar código", corner_radius=10,
                                    command=lambda: manejar_otp(entrada_correo.get()))
boton_enviar_codigo.grid(row=7, column=1, pady=10, padx=20, sticky="nsew")

# Campo para ingresar el código OTP
etiqueta_otp = ctk.CTkLabel(contenedor, text="Código OTP", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_otp.grid(row=8, column=0, padx=20, pady=5, sticky="w")
entrada_otp = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_otp.grid(row=8, column=1, padx=20, pady=5, sticky="ew")

# Muestra mensajes dinámicos (error o éxito)
etiqueta_dinamica = ctk.CTkLabel(contenedor, text="", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_dinamica.grid(row=9, column=1, padx=20, pady=5, sticky="ew")

# Botón para registrar al usuario
boton_registrar = ctk.CTkButton(contenedor, text="Registrar", corner_radius=10, command=registrar_usuario)
boton_registrar.grid(row=10, column=0, padx=20, pady=10)

# Botón para cancelar el registro
boton_cancelar = ctk.CTkButton(contenedor, text="Cancelar", corner_radius=10)
boton_cancelar.grid(row=10, column=1, padx=20, pady=10, sticky="e")

app.mainloop()
