import customtkinter as ctk
from tkinter import ttk

from customtkinter import CTkFrame

from src.DAO.InventarioDAO import obtener_inventario_completo  # Ajusta la ruta si es necesario

class ConsultaInventarioVista:
    def __init__(self, parent,controlador_maestro):
        self.controlador_maestro = controlador_maestro

        self.frame =CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="#7c82e8")

        for col in range(4):
            self.frame.columnconfigure(col, weight=1)
        for row in range(7):
            self.frame.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(self.frame, text="Consulta de Inventario", font=("Arial", 30, "bold"), text_color="black")
        self.consulta.grid(column=2, row=0, sticky="w", padx=80, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"), anchor="center")
        style.configure("Treeview", font=("Arial", 12), rowheight=28)

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Producto", "Sabor", "Cantidad", "Fecha"), show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("Sabor", text="Sabor")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Fecha", text="Fecha")

        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Producto", width=200, anchor="center")
        self.tree.column("Sabor", width=140, anchor="center")
        self.tree.column("Cantidad", width=100, anchor="center")
        self.tree.column("Fecha", width=160, anchor="center")

        self.tree.grid(row=1, column=0, columnspan=4, rowspan=4, padx=20, pady=20, sticky="nsew")

        self.boton_regresar = ctk.CTkButton(self.frame, text="Regresar al Menu", font=("Arial", 16, "bold"), width=200,
                                            height=40, corner_radius=20, fg_color="RED",
                                            command=self.controlador_maestro.mostrar_menu_consultas,
                                            hover_color="darkred"
                                            )
        self.boton_regresar.grid(row=6, column=1, columnspan=2, pady=10, sticky="ew")

        self.cargar_datos()

    def cargar_datos(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        inventario = obtener_inventario_completo()
        for fila in inventario:
            valores_limpios = [str(dato) if dato is not None else "N/A" for dato in fila]
            self.tree.insert("", "end", values=valores_limpios)

