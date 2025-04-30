import customtkinter as ctk
import tkinter as tk
from src.Logica.Producto import agregar_sabor, eliminar_ultimo_sabor, guardar_producto

class Producto:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x750")
        self.app.title("Añadir Producto")

        self.sabores = []

        self.app.grid_columnconfigure((0, 1), weight=1)
        self.app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.titulo = ctk.CTkLabel(self.app, text="Registro de Producto",
                                   font=("Arial", 28, "bold"), text_color="white")
        self.titulo.grid(row=0, column=0, columnspan=2, pady=(30, 10))

        # Frame Producto
        self.frame_producto = ctk.CTkFrame(self.app, corner_radius=20)
        self.frame_producto.grid(row=1, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
        self.frame_producto.grid_columnconfigure(1, weight=1)

        self.label_nombre = ctk.CTkLabel(self.frame_producto, text="Nombre del producto:", font=("Arial", 16))
        self.label_nombre.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. Malanga", font=("Arial", 14))
        self.entry_nombre.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")

        self.label_precio_compra = ctk.CTkLabel(self.frame_producto, text="Precio de compra ($):", font=("Arial", 16))
        self.label_precio_compra.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_precio_compra = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 12", font=("Arial", 14))
        self.entry_precio_compra.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.label_precio_venta = ctk.CTkLabel(self.frame_producto, text="Precio de venta ($):", font=("Arial", 16))
        self.label_precio_venta.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="w")
        self.entry_precio_venta = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 18", font=("Arial", 14))
        self.entry_precio_venta.grid(row=2, column=1, padx=20, pady=(10, 20), sticky="ew")

        # CheckBox: Usar sabores
        self.usar_sabores = tk.BooleanVar(value=True)
        self.checkbox_sabores = ctk.CTkCheckBox(self.app, text="¿Agregar sabores al producto?",
                                                variable=self.usar_sabores, onvalue=True, offvalue=False,
                                                font=("Arial", 16), command=self.mostrar_ocultar_sabores)
        self.checkbox_sabores.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        # Título y Frame Sabores
        self.titulo_sabores = ctk.CTkLabel(self.app, text="Sabores del Producto",
                                           font=("Arial", 24, "bold"), text_color="white")
        self.titulo_sabores.grid(row=3, column=0, columnspan=2, pady=(10, 5))

        self.frame_sabores = ctk.CTkFrame(self.app, corner_radius=20)
        self.frame_sabores.grid(row=4, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
        self.frame_sabores.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame_sabores.grid_rowconfigure(1, weight=1)

        self.sabor_var = tk.StringVar()
        self.sabor_var.trace_add("write", self.actualizar_estado_boton)

        self.entry_sabor = ctk.CTkEntry(self.frame_sabores, textvariable=self.sabor_var,
                                        placeholder_text="Ej. Adobado", font=("Arial", 14))
        self.entry_sabor.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        self.btn_agregar_sabor = ctk.CTkButton(
            self.frame_sabores, text="Añadir", font=("Arial", 14, "bold"),
            command=self.agregar_sabor_interfaz
        )
        self.btn_agregar_sabor.grid(row=0, column=1, padx=10, pady=15)

        self.btn_eliminar_sabor = ctk.CTkButton(
            self.frame_sabores, text="Eliminar último", font=("Arial", 14, "bold"),
            fg_color="#D32F2F", hover_color="#B71C1C",
            command=self.eliminar_sabor_interfaz
        )
        self.btn_eliminar_sabor.grid(row=0, column=2, padx=10, pady=15)

        self.lista_sabores = ctk.CTkTextbox(self.frame_sabores, height=120, font=("Arial", 14))
        self.lista_sabores.grid(row=1, column=0, columnspan=3, padx=20, pady=(0, 10), sticky="nsew")
        self.lista_sabores.insert("0.0", "Sabores añadidos:\n")

        self.etiqueta_dinamica = ctk.CTkLabel(self.frame_sabores, text="", font=("Arial", 14), text_color="white")
        self.etiqueta_dinamica.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        self.btn_guardar = ctk.CTkButton(
            self.app, text="Guardar Producto",
            font=("Arial", 16, "bold"),
            fg_color="#4CAF50", hover_color="#45A049",
            command=self.guardar_producto_interfaz
        )
        self.btn_guardar.grid(row=5, column=0, columnspan=2, pady=30, padx=100, sticky="ew")

        self.actualizar_estado_boton()

    def mostrar_ocultar_sabores(self):
        if self.usar_sabores.get():
            self.titulo_sabores.grid()
            self.frame_sabores.grid()
        else:
            self.titulo_sabores.grid_remove()
            self.frame_sabores.grid_remove()
            self.sabores.clear()
            self.lista_sabores.delete("1.0", "end")
            self.lista_sabores.insert("0.0", "Sabores añadidos:\n")
            self.etiqueta_dinamica.configure(text="")

    def actualizar_estado_boton(self, *args):
        texto = self.sabor_var.get().strip()
        self.btn_agregar_sabor.configure(state="normal" if texto else "disabled")
        self.btn_eliminar_sabor.configure(state="normal" if self.sabores else "disabled")

    def agregar_sabor_interfaz(self):
        sabor = self.entry_sabor.get().strip()
        self.sabores, mensaje = agregar_sabor(sabor, self.sabores, self.lista_sabores)
        self.etiqueta_dinamica.configure(text=mensaje)
        self.entry_sabor.delete(0, "end")
        self.actualizar_estado_boton()

    def eliminar_sabor_interfaz(self):
        self.sabores = eliminar_ultimo_sabor(self.sabores, self.lista_sabores)
        self.etiqueta_dinamica.configure(text="Último sabor eliminado." if self.sabores else "No hay sabores para eliminar.")
        self.actualizar_estado_boton()

    def guardar_producto_interfaz(self):
        nombre = self.entry_nombre.get()
        precio_compra = self.entry_precio_compra.get()
        precio_venta = self.entry_precio_venta.get()
        sabores_a_guardar = self.sabores if self.usar_sabores.get() else []

        exito, mensaje = guardar_producto(nombre, precio_compra, precio_venta, sabores_a_guardar)
        self.etiqueta_dinamica.configure(text=mensaje)

        if exito:
            self.entry_nombre.delete(0, "end")
            self.entry_precio_compra.delete(0, "end")
            self.entry_precio_venta.delete(0, "end")
            self.sabores.clear()
            self.lista_sabores.delete("1.0", "end")
            self.lista_sabores.insert("0.0", "Sabores añadidos:\n")
            self.etiqueta_dinamica.configure(text="Producto guardado correctamente")
            self.actualizar_estado_boton()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    productos = Producto(app)
    app.mainloop()
