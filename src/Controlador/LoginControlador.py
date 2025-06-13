# LoginControlador.py
from src.Modelo.Login import verificar_usuario
from src.Modelo.Sesion import Sesion


class LoginControlador:
    def __init__(self, vista, controlador_maestro):
        self.vista = vista
        self.controlador_maestro = controlador_maestro

    def login_usuario(self, usuario, contrasena):
        resultado =verificar_usuario(usuario, contrasena)
        if resultado:
            id_usuario = resultado[0]
            nombre = resultado[1]
            self.vista.mostrar_mensaje("Login exitoso", "green")
            Sesion.set_usuario_activo(nombre)  # Guarda solo el string
            # Navegar a la vista principal luego de login
            self.controlador_maestro.mostrar_menu_principal()
        else:
            self.vista.mostrar_mensaje("Usuario o contraseña incorrectos", "red")
