import customtkinter as ctk

# --- Configuración de la apariencia ---
ctk.set_appearance_mode("dark")

# --- Configuración principal de la app ---
app = ctk.CTk()
app.geometry("800x600")
app.title("Administración del Inventario")

# Configuración de columnas y filas para centrar
for i in range(3):
    app.grid_columnconfigure(i, weight=1)

for i in range(9):
    app.grid_rowconfigure(i, weight=1)

# --- Datos de productos y sabores ---
opciones_producto = ["Malangas", "Maicitos"]
sabores_malanga = ["Takis Rojo", "Takis azul", "Adobadas", "Habanero", "Especias", "Jalapeño"]
sabores_maicito = ["Ranchero", "Queso", "Takis", "Jalapeño", "Natural"]

# --- Función para actualizar sabores según el producto ---
def actualizar_sabores(seleccion):
    if seleccion == "Malangas":
        combo_sabores_agregar.configure(values=sabores_malanga)
        combo_sabores_agregar.set(sabores_malanga[0])
        combo_sabores_mermar.configure(values=sabores_malanga)
        combo_sabores_mermar.set(sabores_malanga[0])
    elif seleccion == "Maicitos":
        combo_sabores_agregar.configure(values=sabores_maicito)
        combo_sabores_agregar.set(sabores_maicito[0])
        combo_sabores_mermar.configure(values=sabores_maicito)
        combo_sabores_mermar.set(sabores_maicito[0])

# --- Título ---
etiqueta_titulo = ctk.CTkLabel(
    app, text="Administración del Inventario", font=("Arial", 36, "bold")
)
etiqueta_titulo.grid(row=0, column=1, pady=10, sticky="n")

# --- Sección: Escoger producto ---
etiqueta_producto = ctk.CTkLabel(
    app, text="Escoja el producto:", font=("Arial", 16)
)
etiqueta_producto.grid(row=1, column=1, sticky="n", pady=5)

combo_producto = ctk.CTkComboBox(
    app, values=opciones_producto, command=actualizar_sabores, width=200,
    font=("Arial", 14)
)
combo_producto.grid(row=2, column=1, pady=5)
combo_producto.set("Malangas")

# --- Sección: Agregar productos ---
etiqueta_agregar = ctk.CTkLabel(
    app, text="Agregar Productos", font=("Arial", 18, "bold")
)
etiqueta_agregar.grid(row=3, column=1, pady=10, sticky="n")

frame_agregar = ctk.CTkFrame(app, fg_color="transparent")
frame_agregar.grid(row=4, column=1, pady=5)

combo_sabores_agregar = ctk.CTkComboBox(
    frame_agregar, values=sabores_malanga, width=140, font=("Arial", 14)
)
combo_sabores_agregar.grid(row=0, column=0, padx=5)

entrada_cantidad_agregar = ctk.CTkEntry(
    frame_agregar, placeholder_text="Cantidad", width=100, font=("Arial", 14)
)
entrada_cantidad_agregar.grid(row=0, column=1, padx=5)

boton_agregar = ctk.CTkButton(
    frame_agregar, text="Agregar", width=100, font=("Arial", 14, "bold")
)
boton_agregar.grid(row=0, column=2, padx=5)

# --- Sección: Mermar productos ---
etiqueta_mermar = ctk.CTkLabel(
    app, text="Mermar Productos", font=("Arial", 18, "bold")
)
etiqueta_mermar.grid(row=5, column=1, pady=10, sticky="n")

frame_mermar = ctk.CTkFrame(app, fg_color="transparent")
frame_mermar.grid(row=6, column=1, pady=5)

combo_sabores_mermar = ctk.CTkComboBox(
    frame_mermar, values=sabores_malanga, width=140, font=("Arial", 14)
)
combo_sabores_mermar.grid(row=0, column=0, padx=5)

entrada_cantidad_mermar = ctk.CTkEntry(
    frame_mermar, placeholder_text="Cantidad", width=100, font=("Arial", 14)
)
entrada_cantidad_mermar.grid(row=0, column=1, padx=5)

boton_mermar = ctk.CTkButton(
    frame_mermar, text="Mermar", width=100, font=("Arial", 14, "bold")
)
boton_mermar.grid(row=0, column=2, padx=5)

# --- Inicialización por defecto ---
actualizar_sabores("Malangas")

# --- Ejecutar aplicación ---
app.mainloop()
