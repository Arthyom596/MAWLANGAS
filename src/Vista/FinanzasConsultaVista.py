import customtkinter as ctk
from tkinter import ttk

class FinanzasVista(ctk.CTk):

    def __init__(self, controlador):
        super().__init__()

        self.controlador = controlador

        self.title("Consulta de Finanzas")
        self.geometry("800x500")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Título
        titulo = ctk.CTkLabel(self, text="Resumen de Finanzas", font=ctk.CTkFont(size=24, weight="bold"))
        titulo.pack(pady=20)

        # Frame de totales
        self.frame_totales = ctk.CTkFrame(self)
        self.frame_totales.pack(pady=10, padx=20, fill="x")

        # Crear etiquetas de resumen
        self.ingresos_label = self.crear_label(self.frame_totales, "Ingresos Totales", "$0.00", "#3b82f6")
        self.gastos_label = self.crear_label(self.frame_totales, "Gastos Totales", "$0.00", "#ef4444")
        self.ganancia_label = self.crear_label(self.frame_totales, "Ganancia Real", "$0.00", "#10b981")
        self.recuperado_label = self.crear_label(self.frame_totales, "Inversión Recuperada", "$0.00", "#f59e0b")

        # Frame de la tabla
        self.tabla_frame = ctk.CTkFrame(self)
        self.tabla_frame.pack(pady=10, fill="both", expand=True, padx=20)

        # Treeview
        self.tabla = ttk.Treeview(self.tabla_frame, columns=("Tipo", "Monto", "Descripcion", "Fecha"), show="headings")
        self.tabla.heading("Tipo", text="Tipo")
        self.tabla.heading("Monto", text="Monto")
        self.tabla.heading("Descripcion", text="Descripción")
        self.tabla.heading("Fecha", text="Fecha")

        self.tabla.column("Tipo", anchor="center", width=100)
        self.tabla.column("Monto", anchor="center", width=100)
        self.tabla.column("Descripcion", anchor="w", width=300)
        self.tabla.column("Fecha", anchor="center", width=100)

        self.tabla.pack(fill="both", expand=True)

        # Botón para actualizar datos
        actualizar_btn = ctk.CTkButton(self, text="Actualizar datos", command=self.controlador.actualizar_datos)
        actualizar_btn.pack(pady=10)

    def crear_label(self, frame, texto, valor="$0.00", color="#3b82f6"):
        container = ctk.CTkFrame(frame, corner_radius=12, fg_color=color)
        container.pack(side="left", expand=True, fill="both", padx=10, pady=10)

        label_texto = ctk.CTkLabel(container, text=texto, font=ctk.CTkFont(size=16, weight="bold"), text_color="white")
        label_texto.pack(pady=(10, 0))

        label_valor = ctk.CTkLabel(container, text=valor, font=ctk.CTkFont(size=22, weight="bold"), text_color="white")
        label_valor.pack(pady=(0, 10))

        return label_valor

    def mostrar_datos(self, datos, ingresos, gastos, ganancia, recuperado):
        # Limpiar tabla actual
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar datos en tabla
        for fila in datos:
            _, fecha, tipo, monto, descripcion = fila
            self.tabla.insert("", "end", values=(tipo, f"${monto:,.2f}", descripcion, fecha))

        # Actualizar etiquetas
        self.ingresos_label.configure(text=f"${ingresos:,.2f}")
        self.gastos_label.configure(text=f"${gastos:,.2f}")
        self.ganancia_label.configure(text=f"${ganancia:,.2f}")
        self.recuperado_label.configure(text=f"${recuperado:,.2f}")
