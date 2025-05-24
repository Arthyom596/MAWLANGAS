import customtkinter as ctk
from tkinter import messagebox
from src.DAO.UsuariosDAO import obtener_usuarios, buscar_usuario, eliminar_usuario

class EliminarUsuarioVista:

    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True, padx=40, pady=40)

        for col in range(3):
            self.frame.columnconfigure(col, weight=1)
        for row in range(8):
            self.frame.rowconfigure(row, weight=1)

        self.id_por_usuario = {}
        self.usuario_actual = None

        self.crear_interfaz()
        self.actualizar_combobox()

    def crear_interfaz(self):
        # Título
        self.label_titulo = ctk.CTkLabel(
            self.frame,
            text="Eliminar Usuario",
            font=ctk.CTkFont(size=28, weight="bold"),
            anchor="center"
        )
        self.label_titulo.grid(row=0, column=0, columnspan=3, pady=(10, 30))

        # ComboBox para seleccionar usuario
        self.combo_usuarios = ctk.CTkComboBox(
            self.frame,
            values=[],
            width=350,
            state="readonly",
            font=ctk.CTkFont(size=15)
        )
        self.combo_usuarios.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Botón buscar
        self.boton_buscar = ctk.CTkButton(
            self.frame,
            text="Buscar",
            width=130,
            height=35,
            font=ctk.CTkFont(size=14),
            command=self.buscar_usuario
        )
        self.boton_buscar.grid(row=1, column=2, padx=10, pady=10)

        # Labels para mostrar datos del usuario
        self.labels_datos = {}
        campos = ["IDUsuario", "Usuario", "Nombre Completo", "Correo"]
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

        # Botón eliminar usuario en columna 1
        self.boton_eliminar = ctk.CTkButton(
            self.frame,
            text="Eliminar Usuario",
            fg_color="red",
            hover_color="#cc0000",
            width=220,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.eliminar_usuario
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
        usuarios = obtener_usuarios()
        # Diccionario: nombre_usuario -> id_usuario
        self.id_por_usuario = {usuario[1]: usuario[0] for usuario in usuarios}
        nombres = [usuario[1] for usuario in usuarios]
        self.combo_usuarios.configure(values=nombres)
        self.combo_usuarios.set("")

    def buscar_usuario(self):
        nombre_usuario = self.combo_usuarios.get()
        if nombre_usuario not in self.id_por_usuario:
            self.mostrar_mensaje("Usuario no encontrado.", error=True)
            self.boton_eliminar.grid_remove()
            self.limpiar_datos()
            return

        datos = buscar_usuario(nombre_usuario)
        if datos:
            self.usuario_actual = datos
            self.mostrar_datos_usuario(datos)
        else:
            self.mostrar_mensaje("Usuario no encontrado.", error=True)
            self.boton_eliminar.grid_remove()
            self.limpiar_datos()

    def mostrar_datos_usuario(self, usuario):
        # usuario = (IDUsuario, Usuario, Contrasena, Nombre, ApellidoPaterno, ApellidoMaterno, Correo)
        nombre_completo = f"{usuario[3]} {usuario[4]} {usuario[5] or ''}".strip()
        self.labels_datos["IDUsuario"].configure(text=f"IDUsuario: {usuario[0]}")
        self.labels_datos["Usuario"].configure(text=f"Usuario: {usuario[1]}")
        self.labels_datos["Nombre Completo"].configure(text=f"Nombre Completo: {nombre_completo}")
        self.labels_datos["Correo"].configure(text=f"Correo: {usuario[6]}")
        self.boton_eliminar.grid()

    def eliminar_usuario(self):
        if not self.usuario_actual:
            return
        eliminar_usuario(self.usuario_actual[0])
        self.mostrar_mensaje("Usuario eliminado exitosamente.")
        self.usuario_actual = None
        self.actualizar_combobox()
        self.limpiar_datos()
        self.boton_eliminar.grid_remove()

    def limpiar_datos(self):
        for label in self.labels_datos.values():
            label.configure(text="")

    def mostrar_mensaje(self, mensaje, error=False):
        titulo = "Error" if error else "Éxito"
        messagebox.showinfo(titulo, mensaje)
