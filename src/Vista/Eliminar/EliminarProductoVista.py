import customtkinter as ctk
from tkinter import messagebox
from src.DAO.ProductosDAO import obtener_productos_id_nombre, buscar_producto, eliminar_producto

class EliminarProductoVista:

    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True, padx=40, pady=40)

        for col in range(3):
            self.frame.columnconfigure(col, weight=1)
        for row in range(8):
            self.frame.rowconfigure(row, weight=1)

        self.id_por_nombre = {}
        self.producto_actual = None

        self.crear_interfaz()
        self.actualizar_combobox()

    def crear_interfaz(self):
        # Título
        self.label_titulo = ctk.CTkLabel(
            self.frame,
            text="Eliminar Producto",
            font=ctk.CTkFont(size=28, weight="bold"),
            anchor="center"
        )
        self.label_titulo.grid(row=0, column=0, columnspan=3, pady=(10, 30))

        # ComboBox para seleccionar producto
        self.combo_productos = ctk.CTkComboBox(
            self.frame,
            values=[],
            width=350,
            state="readonly",
            font=ctk.CTkFont(size=15)
        )
        self.combo_productos.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Botón buscar
        self.boton_buscar = ctk.CTkButton(
            self.frame,
            text="Buscar",
            width=130,
            height=35,
            font=ctk.CTkFont(size=14),
            command=self.buscar_producto
        )
        self.boton_buscar.grid(row=1, column=2, padx=10, pady=10)

        # Labels para mostrar datos del producto
        self.labels_datos = {}
        campos = ["ID", "Nombre", "Precio Compra", "Precio Venta"]
        for i, campo in enumerate(campos, start=2):
            label = ctk.CTkLabel(
                self.frame,
                text=f"{campo}: ",
                anchor="w",
                font=ctk.CTkFont(size=17),
                width=400
            )
            label.grid(row=i, column=0, columnspan=3, padx=20, pady=8, sticky="w")
            self.labels_datos[campo] = label

        # Botón eliminar producto en columna 1
        self.boton_eliminar = ctk.CTkButton(
            self.frame,
            text="Eliminar Producto",
            fg_color="red",
            hover_color="#cc0000",
            width=220,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.eliminar_producto
        )
        self.boton_eliminar.grid(row=6, column=1, pady=(30, 10))
        self.boton_eliminar.grid_remove()  # Oculto inicialmente

        # Botón regresar al menú debajo del botón eliminar, en misma columna y mismo tamaño
        self.boton_regresar = ctk.CTkButton(
            self.frame,
            text="Regresar al menú",
            font=ctk.CTkFont(size=16, weight="bold"),
            width=220,
            height=45,
            corner_radius=20,
            fg_color="green",
            hover_color="#006400",  # verde oscuro
            command=self.controlador_maestro.menu_eliminar
        )
        self.boton_regresar.grid(row=7, column=1, pady=(0, 10))

    def actualizar_combobox(self):
        productos = obtener_productos_id_nombre()
        self.id_por_nombre = {nombre: id_ for id_, nombre in productos}
        nombres = [nombre for _, nombre in productos]
        self.combo_productos.configure(values=nombres)
        self.combo_productos.set("")

    def buscar_producto(self):
        nombre = self.combo_productos.get()
        if nombre not in self.id_por_nombre:
            self.mostrar_mensaje("Producto no encontrado.", error=True)
            self.boton_eliminar.grid_remove()
            self.limpiar_datos()
            return

        datos = buscar_producto(nombre)
        if datos:
            self.producto_actual = datos
            self.mostrar_datos_producto(datos)
        else:
            self.mostrar_mensaje("Producto no encontrado.", error=True)
            self.boton_eliminar.grid_remove()
            self.limpiar_datos()

    def mostrar_datos_producto(self, producto):
        self.labels_datos["ID"].configure(text=f"ID: {producto[0]}")
        self.labels_datos["Nombre"].configure(text=f"Nombre: {producto[1]}")
        self.labels_datos["Precio Compra"].configure(text=f"Precio Compra: ${producto[2]:.2f}")
        self.labels_datos["Precio Venta"].configure(text=f"Precio Venta: ${producto[3]:.2f}")
        self.boton_eliminar.grid()

    def eliminar_producto(self):
        if not self.producto_actual:
            return
        eliminar_producto(self.producto_actual[0])
        self.mostrar_mensaje("Producto eliminado exitosamente.")
        self.producto_actual = None
        self.actualizar_combobox()
        self.limpiar_datos()
        self.boton_eliminar.grid_remove()

    def limpiar_datos(self):
        for label in self.labels_datos.values():
            label.configure(text="")

    def mostrar_mensaje(self, mensaje, error=False):
        titulo = "Error" if error else "Éxito"
        messagebox.showinfo(titulo, mensaje)
