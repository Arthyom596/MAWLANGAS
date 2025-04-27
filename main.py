from src.Interfaces.Login import Login
from src.Interfaces.Registro import Registro
import customtkinter as ctk

class Main:
    def __init__(self):
        self.app = None

    def mostrar_login(self):
        if self.app:
            self.app.destroy()
        self.app = Login(self.abrir_registro)  # Se pasa el callback de abrir_registro
        self.app.mainloop()

    def abrir_registro(self):
        ventana = Registro()  # Crear la ventana de registro sin pasar 'self'
        ventana.mainloop()  # Esto es importante para que la nueva ventana se ejecute


if __name__ == '__main__':
    manager = Main()  # Instancia del Main
    manager.mostrar_login()  # Mostrar el login
