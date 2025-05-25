# src/Controlador/RegistroControlador.py
from src.Modelo.Otp import verificar_otp
from src.Modelo.Registro import validar_usuario, validar_contraseña, validar_nombre, validar_correo
from src.DAO.UsuariosDAO import crear_usuario


def validar_otp_wrapper(otp_value, datos_completos):
    correo = datos_completos.get("correo")
    print(f"Validando OTP para correo: {correo} con OTP ingresado: {otp_value}")
    return verificar_otp(correo, otp_value)


def registrar_usuario_controlador(datos):
    validaciones = {
        "usuario": validar_usuario,
        "contrasena": validar_contraseña,
        "nombre": validar_nombre,
        "apellido_p": validar_nombre,
        "apellido_m": validar_nombre,
        "correo": validar_correo,
        "otp": lambda otp_val: validar_otp_wrapper(otp_val, datos)
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
