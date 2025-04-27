import re
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


