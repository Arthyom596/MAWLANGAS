import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x600")
app.title("Registro")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
for i in range(10):
    app.grid_rowconfigure(i, weight=1)

contenedor = ctk.CTkFrame(app, fg_color="white", corner_radius=10)
contenedor.grid(row=0, column=0, columnspan=3, rowspan=10, padx=100, pady=40, sticky="nsew")

for i in range(10):
    contenedor.grid_rowconfigure(i, weight=1)
contenedor.grid_columnconfigure(0, weight=0)
contenedor.grid_columnconfigure(1, weight=1)
contenedor.grid_columnconfigure(2, weight=0)

etiqueta_registro = ctk.CTkLabel(contenedor, text="REGISTRO", text_color="#1E1E1E", font=("Arial", 20, "bold"))
etiqueta_registro.grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky="nsew")

etiqueta_nombre = ctk.CTkLabel(contenedor, text="Nombre(s)", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_nombre.grid(row=1, column=0, padx=(20), pady=5, sticky="w")
entrada_nombre = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_nombre.grid(row=1, column=1, padx=20, pady=5, sticky="ew")

etiqueta_apellido_paterno = ctk.CTkLabel(contenedor, text="Apellido Paterno", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_apellido_paterno.grid(row=2, column=0, padx=(20), pady=5, sticky="w")
entrada_apellido_paterno = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_apellido_paterno.grid(row=2, column=1, padx=20, pady=5, sticky="ew")

etiqueta_apellido_materno = ctk.CTkLabel(contenedor, text="Apellido Materno", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_apellido_materno.grid(row=3, column=0, padx=(20), pady=5, sticky="w")
entrada_apellido_materno = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_apellido_materno.grid(row=3, column=1, padx=20, pady=5, sticky="ew")

etiqueta_usuario = ctk.CTkLabel(contenedor, text="Usuario", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_usuario.grid(row=4, column=0, padx=(20), pady=5, sticky="w")
entrada_usuario = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_usuario.grid(row=4, column=1, padx=20, pady=5, sticky="ew")

etiqueta_contrasena = ctk.CTkLabel(contenedor, text="Contraseña", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_contrasena.grid(row=5, column=0, padx=(20), pady=5, sticky="w")
entrada_contrasena = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10, show="*")
entrada_contrasena.grid(row=5, column=1, padx=20, pady=5, sticky="ew")

etiqueta_correo = ctk.CTkLabel(contenedor, text="Correo Electrónico", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_correo.grid(row=6, column=0, padx=(20), pady=5, sticky="w")
entrada_correo = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_correo.grid(row=6, column=1, padx=20, pady=5, sticky="ew")

boton_enviar_codigo = ctk.CTkButton(contenedor, text="Enviar código", corner_radius=10)
boton_enviar_codigo.grid(row=7, column=1, pady=10, padx=20,sticky="nsew")

etiqueta_otp = ctk.CTkLabel(contenedor, text="Código OTP", text_color="#1E1E1E", font=("Arial", 14))
etiqueta_otp.grid(row=8, column=0, padx=(20), pady=5, sticky="w")
entrada_otp = ctk.CTkEntry(contenedor, border_width=1, corner_radius=10)
entrada_otp.grid(row=8, column=1, padx=20, pady=5, sticky="ew")

boton_registrar = ctk.CTkButton(contenedor, text="Registrar", corner_radius=10)
boton_registrar.grid(row=9, column=0, padx=20, pady=10)

boton_cancelar = ctk.CTkButton(contenedor, text="Cancelar", corner_radius=10)
boton_cancelar.grid(row=9, column=1, padx=20, pady=10, sticky="e")

app.mainloop()
