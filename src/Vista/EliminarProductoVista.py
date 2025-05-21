# view.py
import customtkinter as ctk

class EliminarProductoVista(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Eliminar Producto")
        self.geometry("700x450")
        self.configure(padx=20, pady=20)

        self.label_titulo = ctk.CTkLabel(self, text="Eliminar Producto", font=ctk.CTkFont(size=26, weight="bold"))
        self.label_titulo.pack(pady=(10, 25))

        self.frame_selector = ctk.CTkFrame(self)
        self.frame_selector.pack(fill="x", pady=10)

        self.combo_productos = ctk.CTkComboBox(self.frame_selector, width=300, state="readonly", font=ctk.CTkFont(size=15))
        self.combo_productos.pack(side="left", padx=(20, 10), pady=15)

        self.boton_buscar = ctk.CTkButton(self.frame_selector, text="Buscar", width=120, height=35, font=ctk.CTkFont(size=14))
        self.boton_buscar.pack(side="left", padx=(10, 20), pady=15)

        self.frame_resultado = ctk.CTkFrame(self)
        self.frame_resultado.pack(fill="both", expand=True, pady=10, padx=10)

        self.labels_datos = {}
        for campo in ["ID", "Nombre", "Precio Compra", "Precio Venta"]:
            label = ctk.CTkLabel(self.frame_resultado, text=f"{campo}: ", anchor="w", font=ctk.CTkFont(size=16))
            label.pack(fill="x", padx=10, pady=8)
            self.labels_datos[campo] = label

        self.boton_eliminar = ctk.CTkButton(self, text="Eliminar Producto", fg_color="red", hover_color="#cc0000",
                                            width=200, height=40, font=ctk.CTkFont(size=15, weight="bold"))
        self.boton_eliminar.pack(pady=20)
        self.boton_eliminar.pack_forget()

    def mostrar_mensaje(self, texto, color):
        mensaje = ctk.CTkLabel(self, text=texto, text_color=color, font=ctk.CTkFont(size=14))
        mensaje.pack(pady=(5, 0))
        self.after(3000, mensaje.destroy)
