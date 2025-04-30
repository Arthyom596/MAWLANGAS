import customtkinter as ctk

class MenuPrincipal:
    def __init__(self, parent):
        self.parent = parent

        # Configuración del fondo oscuro para el frame
        self.frame = ctk.CTkFrame(parent, bg_color="#2B2B2B")
        self.frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.titulo = ctk.CTkLabel(self.frame, text="Menú Principal", font=("Helvetica", 36, "bold"), text_color="white")
        self.titulo.grid(row=0, column=0, columnspan=3, pady=(30, 20))

        def crear_boton(texto, color="#3B8ED0", hover="#2F6BA8"):
            return ctk.CTkButton(self.frame, text=texto, font=("Arial", 18, "bold"),
                                 height=60, width=250, corner_radius=20,
                                 fg_color=color, hover_color=hover)

        self.boton_inventario = crear_boton("📦 Inventario")
        self.boton_inventario.grid(row=1, column=0, padx=20, pady=15)

        self.boton_finanzas = crear_boton("💰 Finanzas")
        self.boton_finanzas.grid(row=1, column=1, padx=20, pady=15)

        self.boton_ventas = crear_boton("🛒 Iniciar Venta", color="#4CAF50", hover="#3E8E41")
        self.boton_ventas.grid(row=1, column=2, padx=20, pady=15)

        self.boton_productos = crear_boton("🧾 Productos")
        self.boton_productos.grid(row=2, column=0, padx=20, pady=15)

        self.boton_modificar = crear_boton("✏️ Modificar")
        self.boton_modificar.grid(row=2, column=1, padx=20, pady=15)

        self.boton_eliminar = crear_boton("🗑️ Eliminar Elementos", color="#FF4C4C", hover="#CC3C3C")
        self.boton_eliminar.grid(row=2, column=2, padx=20, pady=15)

        self.boton_consultas = crear_boton("🔍 Consultas")
        self.boton_consultas.grid(row=3, column=1, padx=20, pady=15)

        self.etiqueta_version = ctk.CTkLabel(self.frame, text="Versión 1.0 • Desarrollado por Arthyom596", font=("Arial", 12),
                                             text_color="gray")
        self.etiqueta_version.grid(row=5, column=0, columnspan=3, pady=20)

    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

# Inicialización para prueba
if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("850x650")
    app.title("Inicio")
    app.configure(bg_color="#2B2B2B")  # Fondo oscuro para la ventana

    menu = MenuPrincipal(app)
    menu.mostrar()

    app.mainloop()
