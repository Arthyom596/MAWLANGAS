import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x600")
app.title("Eliminar")

for i in range(3):
    app.grid_columnconfigure(i, weight=1)
for i in range(7):
    app.grid_rowconfigure(i, weight=1)

etiqueta_titulo = ctk.CTkLabel(app, text="Reiniciar", font=("Arial", 36, "bold"), text_color="white")
etiqueta_titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="nsew")

etiqueta_subtitulo = ctk.CTkLabel(app, text="Marque las opciones", font=("Arial", 18, "bold"), text_color="white")
etiqueta_subtitulo.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

check_inventario = ctk.CTkCheckBox(app, text="Inventario")
check_inventario.grid(row=2, column=1, pady=5, sticky="ew", padx=100)

check_finanzas = ctk.CTkCheckBox(app, text="Finanzas")
check_finanzas.grid(row=3, column=1, pady=5, sticky="ew", padx=100)

check_productos = ctk.CTkCheckBox(app, text="Productos")
check_productos.grid(row=4, column=1, pady=5, sticky="ew", padx=100)

boton_reiniciar = ctk.CTkButton(app, text="Reiniciar", font=("Arial", 18, "bold"), fg_color="red", text_color="white")
boton_reiniciar.grid(row=5, column=1, pady=30, sticky="ew", padx=100)

app.mainloop()
