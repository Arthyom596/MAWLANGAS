from src.Modelo.Login import verificar_usuario

class LoginControlador:
    def __init__(self, vista):
        self.vista = vista  # Se enlaza con la vista

    def login_usuario(self, usuario, contrasena):
        if verificar_usuario(usuario, contrasena):
            self.vista.mostrar_mensaje("Login exitoso", "green")
        else:
            self.vista.mostrar_mensaje("Usuario o contraseña incorrectos", "red")
