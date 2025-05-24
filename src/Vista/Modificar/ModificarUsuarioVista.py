import customtkinter as ctk
from src.DAO.UsuariosDAO import obtener_usuarios, buscar_usuario, actualizar_usuario
from src.Modelo.Registro import validar_usuario, validar_contraseña, validar_nombre, validar_correo


class ModificarUsuarioVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.usuarios = obtener_usuarios()
        self.campos = {
            "Usuario": "",
            "Contrasena": "",
            "Nombre": "",
            "ApPat": "",  # Cambiado de ApellidoPaterno
            "ApMat": "",  # Cambiado de ApellidoMaterno
            "Correo": "",
        }
        self.checkboxes = {}
        self.entries = {}
        self.usuario_actual = None

        # Frame principal
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        self.frame.grid_columnconfigure((0, 3), weight=1)
        self.frame.grid_columnconfigure(1, weight=0)
        self.frame.grid_rowconfigure(4, weight=1)

        # Título
        self.label_titulo = ctk.CTkLabel(
            self.frame,
            text="Modificar Usuario",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.label_titulo.grid(row=0, column=1, pady=(10, 20), sticky="ew")

        # ComboBox de usuarios
        self.combo_usuario = ctk.CTkComboBox(
            self.frame,
            state="readonly",
            width=400,
            values=[f"{id} - {datos[1]}" for id, datos in enumerate(self.usuarios)]
        )
        self.combo_usuario.grid(row=1, column=1, pady=(0, 10))
        self.combo_usuario.bind("<<ComboboxSelected>>", self.on_cambio_seleccion)

        # Botón Buscar
        self.boton_buscar = ctk.CTkButton(
            self.frame,
            text="Buscar",
            command=self.buscar_usuario,
            width=120
        )
        self.boton_buscar.grid(row=2, column=1, pady=(0, 20))

        # Label de resultados
        self.label_resultado = ctk.CTkLabel(
            self.frame,
            text="",
            font=ctk.CTkFont(size=14)
        )
        self.label_resultado.grid(row=3, column=1, columnspan=2, pady=(5, 10), sticky="ew")

        # Frame de edición (creado pero inicialmente oculto)
        self.frame_edicion = ctk.CTkScrollableFrame(
            self.frame,
            label_text="Editar campos"
        )
        self.frame_edicion.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
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
            command=self.guardar_cambios,
        )
        self.boton_guardar.pack(pady=10)
        self.boton_guardar.configure(state="disabled")

        # Botón volver
        self.boton_volver = ctk.CTkButton(
            self.frame,
            text="Volver al menú",
            command=self.controlador_maestro.menu_modificar,
            width=150
        )
        self.boton_volver.grid(row=5, column=1, pady=(10, 20))

    def on_cambio_seleccion(self, _):
        self.label_resultado.configure(text="")
        self.boton_guardar.configure(state="disabled")
        self.frame_edicion.grid_remove()

    def buscar_usuario(self):
        seleccion = self.combo_usuario.get()
        if not seleccion:
            self.label_resultado.configure(text="Seleccione un usuario.")
            self.frame_edicion.grid_remove()
            return

        usuario_id = int(seleccion.split(" - ")[0])
        datos = buscar_usuario(self.obtener_nombre_por_id(usuario_id))

        if datos:
            self.label_resultado.configure(text=f"Usuario encontrado: {datos[1]}")
            usuario = {
                "Usuario": datos[1],
                "Contrasena": datos[2],
                "Nombre": datos[3],
                "ApPat": datos[4],
                "ApMat": datos[5],
                "Correo": datos[6],
            }
            self.usuario_actual = usuario_id
            self._llenar_campos(usuario)
            self.frame_edicion.grid()
            self.boton_guardar.configure(state="normal")
        else:
            self.label_resultado.configure(text="Usuario no encontrado.")
            self.frame_edicion.grid_remove()

    def _llenar_campos(self, usuario):
        for campo, valor in usuario.items():
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

                if campo in ["Usuario", "Nombre", "ApPat", "ApMat"]:
                    valido, msg = validar_nombre(valor)
                elif campo == "Contrasena":
                    valido, msg = validar_contraseña(valor)
                elif campo == "Correo":
                    valido, msg = validar_correo(valor)
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
            actualizar_usuario(
                self.usuario_actual,
                cambios.get("Usuario", self.entries["Usuario"].get()),
                cambios.get("Contrasena", self.entries["Contrasena"].get()),
                cambios.get("Nombre", self.entries["Nombre"].get()),
                cambios.get("ApPat", self.entries["ApPat"].get()),
                cambios.get("ApMat", self.entries["ApMat"].get()),
                cambios.get("Correo", self.entries["Correo"].get())
            )
            self.label_resultado.configure(text="Cambios guardados correctamente.")
            self.boton_guardar.configure(state="disabled")
        else:
            self.label_resultado.configure(text="No hay cambios para guardar.")

    def obtener_nombre_por_id(self, usuario_id):
        for id_, datos in enumerate(self.usuarios):
            if id_ == usuario_id:
                return datos[1]
        return None
