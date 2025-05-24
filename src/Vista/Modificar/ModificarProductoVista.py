import customtkinter as ctk
from src.DAO.ProductosDAO import obtener_productos_id_nombre, buscar_producto, actualizar_producto
from src.Modelo.Validaciones import validar_texto, validar_numero  # Importa tus validaciones aquí


class ModificarProductoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Modificar Producto")
        self.geometry("800x600")
        self.configure(padx=20, pady=20)

        self.label_titulo = ctk.CTkLabel(
            self,
            text="Modificar Producto",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.label_titulo.grid(row=0, column=0, columnspan=3, pady=(10, 20), sticky="w")

        # Usamos 3 columnas para centrar el combo y botón en la columna 1 (centro)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.productos = obtener_productos_id_nombre()
        self.combo_producto = ctk.CTkComboBox(
            self,
            state="readonly",
            width=400,
            values=[f"{id} - {nombre}" for id, nombre in self.productos]
        )
        self.combo_producto.grid(row=1, column=1, sticky="ew", pady=(0, 10))
        self.combo_producto.bind("<<ComboboxSelected>>", self.on_cambio_seleccion)

        self.boton_buscar = ctk.CTkButton(
            self,
            text="Buscar",
            command=self.buscar_producto,
            width=120
        )
        self.boton_buscar.grid(row=2, column=1, sticky="", pady=(0, 20))

        self.label_resultado = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=14))
        self.label_resultado.grid(row=3, column=0, columnspan=3, pady=(5, 10), sticky="w")

        self.frame_edicion = ctk.CTkScrollableFrame(self, label_text="Editar campos")
        self.frame_edicion.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
        self.frame_edicion.grid_remove()

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure((0, 2), weight=1)

        self.campos = {
            "Nombre": "",
            "PrecioCompra": "",
            "PrecioVenta": "",
        }

        self.checkboxes = {}
        self.entries = {}
        self.boton_guardar = None
        self.id_producto_actual = None

    def on_cambio_seleccion(self, event):
        if self.boton_guardar:
            self.boton_guardar.configure(state="disabled")
        self.label_resultado.configure(text="")

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
            self.construir_menu_edicion(producto)

            if self.boton_guardar:
                self.boton_guardar.configure(state="normal")
        else:
            self.label_resultado.configure(text="Producto no encontrado.")
            self.frame_edicion.grid_remove()

    def obtener_nombre_por_id(self, id_producto):
        for id_, nombre in self.productos:
            if id_ == id_producto:
                return nombre
        return None

    def construir_menu_edicion(self, datos_actuales):
        for widget in self.frame_edicion.winfo_children():
            widget.destroy()

        self.checkboxes.clear()
        self.entries.clear()

        for campo in self.campos:
            frame = ctk.CTkFrame(self.frame_edicion)
            frame.pack(fill="x", pady=5, padx=10)

            checkbox = ctk.CTkCheckBox(frame, text=campo, command=lambda c=campo: self.toggle_entry(c))
            checkbox.pack(side="left", padx=5)
            checkbox.select()
            self.checkboxes[campo] = checkbox

            entry = ctk.CTkEntry(frame)
            entry.pack(side="left", fill="x", expand=True, padx=5)
            entry.insert(0, datos_actuales.get(campo, ""))
            self.entries[campo] = entry

        self.boton_guardar = ctk.CTkButton(
            self.frame_edicion,
            text="Guardar cambios",
            command=self.guardar_cambios
        )
        self.boton_guardar.pack(pady=10)

        self.boton_guardar.configure(state="disabled")

        self.frame_edicion.grid()

    def toggle_entry(self, campo):
        if self.checkboxes[campo].get() == 1:
            self.entries[campo].configure(state="normal")
        else:
            self.entries[campo].delete(0, "end")
            self.entries[campo].configure(state="disabled")

    def guardar_cambios(self):
        cambios = {}
        errores = []

        for campo in self.campos:
            if self.checkboxes[campo].get() == 1:
                valor = self.entries[campo].get()

                if campo == "Nombre":
                    valido, msg = validar_texto(valor)
                elif campo in ["PrecioCompra", "PrecioVenta"]:
                    valido, msg = validar_numero(valor)
                else:
                    valido, msg = True, valor

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


if __name__ == "__main__":
    app = ModificarProductoApp()
    app.mainloop()
