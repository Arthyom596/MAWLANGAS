import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x600")
app.title("Finanzas")

# Configurar columnas y filas
for i in range(3):
    app.columnconfigure(i, weight=1)

for i in range(7):
    app.rowconfigure(i, weight=1)

# Título principal
etiqueta_finanzas = ctk.CTkLabel(app, text="Finanzas", font=("Helvetica", 36, "bold"), text_color="white")
etiqueta_finanzas.grid(row=0, column=1, sticky="nsew")

# Etiqueta para selección de producto
etiqueta_seleccion = ctk.CTkLabel(app, text="Seleccione su producto", font=("Arial", 14, "bold"))
etiqueta_seleccion.grid(row=1, column=1, pady=(10, 0), sticky="n")

# ComboBox con opciones
combo_productos = ctk.CTkComboBox(app, values=["Malangas", "Maicitos"])
combo_productos.grid(row=2, column=1, pady=(0, 20), sticky="n")


etiqueta_ganancia = ctk.CTkLabel(app, text="Ganancia Total")
etiqueta_ganancia.grid(row=2, column=0, sticky="nsew")

etiqueta_cantidad_total = ctk.CTkLabel(app, text="Cantidad: ")
etiqueta_cantidad_total.grid(row=3, column=0, sticky="nsew")

etiqueta_restante = ctk.CTkLabel(app, text="Inversion Restante")
etiqueta_restante.grid(row=2, column=2, sticky="nsew")

etiqueta_cantidad_restante = ctk.CTkLabel(app, text="Cantidad: ")
etiqueta_cantidad_restante.grid(row=3, column=2, sticky="nsew")

etiqueta_gasto = ctk.CTkLabel(app, text="Gasto Total")
etiqueta_gasto.grid(row=4, column=0, sticky="nsew")

dinero_total=ctk.CTkLabel(app, text="Dinero Total")
dinero_total.grid(row=4, column=1, sticky="nsew")

saldo_total=ctk.CTkLabel(app, text="Saldo Total")
saldo_total.grid(row=5, column=1, sticky="nsew")


etiqueta_cantidad_vendido = ctk.CTkLabel(app, text="Cantidad: ")
etiqueta_cantidad_vendido.grid(row=5, column=0, sticky="nsew")

etiqueta_merma = ctk.CTkLabel(app, text="Merma")
etiqueta_merma.grid(row=4, column=2, sticky="nsew")

etiqueta_cantidad_mermado = ctk.CTkLabel(app, text="Cantidad: ")
etiqueta_cantidad_mermado.grid(row=5, column=2, sticky="nsew")

# Ejecutar la app
app.mainloop()
