import customtkinter as ctk

from src.Vista.FinanzaVista import FinanzasVista
from src.Vista.LoginVista import LoginVista
from src.Vista.RegistroVista import Registro
from src.Vista.MenuPrincipalVista import MenuPrincipal
from src.Vista.InventarioVista import InventarioVista
from src.Vista.ProductoVista import ProductoVista
from src.Vista.VentaVista import VentaVista
from src.Vista.Consultas.ConsultasMenuVista import ConsultasMenuVista

class ControladorMaestro:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.app = ctk.CTk()
        self.app.geometry("800x600")
        self.app.title("Mawlangas ")

        self.vista_actual = None

        self.mostrar_menu_principal()

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

    def mostrar_menu_principal(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.menu_principal = MenuPrincipal(self.app, self)
        self.vista_actual = self.menu_principal

    def mostrar_inventario(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.inventario_vista = InventarioVista(self.app, self)
        self.vista_actual = self.inventario_vista

    def mostrar_finanzas(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.finanzas_vista = FinanzasVista(self.app, self)
        self.vista_actual = self.finanzas_vista

    def mostrar_productos(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.app.geometry("850x650")
        self.productos_vista = ProductoVista(self.app, self)
        self.vista_actual = self.productos_vista

    def mostrar_ventas(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.app.geometry("800x600")
        self.ventas_vista = VentaVista(self.app, self)
        self.vista_actual = self.ventas_vista

    def mostrar_menu_consultas(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.menu_consultas = ConsultasMenuVista(self.app, self)
        self.vista_actual = self.menu_consultas



    def ejecutar(self):
        self.app.mainloop()

if __name__ == "__main__":
    controlador = ControladorMaestro()
    controlador.ejecutar()
