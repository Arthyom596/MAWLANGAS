


class Sesion:

    usuario_activo = None

    @classmethod
    def set_usuario_activo(cls, usuario):
        cls.usuario_activo = usuario
    @classmethod
    def cerrar_sesion(cls):
        cls.usuario_activo = None

    @classmethod
    def obtener_usuario(cls):
        return cls.usuario_activo


