import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("850x650")
app.title("Inicio")

for i in range(3): app.grid_columnconfigure(i, weight=1)
for i in range(6): app.grid_rowconfigure(i, weight=1)

titulo = ctk.CTkLabel(app, text="Menú Principal", font=("Helvetica", 36, "bold"), text_color="white")
titulo.grid(row=0, column=0, columnspan=3, pady=(30, 20))

def crear_boton(texto, color="#3B8ED0", hover="#2F6BA8"):
    return ctk.CTkButton(app, text=texto, font=("Arial", 18, "bold"), height=60, width=250, corner_radius=20, fg_color=color, hover_color=hover)

boton_inventario = crear_boton("📦 Inventario")
boton_inventario.grid(row=1, column=0, padx=20, pady=15)

boton_finanzas = crear_boton("💰 Finanzas")
boton_finanzas.grid(row=1, column=1, padx=20, pady=15)

boton_ventas = crear_boton("🛒 Iniciar Venta", color="#4CAF50", hover="#3E8E41")
boton_ventas.grid(row=1, column=2, padx=20, pady=15)

boton_productos = crear_boton("🧾 Productos")
boton_productos.grid(row=2, column=0, padx=20, pady=15)

boton_modificar = crear_boton("✏️ Modificar")
boton_modificar.grid(row=2, column=1, padx=20, pady=15)

boton_consultas = crear_boton("🔍 Consultas")
boton_consultas.grid(row=3, column=1, padx=20, pady=15)  # Botón debajo de 'Modificar'

boton_eliminar = crear_boton("🗑️ Eliminar Elementos", color="#FF4C4C", hover="#CC3C3C")
boton_eliminar.grid(row=2, column=2, padx=20, pady=15)

etiqueta_version = ctk.CTkLabel(app, text="Versión 1.0 • Desarrollado por Arthyom596", font=("Arial", 12), text_color="gray")
etiqueta_version.grid(row=5, column=0, columnspan=3, pady=20)

app.mainloop()
