import bcrypt
from src.Modelos.Usuario import buscar_usuario



def verificar_contraseña( contrasena_ingresada, contrasena_almacenada):
        """Compara la contraseña ingresada con el hash almacenado."""
        if bcrypt.checkpw(contrasena_ingresada.encode(), contrasena_almacenada.encode()):
            return True
        return False

def verificar_usuario( usuario, contrasena):
        """Busca al usuario y verifica su contraseña."""
        # Busca el usuario en la base de datos
        usuario_encontrado = buscar_usuario(usuario)

        if usuario_encontrado:
            # Si el usuario es encontrado, se compara la contraseña
            contrasena_almacenada = usuario_encontrado[2]  # Suponiendo que el hash de la contraseña está en el tercer campo
            if verificar_contraseña(contrasena, contrasena_almacenada):  # Ahora se usa `self`
                return True
        return False
