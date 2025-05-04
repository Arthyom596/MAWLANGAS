# src/Vista/ProductoVista.py

import customtkinter as ctk
import tkinter as tk
from src.Controlador.ProductoControlador import ProductoControlador

class ProductoVista:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x750")
        self.app.title("Añadir Producto")

        self.controlador = ProductoControlador(self) #Se crea una instancia del controlador

        #Se ajusta la venta con grid
        self.app.grid_columnconfigure((0, 1), weight=1)
        self.app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.titulo = ctk.CTkLabel(self.app, text="Registro de Producto",font=("Arial", 28, "bold"), text_color="white")
        self.titulo.grid(row=0, column=0, columnspan=2, pady=(30, 10))

        #Se crea un contenedor para la informacion del producto
        self.frame_producto = ctk.CTkFrame(self.app, corner_radius=20)
        self.frame_producto.grid(row=1, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
        self.frame_producto.grid_columnconfigure(1, weight=1)

        #Creacion de la etiqueta de producto y su entrada
        self.label_nombre = ctk.CTkLabel(self.frame_producto, text="Nombre del producto:", font=("Arial", 16))
        self.label_nombre.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. Malanga", font=("Arial", 14))
        self.entry_nombre.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")

        #Creacion de la etiqueta de precio_compra y su entrada
        self.label_precio_compra = ctk.CTkLabel(self.frame_producto, text="Precio de compra ($):", font=("Arial", 16))
        self.label_precio_compra.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_precio_compra = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 12", font=("Arial", 14))
        self.entry_precio_compra.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        # Creacion de la etiqueta de precio_venta y su entrada
        self.label_precio_venta = ctk.CTkLabel(self.frame_producto, text="Precio de venta ($):", font=("Arial", 16))
        self.label_precio_venta.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="w")
        self.entry_precio_venta = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 18", font=("Arial", 14))
        self.entry_precio_venta.grid(row=2, column=1, padx=20, pady=(10, 20), sticky="ew")

        # Usamos CTkSwitch en lugar de CheckBox y lo dejamos "prendido" por defecto
        self.switch_sabores = ctk.CTkSwitch(self.app, text="¿Agregar sabores al producto?",
                                            onvalue=True, offvalue=False,
                                            font=("Arial", 16), command=self.mostrar_ocultar_sabores,
                                            variable=tk.BooleanVar(value=True))  # Estado inicial "prendido"
        self.switch_sabores.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        self.titulo_sabores = ctk.CTkLabel(self.app, text="Sabores del Producto",
                                           font=("Arial", 24, "bold"), text_color="white")
        self.titulo_sabores.grid(row=3, column=0, columnspan=2, pady=(10, 5))

        self.frame_sabores = ctk.CTkFrame(self.app, corner_radius=20)
        self.frame_sabores.grid(row=4, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
        self.frame_sabores.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame_sabores.grid_rowconfigure(1, weight=1)

        self.sabor_var = tk.StringVar()
        self.sabor_var.trace_add("write", lambda *args: self.actualizar_estado_boton(self.controlador.sabores))

        self.entry_sabor = ctk.CTkEntry(self.frame_sabores, textvariable=self.sabor_var,
                                        placeholder_text="Ej. Adobado", font=("Arial", 14))
        self.entry_sabor.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        self.btn_agregar_sabor = ctk.CTkButton(
            self.frame_sabores, text="Añadir", font=("Arial", 14, "bold"),
            command=lambda: self.controlador.agregar_sabor(self.entry_sabor.get().strip())
        )
        self.btn_agregar_sabor.grid(row=0, column=1, padx=10, pady=15)

        self.btn_eliminar_sabor = ctk.CTkButton(
            self.frame_sabores, text="Eliminar último", font=("Arial", 14, "bold"),
            fg_color="#D32F2F", hover_color="#B71C1C",
            command=self.controlador.eliminar_sabor
        )
        self.btn_eliminar_sabor.grid(row=0, column=2, padx=10, pady=15)

        self.lista_sabores = ctk.CTkTextbox(self.frame_sabores, height=120, font=("Arial", 14))
        self.lista_sabores.grid(row=1, column=0, columnspan=3, padx=20, pady=(0, 10), sticky="nsew")
        self.lista_sabores.insert("0.0", "Sabores añadidos:\n")

        self.etiqueta_dinamica = ctk.CTkLabel(self.frame_sabores, text="", font=("Arial", 14), text_color="white")
        self.etiqueta_dinamica.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        self.btn_guardar = ctk.CTkButton(
            self.app, text="Guardar Producto", font=("Arial", 16, "bold"),
            fg_color="#4CAF50", hover_color="#45A049",
            command=lambda: self.controlador.guardar_producto(
                self.entry_nombre.get(),
                self.entry_precio_compra.get(),
                self.entry_precio_venta.get(),
                self.switch_sabores.get()
            )
        )
        self.btn_guardar.grid(row=5, column=0, columnspan=2, pady=30, padx=100, sticky="ew")

        self.actualizar_estado_boton(self.controlador.sabores)

    def mostrar_ocultar_sabores(self):
        if self.switch_sabores.get():
            self.titulo_sabores.grid()
            self.frame_sabores.grid()
        else:
            self.titulo_sabores.grid_remove()
            self.frame_sabores.grid_remove()
            self.controlador.sabores.clear()
            self.actualizar_textbox_sabores([])
            self.etiqueta_dinamica.configure(text="")
        self.actualizar_estado_boton(self.controlador.sabores)

    def actualizar_estado_boton(self, sabores=None):
        texto = self.sabor_var.get().strip()
        self.btn_agregar_sabor.configure(state="normal" if texto else "disabled")
        self.btn_eliminar_sabor.configure(state="normal" if sabores else "disabled")
        if self.switch_sabores.get() and not sabores:
            self.btn_guardar.configure(state="disabled")
        else:
            self.btn_guardar.configure(state="normal")

    def mostrar_mensaje(self, texto):
        self.etiqueta_dinamica.configure(text=texto)

    def limpiar_entry_sabor(self):
        self.entry_sabor.delete(0, "end")

    def reiniciar_formulario(self):
        self.entry_nombre.delete(0, "end")
        self.entry_precio_compra.delete(0, "end")
        self.entry_precio_venta.delete(0, "end")
        self.actualizar_textbox_sabores([])
        self.etiqueta_dinamica.configure(text="")
        self.actualizar_estado_boton([])

    def actualizar_textbox_sabores(self, lista_sabores):
        self.lista_sabores.configure(state="normal")
        self.lista_sabores.delete("1.0", "end")
        self.lista_sabores.insert("end", "Sabores añadidos:\n")
        for sabor in lista_sabores:
            self.lista_sabores.insert("end", f"{sabor}\n")
        self.lista_sabores.configure(state="disabled")


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    vista = ProductoVista(app)
    app.mainloop()
