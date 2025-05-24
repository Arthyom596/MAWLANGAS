import customtkinter as ctk
from tkinter import messagebox
from src.DAO.SaboresDAO import obtener_sabores_con_nombre_producto, eliminar_sabor


class EliminarSaborVista:

    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True, padx=40, pady=40)

        for col in range(3):
            self.frame.columnconfigure(col, weight=1)
        for row in range(7):
            self.frame.rowconfigure(row, weight=1)

        self.id_por_sabor = {}
        self.sabor_actual = None

        self.crear_interfaz()
        self.actualizar_combobox()

    def crear_interfaz(self):
        # Título
        self.label_titulo = ctk.CTkLabel(
            self.frame,
            text="Eliminar Sabor",
            font=ctk.CTkFont(size=28, weight="bold"),
            anchor="center"
        )
        self.label_titulo.grid(row=0, column=0, columnspan=3, pady=(10, 30))

        # ComboBox para seleccionar sabor
        self.combo_sabores = ctk.CTkComboBox(
            self.frame,
            values=[],
            width=350,
            state="readonly",
            font=ctk.CTkFont(size=15)
        )
        self.combo_sabores.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Botón buscar
        self.boton_buscar = ctk.CTkButton(
            self.frame,
            text="Buscar",
            width=130,
            height=35,
            font=ctk.CTkFont(size=14),
            command=self.buscar_sabor
        )
        self.boton_buscar.grid(row=1, column=2, padx=10, pady=10)

        # Labels para mostrar datos del sabor
        self.labels_datos = {}
        campos = ["IDSabor", "Nombre del Sabor"]
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

        # Botón eliminar sabor
        self.boton_eliminar = ctk.CTkButton(
            self.frame,
            text="Eliminar Sabor",
            fg_color="red",
            hover_color="#cc0000",
            width=220,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.eliminar_sabor
        )
        self.boton_eliminar.grid(row=5, column=1, pady=(30, 10))
        self.boton_eliminar.grid_remove()  # oculto hasta que se seleccione un sabor

        # Botón regresar al menú
        self.boton_regresar = ctk.CTkButton(
            self.frame,
            text="Regresar al menú",
            font=ctk.CTkFont(size=16, weight="bold"),
            width=220,
            height=45,
            corner_radius=20,
            fg_color="green",
            hover_color="#006400",
            command=self.controlador_maestro.menu_eliminar
        )
        self.boton_regresar.grid(row=6, column=1, pady=(0, 10))

    def actualizar_combobox(self):
        sabores = obtener_sabores_con_nombre_producto()  # retorna (IDSabor, NombreProducto, NombreSabor)
        self.id_por_sabor = {}

        for sabor in sabores:
            id_sabor, nombre_producto, nombre_sabor = sabor
            nombre_sabor = nombre_sabor if nombre_sabor else "Sin sabor"
            clave = f"{nombre_producto} - {nombre_sabor} (ID:{id_sabor})"
            self.id_por_sabor[clave] = id_sabor

        self.combo_sabores.configure(values=list(self.id_por_sabor.keys()))
        self.combo_sabores.set("")


    def buscar_sabor(self):
        seleccion = self.combo_sabores.get()
        if seleccion not in self.id_por_sabor:
            self.mostrar_mensaje("Sabor no encontrado.", error=True)
            self.boton_eliminar.grid_remove()
            self.limpiar_datos()
            return

        id_sabor = self.id_por_sabor[seleccion]
        sabores = obtener_sabores_con_nombre_producto()
        sabor = next((s for s in sabores if s[0] == id_sabor), None)

        if sabor:
            self.sabor_actual = sabor
            self.mostrar_datos_sabor(sabor)
        else:
            self.mostrar_mensaje("Sabor no encontrado.", error=True)
            self.boton_eliminar.grid_remove()
            self.limpiar_datos()


    def mostrar_datos_sabor(self, sabor):
        # sabor = (IDSabor, IDProducto, NombreSabor)
        nombre = sabor[2] if sabor[2] else "Sin sabor"
        self.labels_datos["IDSabor"].configure(text=f"IDSabor: {sabor[0]}")
        self.labels_datos["Nombre del Sabor"].configure(text=f"Nombre del Sabor: {nombre}")
        self.boton_eliminar.grid()

    def eliminar_sabor(self):
        if not self.sabor_actual:
            return
        eliminar_sabor(self.sabor_actual[0])
        self.mostrar_mensaje("Sabor eliminado exitosamente.")
        self.sabor_actual = None
        self.actualizar_combobox()
        self.limpiar_datos()
        self.boton_eliminar.grid_remove()

    def limpiar_datos(self):
        for label in self.labels_datos.values():
            label.configure(text="")

    def mostrar_mensaje(self, mensaje, error=False):
        titulo = "Error" if error else "Éxito"
        messagebox.showinfo(titulo, mensaje)
