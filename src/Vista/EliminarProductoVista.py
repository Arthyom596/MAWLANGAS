import customtkinter as ctk
from tkinter import messagebox


class EliminarProductoVista(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Eliminar Producto")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(padx=40, pady=40)

        # Título centrado
        self.label_titulo = ctk.CTkLabel(
            self,
            text="Eliminar Producto",
            font=ctk.CTkFont(size=28, weight="bold"),
            anchor="center"
        )
        self.label_titulo.pack(pady=(10, 30))

        # Frame de selección centrado
        self.frame_selector = ctk.CTkFrame(self)
        self.frame_selector.pack(pady=(0, 30))

        self.combo_productos = ctk.CTkComboBox(
            self.frame_selector,
            values=[],
            width=350,
            state="readonly",
            font=ctk.CTkFont(size=15)
        )
        self.combo_productos.grid(row=0, column=0, padx=10, pady=20)

        self.boton_buscar = ctk.CTkButton(
            self.frame_selector,
            text="Buscar",
            width=130,
            height=35,
            font=ctk.CTkFont(size=14)
        )
        self.boton_buscar.grid(row=1, column=0, padx=10, pady=20)

        # Frame de resultados centrado
        self.frame_resultado = ctk.CTkFrame(self)
        self.frame_resultado.pack(padx=20, pady=10)

        self.labels_datos = {}
        for i, campo in enumerate(["ID", "Nombre", "Precio Compra", "Precio Venta"]):
            label = ctk.CTkLabel(
                self.frame_resultado,
                text=f"{campo}: ",
                anchor="w",
                font=ctk.CTkFont(size=17),
                width=400  # Para alinear y centrar
            )
            label.grid(row=i, column=0, padx=20, pady=8, sticky="w")
            self.labels_datos[campo] = label

        # Botón eliminar centrado (oculto al inicio)
        self.boton_eliminar = ctk.CTkButton(
            self,
            text="Eliminar Producto",
            fg_color="red",
            hover_color="#cc0000",
            width=220,
            height=45,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.boton_eliminar.pack(pady=30)
        self.boton_eliminar.pack_forget()

    def mostrar_datos_producto(self, producto):
        self.labels_datos["ID"].configure(text=f"ID: {producto[0]}")
        self.labels_datos["Nombre"].configure(text=f"Nombre: {producto[1]}")
        self.labels_datos["Precio Compra"].configure(text=f"Precio Compra: ${producto[2]:.2f}")
        self.labels_datos["Precio Venta"].configure(text=f"Precio Venta: ${producto[3]:.2f}")
        self.boton_eliminar.pack(pady=30)

    def ocultar_datos_producto(self):
        self.boton_eliminar.pack_forget()
        for label in self.labels_datos.values():
            label.configure(text="")

    def actualizar_combobox(self, nombres):
        self.combo_productos.configure(values=nombres)
        self.combo_productos.set("")

    def obtener_nombre_seleccionado(self):
        return self.combo_productos.get()

    def mostrar_mensaje(self, mensaje, error=False):
            messagebox.showinfo("Éxito", mensaje)
