import customtkinter as ctk

# --- Configuración de apariencia ---
ctk.set_appearance_mode("dark")

# --- Configuración principal ---
app = ctk.CTk()
app.geometry("800x600")
app.title("Finanzas")

# Configurar columnas y filas
for i in range(5):
    app.grid_columnconfigure(i, weight=1)

for i in range(9):
    app.grid_rowconfigure(i, weight=1)

# --- Título principal ---
etiqueta_titulo = ctk.CTkLabel(
    app, text="Finanzas", font=("Arial", 36, "bold")
)
etiqueta_titulo.grid(row=0, column=1, columnspan=3, pady=(30, 20), sticky="n")

# --- Sección Gasto ---
btn_gasto = ctk.CTkButton(app, text="Agregar Gasto", font=("Arial", 16, "bold"))
btn_gasto.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

entrada_gasto = ctk.CTkEntry(app, placeholder_text="Cantidad", font=("Arial", 14), text_color="white")
entrada_gasto.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

btn_agregar_gasto = ctk.CTkButton(app, text="Agregar", font=("Arial", 14, "bold"))
btn_agregar_gasto.grid(row=1, column=3, padx=20, pady=10, sticky="ew")

etiqueta_concepto_gasto = ctk.CTkLabel(app, text="CONCEPTO", font=("Arial", 14), text_color="white")
etiqueta_concepto_gasto.grid(row=2, column=1, padx=20, pady=(5, 5), sticky="ew")

entrada_concepto_gasto = ctk.CTkEntry(app, placeholder_text="Escriba el concepto")
entrada_concepto_gasto.grid(row=2, column=2, columnspan=2, padx=10, pady=(5, 10), sticky="ew")

# --- Sección Ingreso ---
btn_ingreso = ctk.CTkButton(app, text="Agregar Ingreso", font=("Arial", 16, "bold"))
btn_ingreso.grid(row=4, column=1, padx=20, pady=(40, 10), sticky="ew")

entrada_ingreso = ctk.CTkEntry(app, placeholder_text="Cantidad", font=("Arial", 14), text_color="white")
entrada_ingreso.grid(row=4, column=2, padx=10, pady=(40, 10), sticky="ew")

btn_agregar_ingreso = ctk.CTkButton(app, text="Agregar", font=("Arial", 14, "bold"))
btn_agregar_ingreso.grid(row=4, column=3, padx=20, pady=(40, 10), sticky="ew")

etiqueta_concepto_ingreso = ctk.CTkLabel(app, text="CONCEPTO", font=("Arial", 14), text_color="white")
etiqueta_concepto_ingreso.grid(row=5, column=1, padx=20, pady=(5, 5), sticky="ew")

entrada_concepto_ingreso = ctk.CTkEntry(app, placeholder_text="Escriba el concepto")
entrada_concepto_ingreso.grid(row=5, column=2, columnspan=2, padx=10, pady=(5, 10), sticky="ew")

# --- Ejecutar la app ---
app.mainloop()
