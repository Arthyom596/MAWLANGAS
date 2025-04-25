import re
import bcrypt
import email_validator
from datetime import datetime


# Validar texto genérico (solo letras)
def validar_texto(texto):
    texto = str(texto).strip()

    if len(texto) == 0:
        return False, "Error: Texto vacío"
    if len(texto) > 50:
        return False, "Error: Texto mayor a 50 caracteres"
    if not re.fullmatch(r"^[A-Za-zÑñ]+$", texto):
        return False, "Error: El texto solo debe contener letras"
    return True, texto


# Validar número decimal con hasta dos decimales
def validar_numero(numero):
    numero = str(numero).strip()

    if len(numero) == 0:
        return False, "Error: Número vacío"
    if len(numero) < 1 or len(numero) > 10:
        return False, "Error: Número menor a 1 carácter o mayor a 10 caracteres"
    if not re.fullmatch(r"^[0-9]+(\.[0-9]{1,2})?$", numero):
        return False, "Error: Debe ser un número válido. Puede ser entero o con hasta dos decimales."

    try:
        numero_convertido = float(numero)
    except ValueError:
        return False, "Error: No se pudo convertir el número."

    return True, round(numero_convertido, 2)


# Validar descripción con longitud mínima y máxima
def validar_descripcion(texto):
    texto = str(texto).strip()

    if len(texto) == 0:
        return False, "Error: Texto vacío"
    if len(texto) < 10:
        return False, "Error: El texto debe tener al menos 10 caracteres"
    if len(texto) > 255:
        return False, "Error: El texto no debe superar los 255 caracteres"
    return True, texto


# Obtener fecha actual
def obtener_fecha_exacta_actual():
    ahora = datetime.now()
    return ahora.strftime('%Y-%m-%d %H:%M')


# Validar usuario
def validar_usuario(usuario):
    usuario = str(usuario).strip()

    if not usuario:
        return False, "El nombre de usuario no puede estar vacío."
    if len(usuario) < 5 or len(usuario) > 50:
        return False, "El nombre de usuario debe tener entre 5 y 50 caracteres."
    if not re.fullmatch(r'^[A-Za-z0-9]+$', usuario):
        return False, "El nombre de usuario solo puede contener letras y números, sin caracteres especiales."
    return True, usuario


# Validar contraseña
def validar_contraseña(contraseña):
    contraseña = str(contraseña).strip()

    if not contraseña:
        return False, "La contraseña no puede estar vacía."
    if len(contraseña) < 8 or len(contraseña) > 50:
        return False, "La contraseña debe tener entre 8 y 50 caracteres."
    if not re.search(r'[0-9]', contraseña):
        return False, "La contraseña debe contener al menos un número."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        return False, "La contraseña debe contener al menos un carácter especial."

    contraseña_hash = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())
    return True, contraseña_hash.decode('utf-8')


# Validar nombres y apellidos
def validar_nombre(nombre):
    nombre = str(nombre).strip()

    if not nombre:
        return False, "Debe llenar su nombre completo."
    if len(nombre) > 50:
        return False, "El nombre no puede tener más de 50 caracteres."
    if not re.fullmatch(r'^[A-Za-zÑñ ]+$', nombre):
        return False, "El nombre solo puede contener letras y espacios."
    return True, nombre


# Validar correo electrónico
def validar_correo(correo):
    correo = str(correo).strip()

    if not correo:
        return False, "El correo no puede estar vacío."
    try:
        validado = email_validator.validate_email(correo)
        return True, validado.normalized
    except email_validator.EmailNotValidError as e:
        return False, f"Error en el correo: {str(e)}"
