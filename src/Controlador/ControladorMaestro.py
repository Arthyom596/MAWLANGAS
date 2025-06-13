import customtkinter as ctk

from src.Vista.FinanzaVista import FinanzasVista
from src.Vista.LoginVista import LoginVista
from src.Vista.RegistroVista import Registro
from src.Vista.MenuPrincipalVista import MenuPrincipal
from src.Vista.InventarioVista import InventarioVista
from src.Vista.ProductoVista import ProductoVista
from src.Vista.VentaVista import VentaVista
from src.Vista.Consultas.ConsultasMenuVista import ConsultasMenuVista
from src.Vista.Consultas.ConsultaFinanzasVista import ConsultaFinanzas
from src.Vista.Consultas.ConsultaInventarioVista import ConsultaInventarioVista
from src.Vista.Consultas.ConsultaSaborVista import ConsultaSabor
from src.Vista.Consultas.ConsultaUsuarioVista import ConsultaUsuario
from src.Vista.Consultas.ConsultaProductoVista import ConsultaProducto
from src.Vista.Consultas.ConsultaVentasVista import ConsultaVentas
from src.Vista.Eliminar.MenuPrincipalEliminar import EliminarVista
from src.Vista.Eliminar.EliminarProductoVista import EliminarProductoVista
from src.Vista.Eliminar.EliminarUsuarioVista import EliminarUsuarioVista
from src.Vista.Eliminar.EliminarSaborVista import EliminarSaborVista
from src.Vista.Modificar.MenuPrincipalModificar import ModificarVista
from src.Vista.Modificar.ModificarProductoVista import ModificarProductoVista
from src.Vista.Modificar.ModificarUsuarioVista import ModificarUsuarioVista
from src.Vista.Modificar.ModificarSaborVista import ModificarSaborVista
from src.Vista.Clientes.MenuCliente import MenuCliente
from src.Modelo.Sesion import Sesion


class ControladorMaestro:
    def __init__(self):


        self.app = ctk.CTk()
        self.app.geometry("900x600")
        self.app.title("Mawlangas ")
        self.app.resizable(False, False)

        self.vista_actual = None
        self.mostrar_login()
        #self.mostrar_menu_principal()

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
        usuario_activo = Sesion.obtener_usuario()
        nombre = usuario_activo if usuario_activo else "Usuario"
        self.menu_principal.actualizar_bienvenida(f"{nombre}")

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
        self.app.geometry("850x600")
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

    def consultar_finanzas(self):
         if self.vista_actual:
             self.vista_actual.frame.destroy()
         self.consulta_finanzas = ConsultaFinanzas(self.app, self)
         self.vista_actual = self.consulta_finanzas

    def consultar_inventario(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.consulta_inventario = ConsultaInventarioVista(self.app, self)
        self.vista_actual = self.consulta_inventario

    def consultar_producto(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.consulta_producto = ConsultaProducto(self.app, self)
        self.vista_actual = self.consulta_producto

    def consultar_usuarios(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.consulta_usuario = ConsultaUsuario(self.app, self)
        self.vista_actual = self.consulta_usuario

    def consultar_sabores(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.consulta_sabores = ConsultaSabor(self.app, self)
        self.vista_actual = self.consulta_sabores

    def consultar_ventas(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.consulta_venta = ConsultaVentas(self.app, self)
        self.vista_actual = self.consulta_venta

    def menu_eliminar(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.main_eliminar = EliminarVista(self.app, self)
        self.vista_actual = self.main_eliminar

    def menu_modificar(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.main_modificar = ModificarVista(self.app, self)
        self.vista_actual = self.main_modificar

    def eliminar_productos(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.eliminar_producto = EliminarProductoVista(self.app, self)
        self.vista_actual = self.eliminar_producto

    def eliminar_usuarios(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.eliminar_usuario = EliminarUsuarioVista(self.app, self)
        self.vista_actual = self.eliminar_usuario

    def eliminar_sabores(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.eliminar_sabor = EliminarSaborVista(self.app, self)
        self.vista_actual = self.eliminar_sabor

    def modificar_productos(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.modifica_sabor = ModificarProductoVista(self.app, self)
        self.vista_actual = self.modifica_sabor

    def modificar_usuarios(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.modifica_sabor = ModificarUsuarioVista(self.app, self)
        self.vista_actual = self.modifica_sabor

    def modificar_sabores(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.modifica_sabor = ModificarSaborVista(self.app, self)
        self.vista_actual = self.modifica_sabor

    def menu_cliente(self):
        if self.vista_actual:
            self.vista_actual.frame.destroy()
        self.menu_clientes = MenuCliente(self.app, self)
        self.vista_actual = self.menu_clientes













    def ejecutar(self):
        self.app.mainloop()


