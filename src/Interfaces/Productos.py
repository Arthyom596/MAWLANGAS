import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x750")
app.title("Añadir Producto")

app.grid_columnconfigure((0, 1), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

titulo = ctk.CTkLabel(
    app, text="Registro de Producto",
    font=("Arial", 28, "bold"),
    text_color="white"
)
titulo.grid(row=0, column=0, columnspan=2, pady=(30, 10))

frame_producto = ctk.CTkFrame(app, corner_radius=20)
frame_producto.grid(row=1, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
frame_producto.grid_columnconfigure(1, weight=1)

label_nombre = ctk.CTkLabel(frame_producto, text="Nombre del producto:", font=("Arial", 16))
label_nombre.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

entry_nombre = ctk.CTkEntry(frame_producto, placeholder_text="Ej. Malanga", font=("Arial", 14))
entry_nombre.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")

label_precio_compra = ctk.CTkLabel(frame_producto, text="Precio de compra ($):", font=("Arial", 16))
label_precio_compra.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="w")

entry_precio_compra = ctk.CTkEntry(frame_producto, placeholder_text="Ej. 12", font=("Arial", 14))
entry_precio_compra.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="ew")

label_precio_venta = ctk.CTkLabel(frame_producto, text="Precio de venta ($):", font=("Arial", 16))
label_precio_venta.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="w")

entry_precio_venta = ctk.CTkEntry(frame_producto, placeholder_text="Ej. 18", font=("Arial", 14))
entry_precio_venta.grid(row=2, column=1, padx=20, pady=(10, 20), sticky="ew")

titulo_sabores = ctk.CTkLabel(
    app, text="Sabores del Producto",
    font=("Arial", 24, "bold"),
    text_color="white"
)
titulo_sabores.grid(row=2, column=0, columnspan=2, pady=(10, 5))

frame_sabores = ctk.CTkFrame(app, corner_radius=20)
frame_sabores.grid(row=3, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
frame_sabores.grid_columnconfigure(0, weight=1)

entry_sabor = ctk.CTkEntry(frame_sabores, placeholder_text="Agregar sabor (ej. Adobado)", font=("Arial", 14))
entry_sabor.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

btn_agregar_sabor = ctk.CTkButton(frame_sabores, text="Añadir Sabor", font=("Arial", 14, "bold"))
btn_agregar_sabor.grid(row=0, column=1, padx=20, pady=20)

lista_sabores = ctk.CTkTextbox(frame_sabores, height=100, font=("Arial", 14))
lista_sabores.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
lista_sabores.insert("0.0", "Sabores añadidos:\n")

btn_guardar = ctk.CTkButton(
    app, text="Guardar Producto y Sabores",
    font=("Arial", 16, "bold"),
    fg_color="#4CAF50", hover_color="#45A049"
)
btn_guardar.grid(row=4, column=0, columnspan=2, pady=30, padx=100, sticky="ew")

app.mainloop()
