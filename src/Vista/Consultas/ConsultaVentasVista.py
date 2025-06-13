import customtkinter as ctk
from tkinter import ttk
from src.DAO.VentasDAO import obtener_ventas

class ConsultaVentas:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro

        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)
        self.frame.configure(fg_color="#8cbbf1")

        for col in range(6):
            self.frame.columnconfigure(col, weight=1)
        for row in range(7):
            self.frame.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(
            self.frame, text="Consulta de Ventas",
            font=("Arial", 30, "bold"), text_color="black"
        )
        # Centrar título usando columnspan y sticky nsew para ocupar todo ancho de las columnas
        self.consulta.grid(column=0, row=0, columnspan=6, sticky="nsew", pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"), anchor="center")
        style.configure("Treeview", font=("Arial", 12), rowheight=28)

        self.tree = ttk.Treeview(
            self.frame,
            columns=("NombreProducto", "NombreSabor", "CantidadVendida", "Fecha", "Usuario"),
            show="headings"
        )

        self.tree.heading("NombreProducto", text="Producto")
        self.tree.heading("NombreSabor", text="Sabor")
        self.tree.heading("CantidadVendida", text="Cantidad")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Usuario", text="Usuario")

        # Cambiar anchor a center para Producto y Sabor
        self.tree.column("NombreProducto", width=200, anchor="center")
        self.tree.column("NombreSabor", width=200, anchor="center")
        self.tree.column("CantidadVendida", width=130, anchor="center")
        self.tree.column("Fecha", width=150, anchor="center")
        self.tree.column("Usuario", width=120, anchor="center")

        self.tree.grid(row=1, column=0, columnspan=6, rowspan=4, padx=20, pady=20, sticky="nsew")

        self.boton_regresar = ctk.CTkButton(
            self.frame, text="Regresar al Menú", font=("Arial", 16, "bold"),
            width=200, height=40, corner_radius=20, fg_color="red",
            command=self.controlador_maestro.mostrar_menu_consultas,
            hover_color="darkred"
        )
        self.boton_regresar.grid(row=6, column=1, columnspan=4, pady=10, sticky="ew")

        self.cargar_ventas()

    def cargar_ventas(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        ventas = obtener_ventas()
        for venta in ventas:
            # venta = (IDVenta, IDProducto, NombreProducto, IDSabor, NombreSabor, CantidadVendida, Fecha, Usuario)
            valores_limpios = [
                venta[2] if venta[2] is not None else "No disponible",    # NombreProducto
                venta[4] if venta[4] is not None else "No disponible",    # NombreSabor
                str(venta[5]) if venta[5] is not None else "N/A",         # CantidadVendida
                str(venta[6]) if venta[6] is not None else "N/A",         # Fecha
                str(venta[7]) if venta[7] is not None else "N/A",         # Usuario
            ]
            self.tree.insert("", "end", values=valores_limpios)
