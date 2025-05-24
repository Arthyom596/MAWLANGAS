import customtkinter as ctk
from tkinter import ttk
from src.DAO.SaboresDAO import obtener_sabores  # Ajusta según tu ruta real

class ConsultaSabor:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro

        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="#69d3a8")

        for col in range(4):
            self.frame.columnconfigure(col, weight=1)
        for row in range(7):
            self.frame.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(self.frame, text="Consulta de Sabores", font=("Arial", 30, "bold"),
                                     text_color="black")
        self.consulta.grid(column=2, row=0, sticky="w", padx=80, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"), anchor="center")
        style.configure("Treeview", font=("Arial", 12), rowheight=28)

        self.tree = ttk.Treeview(self.frame, columns=("IDSabor", "IDProducto", "NombreSabor"), show="headings")

        self.tree.heading("IDSabor", text="ID Sabor")
        self.tree.heading("IDProducto", text="ID Producto")
        self.tree.heading("NombreSabor", text="Nombre del Sabor")

        self.tree.column("IDSabor", width=100, anchor="center")
        self.tree.column("IDProducto", width=200, anchor="center")
        self.tree.column("NombreSabor", width=150, anchor="center")

        self.tree.grid(row=1, column=0, columnspan=4, rowspan=4, padx=20, pady=20, sticky="nsew")

        self.boton_regresar = ctk.CTkButton(self.frame, text="Regresar al Menú", font=("Arial", 16, "bold"),
                                            width=200, height=40, corner_radius=20, fg_color="red",
                                            command=self.controlador_maestro.mostrar_menu_consultas,
                                            hover_color="darkred")
        self.boton_regresar.grid(row=6, column=1, columnspan=2, pady=10, sticky="ew")

        self.cargar_sabores()

    def cargar_sabores(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        sabores = obtener_sabores()
        for sabor in sabores:
            valores_limpios = [str(dato) if dato is not None else "Sin sabor" for dato in sabor]
            self.tree.insert("", "end", values=valores_limpios)

