# src/Controlador/RegistroControlador.py
from src.Modelo.Registro import validar_usuario, validar_contraseña, validar_nombre, validar_correo
from src.DAO.UsuariosDAO import crear_usuario

def registrar_usuario_controlador(datos):
    validaciones = {
        "usuario": validar_usuario,
        "contrasena": validar_contraseña,
        "nombre": validar_nombre,
        "apellido_p": validar_nombre,
        "apellido_m": validar_nombre,
        "correo": validar_correo
    }

    resultados = {}
    for clave, funcion in validaciones.items():
        valido, resultado = funcion(datos[clave])
        if not valido:
            return False, resultado
        resultados[clave] = resultado

    try:
        crear_usuario(
            resultados["usuario"],
            resultados["contrasena"],
            resultados["nombre"],
            resultados["apellido_p"],
            resultados["apellido_m"],
            resultados["correo"]
        )
        return True, "Usuario registrado correctamente"
    except Exception as e:
        return False, f"Error al registrar usuario: {e}"
