# src/Vista/ProductoVista.py

import customtkinter as ctk
import tkinter as tk
from src.Controlador.ProductoControlador import ProductoControlador

"""
Esta clase representa la interfaz gráfica del usuario para el registro de productos.

Se encarga de construir la ventana principal, mostrando campos para ingresar el nombre del producto,
su precio de compra y venta, así como la opción de añadir sabores adicionales mediante una sección
dinámica (toggle) que puede activarse o desactivarse.

La vista también contiene botones que permiten al usuario agregar o eliminar sabores y guardar el
producto. A través del uso de etiquetas y cuadros de texto, muestra mensajes dinámicos para informar
al usuario sobre el estado del formulario.

Toda la interacción con los datos reales es delegada al controlador, manteniendo esta clase enfocada
únicamente en la presentación y la respuesta a eventos visuales del usuario.
"""


class ProductoVista:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x650")
        self.app.title("Añadir Producto")

        self.controlador = ProductoControlador(self) #Se crea una instancia del controlador

        #Se ajusta la venta con grid
        self.app.grid_columnconfigure((0, 1), weight=1)
        self.app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.titulo = ctk.CTkLabel(self.app, text="Registro de Producto",font=("Arial", 28, "bold"),
                                   text_color="white")
        self.titulo.grid(row=0, column=0, columnspan=2, pady=(30, 10))

        #Se crea un contenedor para la informacion del producto
        self.frame_producto = ctk.CTkFrame(self.app, corner_radius=20)
        self.frame_producto.grid(row=1, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
        self.frame_producto.grid_columnconfigure(1, weight=1)

        #Creacion de la etiqueta de producto y su entrada
        self.label_nombre = ctk.CTkLabel(self.frame_producto, text="Nombre del producto:",
                                         font=("Arial", 16))
        self.label_nombre.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. Malanga",
                                         font=("Arial", 14))
        self.entry_nombre.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")

        #Creacion de la etiqueta de precio_compra y su entrada
        self.label_precio_compra = ctk.CTkLabel(self.frame_producto, text="Precio de compra ($):",
                                                font=("Arial", 16))
        self.label_precio_compra.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_precio_compra = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 12",
                                                font=("Arial", 14))
        self.entry_precio_compra.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        # Creacion de la etiqueta de precio_venta y su entrada
        self.label_precio_venta = ctk.CTkLabel(self.frame_producto, text="Precio de venta ($):",
                                               font=("Arial", 16))
        self.label_precio_venta.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="w")
        self.entry_precio_venta = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 18",
                                               font=("Arial", 14))
        self.entry_precio_venta.grid(row=2, column=1, padx=20, pady=(10, 20), sticky="ew")

        # Creacion del Switch y lo dejamos "prendido" por defecto
        self.switch_sabores =ctk.CTkSwitch(self.app, text="Agregar sabores al producto?", onvalue=True, offvalue=False,
                                           font=("Arial",16), command=self.toggle_sabores, variable=tk.BooleanVar(value=True))

        self.switch_sabores.grid(row=2, column=0, columnspan=2, pady=(0, 10))

        self.titulo_sabores = ctk.CTkLabel(self.app, text="Sabores del Producto",
                                           font=("Arial", 24, "bold"), text_color="white")
        self.titulo_sabores.grid(row=3, column=0, columnspan=2, pady=(10, 5))

         #Se crea el frame dinamico de sabores
        self.frame_sabores = ctk.CTkFrame(self.app, corner_radius=20)
        self.frame_sabores.grid(row=4, column=0, columnspan=2, padx=40, pady=10, sticky="nsew")
        self.frame_sabores.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame_sabores.grid_rowconfigure(1, weight=1)

        #Accion para desbloquear el boton si encuentra algo escrito en la entrada de sabores
        self.sabor_var = tk.StringVar()
        self.sabor_var.trace_add("write", lambda *args: self.actualizar_estado_boton(self.controlador.sabores))

        #Se crea la entrada para el nombre del sabor
        self.entry_sabor = ctk.CTkEntry(self.frame_sabores, textvariable=self.sabor_var,
                                        placeholder_text="Ej. Takis", font=("Arial", 14))
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

        #Se crea la texbox con la lista de sabores
        self.lista_sabores = ctk.CTkTextbox(self.frame_sabores, height=120, font=("Arial", 14))
        self.lista_sabores.grid(row=1, column=0, columnspan=3, padx=20, pady=(0, 10), sticky="nsew")
        self.lista_sabores.insert("0.0", "Sabores añadidos:\n") #Se inicia en 0,0

        #Se crea una etiqueta para mostrar mensajes personalizados al usuario (Error,Exito)


        self.btn_guardar = ctk.CTkButton(
            self.app, text="Guardar Producto", font=("Arial", 16, "bold"),
            fg_color="green", hover_color="#45A049", #Verde y verde oscuro
            command=lambda: self.controlador.guardar_producto(
                self.entry_nombre.get(),
                self.entry_precio_compra.get(),
                self.entry_precio_venta.get(),
                self.switch_sabores.get()
            )
        )
        self.btn_guardar.grid(row=6, column=0, columnspan=2, pady=30, padx=100, sticky="ew")

        self.etiqueta_dinamica = ctk.CTkLabel(
            self.app,
            text="",
            font=("Arial", 14),
            text_color="white",
        )
        self.etiqueta_dinamica.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="ew")

        self.actualizar_estado_boton(self.controlador.sabores)

    #Define si se muestra el frame de sabores
    def toggle_sabores(self):
        if self.switch_sabores.get(): #Si esta encendido posiciona todos los grid
            self.titulo_sabores.grid()
            self.frame_sabores.grid()
        else: #Si esta en false remueve toto lo relacionado con el Frame
            self.titulo_sabores.grid_remove()
            self.frame_sabores.grid_remove()
            self.controlador.sabores.clear()
            self.actualizar_textbox_sabores([]) #Limpia la lista
            self.etiqueta_dinamica.configure(text="") #Regresa a su estado normal a la etiqueta dinamica
        self.actualizar_estado_boton(self.controlador.sabores)

    def actualizar_estado_boton(self, sabores=None):
        #Si se encuentra texto en el entry del sabor se trae y se limpia
        texto = self.sabor_var.get().strip()
        #Si hay texto prende los botones para manipular la lista si no los apaga
        self.btn_agregar_sabor.configure(state="normal" if texto else "disabled")
        self.btn_eliminar_sabor.configure(state="normal" if sabores else "disabled")
        #Si no encuentra sabores en la lista no permite guardar el producto
        if self.switch_sabores.get() and not sabores:
            self.btn_guardar.configure(state="disabled")
        else:
            self.btn_guardar.configure(state="normal")

    """""
    mostrar_mensaje es un metodo muy importante ya que cada error en cualquier parte de la validacion
    o error en las entradas etc,asi como cuando se procese un producto correctamente recibira el mensaje
    correspondiente y lo insertara en la etiqueta vacia "" de etiqueta_dinamica
    """
    def mostrar_mensaje(self, texto):
        self.etiqueta_dinamica.configure(text=texto)

    #Limpia la entrada del sabor
    def limpiar_entry_sabor(self):
        self.entry_sabor.delete(0, "end")

    #Restaura y limpia las entradas a sus valores por defecto del formulario
    def reiniciar_formulario(self):
        self.entry_nombre.delete(0, "end")
        self.entry_precio_compra.delete(0, "end")
        self.entry_precio_venta.delete(0, "end")
        self.actualizar_textbox_sabores([])
        self.etiqueta_dinamica.configure(text="")
        self.actualizar_estado_boton([])


    def actualizar_textbox_sabores(self, lista_sabores):

        self.lista_sabores.configure(state="normal") #Permite modificaciones en la texbox
        self.lista_sabores.delete("1.0", "end") #Limpia la texbox
        self.lista_sabores.insert("end", "Sabores añadidos:\n") #Inserta el titulo
        for sabor in lista_sabores: #Recorre la lista de sabores
            self.lista_sabores.insert("end", f"{sabor}\n") #Lo agrega como una nueva linea de texto
        self.lista_sabores.configure(state="disabled") #Apaga la texbpx


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    vista = ProductoVista(app)
    app.mainloop()
