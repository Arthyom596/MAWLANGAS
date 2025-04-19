import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x600")
app.title("Inventario")

# Configurar columnas y filas
for i in range(3):
    app.columnconfigure(i, weight=1)

for i in range(7):
    app.rowconfigure(i, weight=1)

# Título principal
etiqueta_inventario = ctk.CTkLabel(app, text="Inventario", font=("Helvetica", 36, "bold"), text_color="white")
etiqueta_inventario.grid(row=0, column=1, sticky="nsew")

# Etiqueta para selección de producto
etiqueta_seleccion = ctk.CTkLabel(app, text="Seleccione su producto", font=("Arial", 14, "bold"))
etiqueta_seleccion.grid(row=1, column=1, pady=(10, 0), sticky="n")

# ComboBox con opciones
combo_productos = ctk.CTkComboBox(app, values=["Malangas", "Maicitos"])
combo_productos.grid(row=2, column=1, pady=(0, 20), sticky="n")

# Etiquetas de productos (subidas una fila)
etiqueta_total = ctk.CTkLabel(app, text="Producto Total")
etiqueta_total.grid(row=2, column=0, sticky="nsew")

etiqueta_cantidad_total = ctk.CTkLabel(app, text="Cantidad: ")
etiqueta_cantidad_total.grid(row=3, column=0, sticky="nsew")

etiqueta_restante = ctk.CTkLabel(app, text="Producto Restante")
etiqueta_restante.grid(row=2, column=2, sticky="nsew")

etiqueta_cantidad_restante = ctk.CTkLabel(app, text="Cantidad: ")
etiqueta_cantidad_restante.grid(row=3, column=2, sticky="nsew")

etiqueta_vendido = ctk.CTkLabel(app, text="Producto Vendido")
etiqueta_vendido.grid(row=4, column=0, sticky="nsew")

etiqueta_cantidad_vendido = ctk.CTkLabel(app, text="Cantidad: ")
etiqueta_cantidad_vendido.grid(row=5, column=0, sticky="nsew")

etiqueta_mermado = ctk.CTkLabel(app, text="Producto Mermado")
etiqueta_mermado.grid(row=4, column=2, sticky="nsew")

etiqueta_cantidad_mermado = ctk.CTkLabel(app, text="Cantidad: ")
etiqueta_cantidad_mermado.grid(row=5, column=2, sticky="nsew")

# Ejecutar la app
app.mainloop()
