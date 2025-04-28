import customtkinter as ctk
from src.Interfaces.Login import Login
from src.Interfaces.Registro import Registro
from src.Interfaces.MenuPrincipal import MenuPrincipal


class MainController:
    def __init__(self):
        self.root = ctk.CTk()  # Raíz principal
        self.root.geometry("850x650")
        self.root.title("Mi Aplicación")
        self.frame_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        self._cambiar_frame(Login)

    def login_exitoso(self):
        self._cambiar_frame(MenuPrincipal)

    def abrir_registro(self):
        self._cambiar_frame(Registro)

    def registro_exitoso(self):
        self.mostrar_login()

    def salir_app(self):
        self.root.destroy()
        print("La aplicación ha sido cerrada.")
        exit()

    def _cambiar_frame(self, frame_class):
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        # AQUÍ EL CAMBIO:
        self.frame_actual = frame_class(self.root, controller=self)
        self.frame_actual.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    main = MainController()
    main.run()
