import customtkinter as ctk
from tkinter import ttk

class ConsultaUsuario:
    def __init__(self, root):
        self.app = root
        self.app.geometry("850x650")
        self.app.title("Consultar Usuarios")
        self.app.configure(fg_color="#eabb46")

        for col in (0, 1, 2, 3):
            app.columnconfigure(col, weight=1)

        for row in (0, 1, 2, 3, 4, 5):
            app.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(self.app,text="Consulta de Usuarios",font=("Arial",30,"bold"),text_color="black")
        self.consulta.grid(column=2,row=0,sticky="w",padx=80, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"))

        # --- Treeview ---
        self.tree = ttk.Treeview(self.app, columns=("ID", "Usuarios","Contraseña","Nombre","Apellido Pat","Apellido Mat","Correo"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Usuarios", text="Usuarios")
        self.tree.heading("Contraseña", text="Contraseña")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido Pat", text="Apellido Pat")
        self.tree.heading("Apellido Mat", text="Apellido Mat")
        self.tree.heading("Correo", text="Correo")

        # Opcional: ancho de columnas
        self.tree.column("ID", width=50)
        self.tree.column("Usuarios", width=100)
        self.tree.column("Contraseña", width=100)
        self.tree.column("Nombre", width=100)
        self.tree.column("Apellido Pat", width=100)
        self.tree.column("Apellido Mat", width=100)
        self.tree.column("Correo", width=100)

        self.tree.grid(row=1, column=0, columnspan=4, rowspan=5, padx=20, pady=20, sticky="nsew")

if __name__ == "__main__":
    app = ctk.CTk()
    vista = ConsultaUsuario(app)
    app.mainloop()