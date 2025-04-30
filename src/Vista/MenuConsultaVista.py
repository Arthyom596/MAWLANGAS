import customtkinter as ctk

class MenuConsulta:
    def __init__(self, root):
        self.app = root
        self.app.geometry("800x600")
        self.app.title("Consultas")

        for i in range(3):
            self.app.columnconfigure(i, weight=1)

        for i in range(4):
            self.app.rowconfigure(i, weight=1)

        self.etiqueta_consultas = ctk.CTkLabel(self.app, text="Consultas", font=("Helvetica", 36, "bold"), text_color="white")
        self.etiqueta_consultas.grid(row=0, column=1, sticky="nsew")

        self.btn_inventario = ctk.CTkButton(self.app, text="Inventario")
        self.btn_inventario.grid(row=1, column=0)

        self.btn_finanzas = ctk.CTkButton(self.app, text="Finanzas")
        self.btn_finanzas.grid(row=1, column=2)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ctk.CTk()
    app_instance = MenuConsulta(app)
    app.mainloop()
