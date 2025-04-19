import customtkinter as ctk

# Configuración inicial
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x600")
app.title("Inicio")

# Configurar columnas y filas
for i in range(3):
    app.grid_columnconfigure(i, weight=1)
for i in range(5):
    app.grid_rowconfigure(i, weight=1)

# Etiqueta del menú
etiqueta_menu = ctk.CTkLabel(
    app,
    text="Menú Principal",
    font=("Helvetica", 36, "bold"),
    text_color="white")
etiqueta_menu.grid(row=0, column=0, columnspan=3, pady=(20, 10))

# Estilo uniforme para los botones
btn_width = 220
btn_height = 55
btn_radius = 20

# Botones principales
boton_inventario = ctk.CTkButton(app, text="Inventario", width=btn_width, height=btn_height, corner_radius=btn_radius)
boton_inventario.grid(row=1, column=0, padx=20, pady=10)

boton_finanzas = ctk.CTkButton(app, text="Finanzas", width=btn_width, height=btn_height, corner_radius=btn_radius)
boton_finanzas.grid(row=1, column=2, padx=20, pady=10)

boton_consultas = ctk.CTkButton(app, text="Consultas", width=btn_width, height=btn_height, corner_radius=btn_radius)
boton_consultas.grid(row=2, column=0, padx=20, pady=10)

boton_esquemas = ctk.CTkButton(app, text="Esquemas", width=btn_width, height=btn_height, corner_radius=btn_radius)
boton_esquemas.grid(row=2, column=2, padx=20, pady=10)

boton_reiniciar = ctk.CTkButton(
    app,
    text="Reiniciar Listas",
    width=btn_width,
    height=btn_height,
    corner_radius=btn_radius,
    fg_color="#FF4C4C",
    hover_color="#CC3C3C"
)
boton_reiniciar.grid(row=3, column=0, padx=20, pady=10)

boton_venta = ctk.CTkButton(
    app,
    text="Iniciar Venta",
    width=btn_width,
    height=btn_height,
    corner_radius=btn_radius,
    fg_color="#4CAF50",
    hover_color="#3E8E41"
)
boton_venta.grid(row=3, column=2, padx=20, pady=10)

# Espacio extra al final
espacio = ctk.CTkLabel(app, text="")
espacio.grid(row=4, column=0, columnspan=3)

app.mainloop()
