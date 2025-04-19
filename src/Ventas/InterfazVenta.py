import customtkinter as ctk

# Configuración de apariencia
ctk.set_appearance_mode("dark")

# Crear ventana principal
app = ctk.CTk()
app.geometry("800x600")
app.title("Venta")

# Configurar columnas y filas
for i in range(3):
    app.grid_columnconfigure(i, weight=1)
for i in range(10):
    app.grid_rowconfigure(i, weight=1)

# Título principal
etiqueta_titulo = ctk.CTkLabel(app, text="Venta", font=("Arial", 36, "bold"), text_color="white")
etiqueta_titulo.grid(row=0, column=1, pady=20, sticky="ew")

# Selección de producto
etiqueta_seleccion = ctk.CTkLabel(app, text="Seleccione su producto", font=("Arial", 16, "bold"))
etiqueta_seleccion.grid(row=1, column=1, pady=(0, 5), sticky="n")

combo_productos = ctk.CTkComboBox(app, values=["Malangas", "Maicitos"], width=200)
combo_productos.grid(row=2, column=1, pady=(0, 20), sticky="n")

# Checkbox preparada
check_preparado = ctk.CTkCheckBox(app, text="Preparada", font=("Arial", 14))
check_preparado.grid(row=3, column=1, pady=10, sticky="n")

# Entrada de cantidad
etiqueta_cantidad = ctk.CTkLabel(app, text="Cantidad", font=("Arial", 16, "bold"))
etiqueta_cantidad.grid(row=4, column=1, pady=(10, 5), sticky="n")

entrada_cantidad = ctk.CTkEntry(app, placeholder_text="Ingrese la cantidad", width=200)
entrada_cantidad.grid(row=5, column=1, pady=(0, 20), sticky="n")

# Selección de sabor
etiqueta_sabor = ctk.CTkLabel(app, text="Seleccione el sabor", font=("Arial", 16, "bold"))
etiqueta_sabor.grid(row=6, column=1, pady=(10, 5), sticky="n")

combo_sabor = ctk.CTkComboBox(app, values=["Queso", "Picante", "Natural", "Tocineta"], width=200)
combo_sabor.grid(row=7, column=1, pady=(0, 20), sticky="n")

# Botón de reinicio
boton_reiniciar = ctk.CTkButton(app, text="Reiniciar", font=("Arial", 18, "bold"), fg_color="red", text_color="white", width=150)
boton_reiniciar.grid(row=8, column=1, pady=30, sticky="n")

# Ejecutar app
app.mainloop()
