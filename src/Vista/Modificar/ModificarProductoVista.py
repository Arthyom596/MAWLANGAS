import customtkinter as ctk
from src.DAO.ProductosDAO import obtener_productos_id_nombre, buscar_producto, actualizar_producto
from src.Modelo.Validaciones import validar_texto, validar_numero


class ModificarProductoVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.productos = obtener_productos_id_nombre()
        self.campos = {
            "Nombre": "",
            "PrecioCompra": "",
            "PrecioVenta": "",
        }
        self.checkboxes = {}
        self.entries = {}
        self.id_producto_actual = None

        # Frame principal
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="white")

        self.frame_superior = ctk.CTkFrame(self.frame, height=50, fg_color="#1c67f3", bg_color="#1c67f3")
        self.frame_superior.grid(row=0, column=0, sticky="new", columnspan=4,rowspan=1)

        self.frame.grid_columnconfigure((0, 3), weight=1)
        self.frame.grid_columnconfigure(1, weight=0)
        self.frame.grid_rowconfigure(4, weight=1)

        self.frame_superior.grid_columnconfigure((0, 3), weight=1)
        self.frame_superior.grid_columnconfigure(1, weight=1)
        self.frame_superior.grid_rowconfigure(4, weight=1)

        # Título
        self.label_titulo = ctk.CTkLabel(
            self.frame_superior,
            text="Modificar Producto",
            font=ctk.CTkFont(size=30, weight="bold"),text_color="white"
        )
        self.label_titulo.grid(row=1, column=1, pady=(10, 20), sticky="ew")

        # ComboBox de productos
        self.combo_producto = ctk.CTkComboBox(
            self.frame,
            state="readonly",
            width=400,
            values=[f"{id} - {nombre}" for id, nombre in self.productos]
        )
        self.combo_producto.grid(row=2, column=1, pady=(50, 10))
        self.combo_producto.bind("<<ComboboxSelected>>", self.on_cambio_seleccion)

        # Botón Buscar
        self.boton_buscar = ctk.CTkButton(
            self.frame,
            text="Buscar",
            command=self.buscar_producto,
            width=120,font=("Arial", 20, "bold"),fg_color="#17bd15",hover_color="#07eb05",corner_radius=50,
        )
        self.boton_buscar.grid(row=3, column=1, pady=(0, 20))

        # Label de resultados
        self.label_resultado = ctk.CTkLabel(
            self.frame,
            text="",
            font=ctk.CTkFont(size=14)
        )
        self.label_resultado.grid(row=4, column=1, columnspan=2, pady=(5, 10), sticky="ew")

        # Frame de edición (creado pero inicialmente oculto)
        self.frame_edicion = ctk.CTkScrollableFrame(
            self.frame,
            label_text="Editar campos"
        )
        self.frame_edicion.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.frame_edicion.grid_remove()

        # Entradas y checkboxes para campos editables
        for campo in self.campos:
            fila = ctk.CTkFrame(self.frame_edicion)
            fila.pack(fill="x", pady=5, padx=10)

            checkbox = ctk.CTkCheckBox(fila, text=campo, command=lambda c=campo: self.toggle_entry(c))
            checkbox.pack(side="left", padx=5)
            checkbox.deselect()
            self.checkboxes[campo] = checkbox

            entry = ctk.CTkEntry(fila, state="disabled")
            entry.pack(side="left", fill="x", expand=True, padx=5)
            self.entries[campo] = entry

        # Botón guardar cambios (inicialmente deshabilitado)
        self.boton_guardar = ctk.CTkButton(
            self.frame_edicion,
            text="Guardar cambios",
            command=self.guardar_cambios, fg_color="#17bd15",hover_color="#07eb05",font=("Arial", 20, "bold")
        )
        self.boton_guardar.pack(pady=10,padx=50)
        self.boton_guardar.configure(state="disabled")
        self.boton_volver = ctk.CTkButton(
            self.frame,
            text="Volver al menu",
            command=self.controlador_maestro.menu_modificar,font=("Arial", 20, "bold"),corner_radius=50,hover_color="#fc0303",fg_color="#b80404",
            width=150
        )
        self.boton_volver.grid(row=7, column=1, pady=(10, 20))

    def on_cambio_seleccion(self, _):
        self.label_resultado.configure(text="")
        self.boton_guardar.configure(state="disabled")
        self.frame_edicion.grid_remove()

    def buscar_producto(self):
        seleccion = self.combo_producto.get()
        if not seleccion:
            self.label_resultado.configure(text="Seleccione un producto.")
            self.frame_edicion.grid_remove()
            return

        id_producto = int(seleccion.split(" - ")[0])
        datos = buscar_producto(self.obtener_nombre_por_id(id_producto))

        if datos:
            self.label_resultado.configure(text=f"Producto encontrado: {datos[1]}")
            producto = {
                "Nombre": datos[1],
                "PrecioCompra": str(datos[2]),
                "PrecioVenta": str(datos[3])
            }
            self.id_producto_actual = id_producto
            self._llenar_campos(producto)
            self.frame_edicion.grid()
            self.boton_guardar.configure(state="normal")
        else:
            self.label_resultado.configure(text="Producto no encontrado.")
            self.frame_edicion.grid_remove()

    def _llenar_campos(self, producto):
        for campo, valor in producto.items():
            entry = self.entries[campo]
            checkbox = self.checkboxes[campo]
            checkbox.select()
            entry.configure(state="normal")
            entry.delete(0, "end")
            entry.insert(0, valor)

    def toggle_entry(self, campo):
        entry = self.entries[campo]
        if self.checkboxes[campo].get() == 1:
            entry.configure(state="normal")
        else:
            entry.delete(0, "end")
            entry.configure(state="disabled")

    def guardar_cambios(self):
        cambios = {}
        errores = []

        for campo in self.campos:
            if self.checkboxes[campo].get() == 1:
                valor = self.entries[campo].get()

                if campo == "Nombre":
                    valido, msg = validar_texto(valor)
                else:
                    valido, msg = validar_numero(valor)

                if not valido:
                    errores.append(f"{campo}: {msg}")
                else:
                    cambios[campo] = msg

        if errores:
            self.label_resultado.configure(text="Errores:\n" + "\n".join(errores))
            return

        if cambios:
            actualizar_producto(
                self.id_producto_actual,
                cambios.get("Nombre", self.entries["Nombre"].get()),
                float(cambios.get("PrecioCompra", self.entries["PrecioCompra"].get())),
                float(cambios.get("PrecioVenta", self.entries["PrecioVenta"].get()))
            )
            self.label_resultado.configure(text="Cambios guardados correctamente.")
            self.boton_guardar.configure(state="disabled")
        else:
            self.label_resultado.configure(text="No hay cambios para guardar.")

    def obtener_nombre_por_id(self, id_producto):
        for id_, nombre in self.productos:
            if id_ == id_producto:
                return nombre
        return None
