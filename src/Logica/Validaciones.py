import re
import bcrypt
import email_validator


def validar_texto(texto):
    if len(texto) == 0:
        print("Error:Texto vacio")
        return False
    if len(texto[0]) >50:
        print("Error:Texto mayor a 50 caracteres")
        return False
    if not re.match("^[A-Za-zÑñ]+$",texto):
        print("Error el texto solo debe contener caracteres")
        return False



def validar_numero(numero):
    numero = str(numero).strip()

    if len(numero) == 0:
        print("Error: Número vacío")
        return False, None
    if len(numero) < 1 or len(numero) > 10:
        print("Error: Número menor a 1 carácter o mayor a 10 caracteres")
        return False, None
    if not re.fullmatch(r"^[0-9]+(\.[0-9]{1,2})?$", numero):
        print("Error: Debe ser un número válido. Puede ser entero o con hasta dos decimales.")
        return False, None

    try:
        numero_convertido = float(numero)
    except ValueError:
        print("Error: No se pudo convertir el número.")
        return False, None

    return True, round(numero_convertido, 2)

def validar_descripcion(texto):
    texto = str(texto).strip()

    if len(texto) == 0:
        print("Error: Texto vacío")
        return False, None
    if len(texto) < 10:
        print("Error: El texto debe tener al menos 10 caracteres")
        return False, None
    if len(texto) > 255:
        print("Error: El texto no debe superar los 255 caracteres")
        return False, None
    return True, texto

from datetime import datetime

def obtener_fecha_exacta_actual():
    ahora = datetime.now()
    return ahora.strftime('%Y-%m-%d %H:%M')




# Validar usuario
def validar_usuario(usuario):
    if not usuario or len(usuario.strip()) == 0:
        return False, "El nombre de usuario no puede estar vacío."
    if len(usuario) < 5 or len(usuario) > 50:
        return False, "El nombre de usuario debe tener entre 5 y 50 caracteres."
    if not re.fullmatch(r'^[A-Za-z0-9]+$', usuario):
        return False, "El nombre de usuario solo puede contener letras y números, sin caracteres especiales."
    return True, usuario


# Validar contraseña
def validar_contraseña(contraseña):
    if not contraseña or len(contraseña.strip()) == 0:
        return False, "La contraseña no puede estar vacía."
    if len(contraseña) < 8 or len(contraseña) > 50:
        return False, "La contraseña debe tener entre 8 y 50 caracteres."
    if not re.search(r'[0-9]', contraseña):
        return False, "La contraseña debe contener al menos un número."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        return False, "La contraseña debe contener al menos un carácter especial."

    # Hashear la contraseña
    contraseña_hash = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())
    return True, contraseña_hash


# Validar nombre o apellidos
def validar_nombre(nombre):
    if not nombre or len(nombre.strip()) == 0:
        return False, "El nombre no puede estar vacío."
    if len(nombre) > 50:
        return False, "El nombre no puede tener más de 50 caracteres."
    if not re.fullmatch(r'^[A-Za-zÑñ ]+$', nombre):
        return False, "El nombre solo puede contener letras y espacios."
    return True, nombre


def validar_correo(correo):
    if not correo or len(correo.strip()) == 0:
        return False, "El correo no puede estar vacío."
    try:
        validado = email_validator.validate_email(correo)
        return True, validado.normalized
    except email_validator.EmailNotValidError as e:
        return False, str(e)

