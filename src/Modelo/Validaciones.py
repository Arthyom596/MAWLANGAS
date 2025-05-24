import re
from datetime import datetime

"""""
El proposito de esta clase con ayuda de las expresiones regulares(re) es crear metodos genericos para 
poder validar cualquier entrada de usuario sin importar la clase, es un filtro para que no entren 
caracteres que compromentan el programa 
cualquier metodo que implique una entrada de usuario debe ser validado con un metodo de esta clase primero
y despues debe llamar al CRUD de la respectiva clase para completar el movimiento en la base de datos
"""



"""""
El metodo validar texto permite el ingreso de caracteres de la A-Z mayuscula y minuscula incluyendo la ñ
No permite un ingreso menor a 1 caracter y no mayor a 50 caracteres 
"""
def validar_texto(texto):
    texto = str(texto).strip()

    if len(texto) == 0: #Compara la longitud si es igual a 0 retorna False
        return False, "Error: Texto vacio"
    if len(texto) > 50: #Compara la longitud si es mayor a 50 retorna False
        return False, "Error: Texto mayor a 50 caracteres"
    if not re.fullmatch(r"^[A-Za-zÑñ]+$", texto): #Si el texto no es una letra valida retorna False
        return False, "Error: El texto solo debe contener letras"
    return True, texto


"""""
El metodo validar numero permite el ingreso de numeros del 0 al 9 pidiendo 2 decimales opcionales 
No permite ingresar letras ni caracteres especiales  ni un numerp menor a 1 o mayor a 10
Finalmente devuelve el numero en su estado float para ingresarlo en la base de datos
"""
def validar_numero(numero):
    numero = str(numero).strip() #Convierte el numero en un String para ser evaluado

    if len(numero) < 1 or len(numero) > 8: #El numero debe ser
        return False, "Error: Número menor a 1 carácter o mayor a 8 caracteres"
    if not re.fullmatch(r"^[0-9]+(\.[0-9]{1,2})?$", numero):
        return False, "Error: Debe ser un número válido. Puede ser entero o con hasta dos decimales."
    numero_convertido = float(numero) #Convierte el String de numero a un flotante
    return True, round(numero_convertido, 2) #Redondea a 2 decimales y lo devuelve

""""
El metodo validar descripcion esta pensado para cualquier campo extenso delimitando su rango
de al menos 10 y maximo 255 caracteres es decir 1 byte permitiendo uso de cualquier caracter
"""
# Validar descripción con longitud mínima y máxima
def validar_descripcion(texto):
    texto = str(texto).strip() #Se limpia el texto

    if len(texto) < 10: #El texto no puede tener menos de 10 caracteres
        return False, "Error: El texto debe tener al menos 10 caracteres"
    if len(texto) > 255: #eL texto no puede tener mas de 255 caracteres
        return False, "Error: El texto no debe superar los 255 caracteres"
    return True, texto


# Obtiene la fecha actual en formato año-mes-dia-hora-minuto y lo retorna
def obtener_fecha_exacta_actual():
    ahora = datetime.now()
    return ahora.strftime('%Y-%m-%d %H:%M')


