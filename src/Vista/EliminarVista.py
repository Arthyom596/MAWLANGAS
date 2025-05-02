import customtkinter as ctk


class EliminarVista:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Eliminar")

        ctk.set_appearance_mode("dark")

        # Configurar columnas y filas
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)

        # Título
        self.etiqueta_titulo = ctk.CTkLabel(self.root, text="Eliminar", font=("Arial", 36, "bold"), text_color="white")
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="nsew")

        # Subtítulo
        self.etiqueta_subtitulo = ctk.CTkLabel(self.root, text="En proceso", font=("Arial", 18, "bold"),
                                               text_color="white")
        self.etiqueta_subtitulo.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")


if __name__ == "__main__":
    root = ctk.CTk()
    app = EliminarVista(root)
    root.mainloop()
