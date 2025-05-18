import bcrypt
import email_validator
import re

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
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', contraseña):
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
