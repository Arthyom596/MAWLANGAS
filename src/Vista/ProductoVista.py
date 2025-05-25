import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkFrame
from src.Controlador.ProductoControlador import ProductoControlador

class ProductoVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = CTkFrame(parent, width=800, height=600)
        self.frame.pack(fill="both", expand=False)
        self.frame.pack_propagate(False)

        self.controlador = ProductoControlador(self)

        self.frame.grid_columnconfigure((0, 1), weight=1)
        self.frame.grid_rowconfigure((1, 4), weight=1)

        # Título
        self.titulo = ctk.CTkLabel(self.frame, text="Registro de Producto", font=("Arial", 22, "bold"))
        self.titulo.grid(row=0, column=0, columnspan=2, pady=(10, 5))

        # Frame producto
        self.frame_producto = ctk.CTkFrame(self.frame, corner_radius=12)
        self.frame_producto.grid(row=1, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")
        self.frame_producto.grid_columnconfigure(1, weight=1)

        self.label_nombre = ctk.CTkLabel(self.frame_producto, text="Nombre del producto:", font=("Arial", 13))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=(12, 4), sticky="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. Malanga", font=("Arial", 13))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=(12, 4), sticky="ew")

        self.label_precio_compra = ctk.CTkLabel(self.frame_producto, text="Precio de compra ($):", font=("Arial", 13))
        self.label_precio_compra.grid(row=1, column=0, padx=10, pady=4, sticky="w")
        self.entry_precio_compra = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 12", font=("Arial", 13))
        self.entry_precio_compra.grid(row=1, column=1, padx=10, pady=4, sticky="ew")

        self.label_precio_venta = ctk.CTkLabel(self.frame_producto, text="Precio de venta ($):", font=("Arial", 13))
        self.label_precio_venta.grid(row=2, column=0, padx=10, pady=(4, 12), sticky="w")
        self.entry_precio_venta = ctk.CTkEntry(self.frame_producto, placeholder_text="Ej. 18", font=("Arial", 13))
        self.entry_precio_venta.grid(row=2, column=1, padx=10, pady=(4, 12), sticky="ew")

        # Switch Sabores
        self.switch_sabores = ctk.CTkSwitch(
            self.frame, text="Agregar sabores al producto?", onvalue=True, offvalue=False,
            font=("Arial", 13), command=self.toggle_sabores, variable=tk.BooleanVar(value=True)
        )
        self.switch_sabores.grid(row=2, column=0, columnspan=2, pady=4)

        # Título sabores
        self.titulo_sabores = ctk.CTkLabel(self.frame, text="Sabores del Producto", font=("Arial", 18, "bold"))
        self.titulo_sabores.grid(row=3, column=0, columnspan=2, pady=(4, 0))

        # Frame sabores
        self.frame_sabores = ctk.CTkFrame(self.frame, corner_radius=12)
        self.frame_sabores.grid(row=4, column=0, columnspan=2, padx=15, pady=5, sticky="nsew")
        self.frame_sabores.grid_columnconfigure((0, 1, 2), weight=1)

        self.sabor_var = tk.StringVar()
        self.sabor_var.trace_add("write", lambda *args: self.actualizar_estado_boton(self.controlador.sabores))

        self.entry_sabor = ctk.CTkEntry(self.frame_sabores, textvariable=self.sabor_var, placeholder_text="Ej. Takis", font=("Arial", 12))
        self.entry_sabor.grid(row=0, column=0, padx=5, pady=8, sticky="ew")

        self.btn_agregar_sabor = ctk.CTkButton(self.frame_sabores, text="Añadir", font=("Arial", 12),
                                               command=lambda: self.controlador.agregar_sabor(self.entry_sabor.get().strip()))
        self.btn_agregar_sabor.grid(row=0, column=1, padx=5, pady=8)

        self.btn_eliminar_sabor = ctk.CTkButton(self.frame_sabores, text="Eliminar último", font=("Arial", 12),
                                                fg_color="#D32F2F", hover_color="#B71C1C", command=self.controlador.eliminar_sabor)
        self.btn_eliminar_sabor.grid(row=0, column=2, padx=5, pady=8)

        self.lista_sabores = ctk.CTkTextbox(self.frame_sabores, height=80, font=("Arial", 12))
        self.lista_sabores.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 8), sticky="nsew")
        self.lista_sabores.insert("0.0", "Sabores añadidos:\n")

        # Mensaje inferior
        self.etiqueta_dinamica = ctk.CTkLabel(self.frame, text="", font=("Arial", 12))
        self.etiqueta_dinamica.grid(row=5, column=0, columnspan=2, padx=10, pady=4, sticky="ew")

        # Botones finales
        self.frame_botones = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.frame_botones.grid(row=6, column=0, columnspan=2, pady=(6, 10), padx=40, sticky="ew")
        self.frame_botones.grid_columnconfigure((0, 1), weight=1)

        self.btn_guardar = ctk.CTkButton(self.frame_botones, text="Guardar Producto", font=("Arial", 13, "bold"),
                                         fg_color="green", hover_color="#45A049",
                                         command=lambda: self.controlador.guardar_producto(
                                             self.entry_nombre.get(),
                                             self.entry_precio_compra.get(),
                                             self.entry_precio_venta.get(),
                                             self.switch_sabores.get()
                                         ))
        self.btn_guardar.grid(row=0, column=0, padx=8, sticky="ew")

        self.btn_regresar = ctk.CTkButton(self.frame_botones, text="Cancelar", font=("Arial", 13, "bold"),
                                          fg_color="#D32F2F", hover_color="#B71C1C",
                                          command=self.controlador_maestro.mostrar_menu_principal)
        self.btn_regresar.grid(row=0, column=1, padx=8, sticky="ew")

        self.actualizar_estado_boton(self.controlador.sabores)

    def toggle_sabores(self):
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
        self.btn_guardar.configure(state="normal" if not self.switch_sabores.get() or sabores else "disabled")

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
            self.lista_sabores.insert("end", f"- {sabor}\n")
