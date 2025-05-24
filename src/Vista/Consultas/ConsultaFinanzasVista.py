import customtkinter as ctk
from tkinter import ttk

from customtkinter import CTkFrame

from src.DAO.FinanzaDAO import consultar_finanzas

class ConsultaFinanzas:

    def __init__(self,parent,controlador_maestro):
        self.controlador_maestro=controlador_maestro
        self.frame = CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        for col in range(4):
            self.frame.columnconfigure(col, weight=1)
        for row in range(6):
            self.frame.rowconfigure(row, weight=1)

        # Título principal
        self.label_titulo = ctk.CTkLabel(self.frame, text="Resumen de Finanzas", font=("Arial", 30, "bold"), text_color="black")
        self.label_titulo.grid(row=0, column=1, columnspan=2, pady=10, sticky="n")

        # Frame contenedor de las tarjetas
        self.frame_totales = ctk.CTkFrame(self.frame)
        self.frame_totales.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

        # Card ingresos
        self.frame_ingresos = ctk.CTkFrame(self.frame_totales, corner_radius=12, fg_color="#3b82f6")
        self.frame_ingresos.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        self.label_ingresos_texto = ctk.CTkLabel(self.frame_ingresos, text="Ingresos Totales", font=("Arial", 16, "bold"), text_color="white")
        self.label_ingresos_texto.pack(pady=(10, 0))
        self.label_ingresos_valor = ctk.CTkLabel(self.frame_ingresos, text="$0.00", font=("Arial", 22, "bold"), text_color="white")
        self.label_ingresos_valor.pack(pady=(0, 10))

        # Card gastos
        self.frame_gastos = ctk.CTkFrame(self.frame_totales, corner_radius=12, fg_color="#ef4444")
        self.frame_gastos.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        self.label_gastos_texto = ctk.CTkLabel(self.frame_gastos, text="Gastos Totales", font=("Arial", 16, "bold"), text_color="white")
        self.label_gastos_texto.pack(pady=(10, 0))
        self.label_gastos_valor = ctk.CTkLabel(self.frame_gastos, text="$0.00", font=("Arial", 22, "bold"), text_color="white")
        self.label_gastos_valor.pack(pady=(0, 10))

        # Card ganancia
        self.frame_ganancia = ctk.CTkFrame(self.frame_totales, corner_radius=12, fg_color="#10b981")
        self.frame_ganancia.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        self.label_ganancia_texto = ctk.CTkLabel(self.frame_ganancia, text="Ganancia Real", font=("Arial", 16, "bold"), text_color="white")
        self.label_ganancia_texto.pack(pady=(10, 0))
        self.label_ganancia_valor = ctk.CTkLabel(self.frame_ganancia, text="$0.00", font=("Arial", 22, "bold"), text_color="white")
        self.label_ganancia_valor.pack(pady=(0, 10))

        # Card recuperado
        self.frame_recuperado = ctk.CTkFrame(self.frame_totales, corner_radius=12, fg_color="#f59e0b")
        self.frame_recuperado.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        self.label_recuperado_texto = ctk.CTkLabel(self.frame_recuperado, text="Inversión Recuperada", font=("Arial", 16, "bold"), text_color="white")
        self.label_recuperado_texto.pack(pady=(10, 0))
        self.label_recuperado_valor = ctk.CTkLabel(self.frame_recuperado, text="$0.00", font=("Arial", 22, "bold"), text_color="white")
        self.label_recuperado_valor.pack(pady=(0, 10))

        # Frame y tabla de detalles
        self.frame_tabla = ctk.CTkFrame(self.frame)
        self.frame_tabla.grid(row=2, column=0, columnspan=4, rowspan=3, padx=20, pady=10, sticky="nsew")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"))

        self.tree_tabla = ttk.Treeview(self.frame_tabla, columns=("Tipo", "Monto", "Descripcion", "Fecha"), show="headings")
        self.tree_tabla.heading("Tipo", text="Tipo")
        self.tree_tabla.heading("Monto", text="Monto")
        self.tree_tabla.heading("Descripcion", text="Descripción")
        self.tree_tabla.heading("Fecha", text="Fecha")

        self.tree_tabla.column("Tipo", anchor="center", width=150)
        self.tree_tabla.column("Monto", anchor="center", width=150)
        self.tree_tabla.column("Descripcion", anchor="w", width=300)
        self.tree_tabla.column("Fecha", anchor="center", width=150)

        self.tree_tabla.pack(fill="both", expand=True)

        # Botón regresar
        self.boton_regresar = ctk.CTkButton(self.frame, text="Menu Consultas", font=("Arial", 16, "bold"),
                                            width=200, height=40, corner_radius=20,
                                            command=self.controlador_maestro.mostrar_menu_consultas,
                                            hover_color="darkred")
        self.boton_regresar.grid(row=5, column=1, columnspan=2, pady=10, sticky="ew")

        # Inicializar datos
        self.actualizar_datos()

    def obtener_finanzas(self):
        return consultar_finanzas()

    def calcular_totales(self, datos):
        ingresos = 0
        gastos = 0

        for fila in datos:
            _, _, tipo, monto, _ = fila
            if tipo.lower() == "venta":
                ingresos += monto
            elif tipo.lower() == "inversion":
                gastos += monto

        ganancia = ingresos - gastos
        recuperado = gastos if ingresos >= gastos else ingresos

        return ingresos, gastos, ganancia, recuperado

    def actualizar_datos(self):
        datos = self.obtener_finanzas()
        ingresos, gastos, ganancia, recuperado = self.calcular_totales(datos)
        self.mostrar_datos(datos, ingresos, gastos, ganancia, recuperado)

    def mostrar_datos(self, datos, ingresos, gastos, ganancia, recuperado):
        for item in self.tree_tabla.get_children():
            self.tree_tabla.delete(item)

        for fila in datos:
            _, fecha, tipo, monto, descripcion = fila
            self.tree_tabla.insert("", "end", values=(tipo, f"${monto:,.2f}", descripcion, fecha))

        self.label_ingresos_valor.configure(text=f"${ingresos:,.2f}")
        self.label_gastos_valor.configure(text=f"${gastos:,.2f}")
        self.label_ganancia_valor.configure(text=f"${ganancia:,.2f}")
        self.label_recuperado_valor.configure(text=f"${recuperado:,.2f}")


