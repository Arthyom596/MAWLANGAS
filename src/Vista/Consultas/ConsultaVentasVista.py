import customtkinter as ctk
from tkinter import ttk
from src.DAO.VentasDAO import obtener_ventas

class ConsultaVentas:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro

        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="#8cbbf1")

        for col in range(5):
            self.frame.columnconfigure(col, weight=1)
        for row in range(7):
            self.frame.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(self.frame, text="Consulta de Ventas", font=("Arial", 30, "bold"),
                                     text_color="black")
        self.consulta.grid(column=2, row=0, sticky="w", padx=80, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"), anchor="center")
        style.configure("Treeview", font=("Arial", 12), rowheight=28)

        self.tree = ttk.Treeview(self.frame,
                                 columns=("IDVenta", "IDProducto", "IDSabor", "CantidadVendida", "Fecha"),
                                 show="headings")

        self.tree.heading("IDVenta", text="ID Venta")
        self.tree.heading("IDProducto", text="ID Producto")
        self.tree.heading("IDSabor", text="ID Sabor")
        self.tree.heading("CantidadVendida", text="Cantidad Vendida")
        self.tree.heading("Fecha", text="Fecha")

        self.tree.column("IDVenta", width=80, anchor="center")
        self.tree.column("IDProducto", width=100, anchor="center")
        self.tree.column("IDSabor", width=100, anchor="center")
        self.tree.column("CantidadVendida", width=130, anchor="center")
        self.tree.column("Fecha", width=150, anchor="center")

        self.tree.grid(row=1, column=0, columnspan=5, rowspan=4, padx=20, pady=20, sticky="nsew")

        self.boton_regresar = ctk.CTkButton(self.frame, text="Regresar al Menú", font=("Arial", 16, "bold"),
                                            width=200, height=40, corner_radius=20, fg_color="red",
                                            command=self.controlador_maestro.mostrar_menu_consultas,
                                            hover_color="darkred")
        self.boton_regresar.grid(row=6, column=1, columnspan=3, pady=10, sticky="ew")

        self.cargar_ventas()

    def cargar_ventas(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        ventas = obtener_ventas()
        for venta in ventas:
            # venta = (IDVenta, IDProducto, IDSabor, CantidadVendida, Fecha)
            valores_limpios = [
                str(venta[0]) if venta[0] is not None else "N/A",
                str(venta[1]) if venta[1] is not None else "N/A",
                str(venta[2]) if venta[2] is not None else "No Aplica",
                str(venta[3]) if venta[3] is not None else "N/A",
                str(venta[4]) if venta[4] is not None else "N/A",
            ]
            self.tree.insert("", "end", values=valores_limpios)



