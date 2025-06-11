import customtkinter as ctk
from src.DAO.SaboresDAO import obtener_sabores_con_nombre_producto, actualizar_sabor, obtener_nombre_sabor_por_id
from src.Modelo.Validaciones import validar_texto


class ModificarSaborVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.sabores = obtener_sabores_con_nombre_producto()
        self.id_sabor_actual = None

        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        self.frame.grid_columnconfigure((0, 3), weight=1)
        self.frame.grid_columnconfigure(1, weight=0)
        self.frame.grid_rowconfigure(4, weight=1)

        self.frame_superior = ctk.CTkFrame(self.frame, height=50, fg_color="#1c67f3", bg_color="#1c67f3")
        self.frame_superior.grid(row=0, column=0, sticky="new", columnspan=4, rowspan=1)

        self.frame_superior.grid_columnconfigure((0, 3), weight=1)
        self.frame_superior.grid_columnconfigure(1, weight=0)
        self.frame_superior.grid_rowconfigure(4, weight=1)

        self.label_titulo = ctk.CTkLabel(
            self.frame_superior,
            text="Modificar Sabor",text_color="white",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        self.label_titulo.grid(row=0, column=1, pady=(10, 20), sticky="ew")

        self.combo_sabor = ctk.CTkComboBox(
            self.frame,
            state="readonly",
            width=400,
            values=[f"{id_sabor} - {nombre_producto} - {nombre_sabor}" for id_sabor, nombre_producto, nombre_sabor in
                    self.sabores]
        )
        self.combo_sabor.grid(row=1, column=1, pady=(20, 10))
        self.combo_sabor.bind("<<ComboboxSelected>>", self.on_cambio_seleccion)

        # Botón Buscar
        self.boton_buscar = ctk.CTkButton(
            self.frame,
            text="Buscar",
            command=self.buscar_sabor,
            width=120,corner_radius=50,fg_color="#3abd0d",hover_color="#51ef1a",font=("Arial", 20,"bold"),
        )
        self.boton_buscar.grid(row=2, column=1, pady=(0, 20))

        self.label_resultado = ctk.CTkLabel(
            self.frame,
            text="",
            font=ctk.CTkFont(size=14)
        )
        self.label_resultado.grid(row=3, column=1, columnspan=2, pady=(5, 10), sticky="ew")

        self.frame_edicion = ctk.CTkScrollableFrame(
            self.frame,
            label_text="Editar Sabor"
        )
        self.frame_edicion.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        self.frame_edicion.grid_remove()

        self.label_producto_texto = ctk.CTkLabel(
            self.frame_edicion,
            text="Producto asociado:",
            anchor="w",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.label_producto_texto.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="w")

        self.label_producto = ctk.CTkLabel(
            self.frame_edicion,
            text="",
            anchor="w",
            font=ctk.CTkFont(size=14)
        )
        self.label_producto.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="w")

        # Campo editable para NombreSabor
        self.label_sabor_texto = ctk.CTkLabel(
            self.frame_edicion,
            text="Nombre del sabor:",
            anchor="w",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.label_sabor_texto.grid(row=1, column=0, padx=(10, 5), pady=(5, 10), sticky="w")

        self.entry_nombre_sabor = ctk.CTkEntry(
            self.frame_edicion,
            state="normal",
            width=300
        )
        self.entry_nombre_sabor.grid(row=1, column=1, padx=(5, 10), pady=(5, 10), sticky="w")

        self.boton_guardar = ctk.CTkButton(
            self.frame_edicion,
            text="Guardar cambios",
            command=self.guardar_cambios,
        )
        self.boton_guardar.grid(row=2, column=1, padx=10, pady=(20, 10), sticky="e")
        self.boton_guardar.configure(state="disabled")

        # Botón volver
        self.boton_volver = ctk.CTkButton(
            self.frame,
            text="Volver al menú",
            command=self.controlador_maestro.menu_modificar,
            width=150,fg_color="#c20f0c",hover_color="#f60d09",
        )
        self.boton_volver.grid(row=5, column=1, pady=(10, 20))

    def on_cambio_seleccion(self, _):
        self.label_resultado.configure(text="")
        self.boton_guardar.configure(state="disabled")
        self.frame_edicion.grid_remove()

    def buscar_sabor(self):
        seleccion = self.combo_sabor.get()
        if not seleccion:
            self.label_resultado.configure(text="Seleccione un sabor.")
            self.frame_edicion.grid_remove()
            return

        id_sabor = int(seleccion.split(" - ")[0])
        nombre_producto = seleccion.split(" - ")[1]
        nombre_sabor = obtener_nombre_sabor_por_id(id_sabor)

        if nombre_sabor:
            self.label_resultado.configure(text=f"Sabor encontrado: {nombre_sabor}")
            self.id_sabor_actual = id_sabor

            # Mostrar información en las etiquetas y el campo editable
            self.label_producto.configure(text=nombre_producto)
            self.entry_nombre_sabor.delete(0, "end")
            self.entry_nombre_sabor.insert(0, nombre_sabor)

            # Mostrar frame de edición
            self.frame_edicion.grid()
            self.boton_guardar.configure(state="normal")
        else:
            self.label_resultado.configure(text="Sabor no encontrado.")
            self.frame_edicion.grid_remove()

    def guardar_cambios(self):
        nuevo_nombre = self.entry_nombre_sabor.get()

        valido, msg = validar_texto(nuevo_nombre)
        if not valido:
            self.label_resultado.configure(text=f"Error: {msg}")
            return

        actualizar_sabor(
            self.id_sabor_actual,
            None,  # El IDProducto no cambia, se pasa como None
            nuevo_nombre
        )

        self.label_resultado.configure(text="Cambios guardados correctamente.")
        self.boton_guardar.configure(state="disabled")
