import customtkinter as ctk
from src.Vista.LoginVista import LoginVista
from src.Vista.RegistroVista import Registro
from src.Vista.MainVista import MainVista

class ControladorMaestro:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.app = ctk.CTk()
        self.app.geometry("800x600")
        self.app.title("Aplicación")

        self.vista_actual = None

        self.mostrar_login()

    def mostrar_login(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.login_vista = LoginVista(self.app, self)
        self.vista_actual = self.login_vista

    def mostrar_registro(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.registro_vista = Registro(self.app, self)
        self.vista_actual = self.registro_vista

    def mostrar_main(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.main_vista = MainVista(self.app, self)
        self.vista_actual = self.main_vista

    def ejecutar(self):
        self.app.mainloop()

if __name__ == "__main__":
    controlador = ControladorMaestro()
    controlador.ejecutar()
