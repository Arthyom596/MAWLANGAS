import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from src.DAO.ProductosDAO import obtener_productos_consulta


class ConsultaProducto:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro

        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="#bec752")

        for col in range(4):
            self.frame.columnconfigure(col, weight=1)
        for row in range(7):
            self.frame.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(self.frame, text="Consulta de Productos", font=("Arial", 30, "bold"),
                                     text_color="black")
        self.consulta.grid(column=2, row=0, sticky="w", padx=80, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"), anchor="center")
        style.configure("Treeview", font=("Arial", 12), rowheight=28)

        self.tree = ttk.Treeview(self.frame, columns=("ID", "Producto", "P. Compra", "P. Venta"), show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("P. Compra", text="P. Compra")
        self.tree.heading("P. Venta", text="P. Venta")

        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Producto", width=200, anchor="center")
        self.tree.column("P. Compra", width=100, anchor="center")
        self.tree.column("P. Venta", width=100, anchor="center")

        self.tree.grid(row=1, column=0, columnspan=4, rowspan=4, padx=20, pady=20, sticky="nsew")

        self.boton_regresar = ctk.CTkButton(self.frame, text="Regresar al Menú", font=("Arial", 16, "bold"),
                                            width=200, height=40, corner_radius=20, fg_color="red",
                                            command=self.controlador_maestro.mostrar_menu_consultas)
        self.boton_regresar.grid(row=6, column=1, columnspan=2, pady=10, sticky="ew")

        self.cargar_productos()

    def cargar_productos(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        productos = obtener_productos_consulta()
        for producto in productos:
            valores_limpios = [str(dato) if dato is not None else "N/A" for dato in producto]
            self.tree.insert("", "end", values=valores_limpios)


if __name__ == "__main__":
    app = ctk.CTk()
    vista = ConsultaProducto(app)
    app.mainloop()