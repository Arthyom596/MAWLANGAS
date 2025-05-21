import customtkinter as ctk

class MainVista:
    def __init__(self, parent, controlador_maestro):
        self.controlador_maestro = controlador_maestro
        self.frame = ctk.CTkFrame(parent)
        self.frame.pack(fill="both", expand=True)

        label = ctk.CTkLabel(self.frame, text="Bienvenido a la aplicación", font=("Arial", 24))
        label.pack(pady=20)

        logout_btn = ctk.CTkButton(self.frame, text="Cerrar sesión", command=self.cerrar_sesion)
        logout_btn.pack(pady=10)

    def cerrar_sesion(self):
        self.controlador_maestro.mostrar_login()
