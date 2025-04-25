import re


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


import re

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

