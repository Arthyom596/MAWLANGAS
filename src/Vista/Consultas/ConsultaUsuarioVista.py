import customtkinter as ctk
from tkinter import ttk
from src.DAO.UsuariosDAO import obtener_usuarios
class ConsultaUsuario:
    def __init__(self,parent,controlador_maestro):
        self.controlador_maestro=controlador_maestro
        self.frame=ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="#eabb46")

        for col in (0, 1, 2, 3):
            self.frame.columnconfigure(col, weight=1)

        for row in (0, 1, 2, 3, 4, 5):
            self.frame.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(self.frame, text="Consulta de Usuarios", font=("Arial", 30, "bold"), text_color="black")
        self.consulta.grid(column=2, row=0, sticky="w", padx=80, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"))
        style.configure("Treeview", font=("Arial", 12), rowheight=28)

        self.tree = ttk.Treeview(self.frame,
                                 columns=("ID", "Usuarios", "Contraseña", "Nombre", "Apellido Pat", "Apellido Mat", "Correo"),
                                 show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Usuarios", text="Usuarios")
        self.tree.heading("Contraseña", text="Contraseña")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido Pat", text="Apellido Pat")
        self.tree.heading("Apellido Mat", text="Apellido Mat")
        self.tree.heading("Correo", text="Correo")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Usuarios", width=100, anchor="center")
        self.tree.column("Contraseña", width=100, anchor="center")
        self.tree.column("Nombre", width=100, anchor="center")
        self.tree.column("Apellido Pat", width=100, anchor="center")
        self.tree.column("Apellido Mat", width=100, anchor="center")
        self.tree.column("Correo", width=150, anchor="center")

        self.tree.grid(row=1, column=0, columnspan=4, rowspan=5, padx=20, pady=20, sticky="nsew")

        self.cargar_usuarios()  # <--- Cargar datos al iniciar
        self.boton_regresar = ctk.CTkButton(self.frame, text="Regresar al Menú", font=("Arial", 16, "bold"),
                                            width=200, height=40, corner_radius=20, fg_color="red",
                                            command=self.controlador_maestro.mostrar_menu_consultas,
                                            hover_color="darkred")
        self.boton_regresar.grid(row=6, column=1, columnspan=2, pady=10, sticky="ew")

    def cargar_usuarios(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        usuarios = obtener_usuarios()
        for usuario in usuarios:
            valores_limpios = [str(dato) if dato is not None else "N/A" for dato in usuario]
            self.tree.insert("", "end", values=valores_limpios)

# Solo si ejecutas este archivo directamente
if __name__ == "__main__":
    app = ctk.CTk()
    vista = ConsultaUsuario(app)
    app.mainloop()
