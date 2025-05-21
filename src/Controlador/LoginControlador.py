# LoginControlador.py

from src.Modelo.Login import verificar_usuario

class LoginControlador:
    def __init__(self, vista, controlador_maestro):
        self.vista = vista
        self.controlador_maestro = controlador_maestro

    def login_usuario(self, usuario, contrasena):
        if verificar_usuario(usuario, contrasena):
            self.vista.mostrar_mensaje("Login exitoso", "green")
            # Navegar a la vista principal luego de login
            self.controlador_maestro.mostrar_main()
        else:
            self.vista.mostrar_mensaje("Usuario o contraseña incorrectos", "red")
