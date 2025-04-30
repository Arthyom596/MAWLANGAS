import smtplib
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

""""
El proposito de esta clase es manejar toda la logica de la creacion,manejo y envio de los codigos OTP
para verificar correos electronicos validos y hacer un registro exitoso, se puede usar enviar otp para 
enviar otro tipo de correos automatizados si es necesario
"""

otp_almacen = {}

def generar_otp():
    return random.randint(100000, 999999)

def enviar_otp(destinatario):
    otp = generar_otp()
    otp_almacen[destinatario] = {
        "otp": otp,
        "fecha_envio": time.time()
    }

    remitente = "mawlangasoficial@gmail.com"

    try:
        conexion = smtplib.SMTP("smtp.gmail.com", 587)
        conexion.ehlo()
        conexion.starttls()
        conexion.login(user=remitente, password="ztiy wnom deas wqfp")

        mensaje = MIMEMultipart()
        mensaje["From"] = remitente
        mensaje["To"] = destinatario
        mensaje["Subject"] = "Codigo de verificacion"

        cuerpo = f"Tu codigo OTP es: {otp}"
        mensaje.attach(MIMEText(cuerpo, "plain", "utf-8"))

        conexion.sendmail(from_addr=remitente, to_addrs=destinatario, msg=mensaje.as_string())
        conexion.quit()

    except Exception as e:
        print(e)

def verificar_otp(destinatario, otp_ingresado):
    datos = otp_almacen.get(destinatario)
    if not datos:
        print("Error, no se encontro el correo asociado")
        return False

    otp_generado = datos["otp"]
    tiempo_envio = datos["fecha_envio"]

    if time.time() - tiempo_envio > 300:
        print("otp expirado")
        del otp_almacen[destinatario]
        return False
    if otp_generado == otp_ingresado:
        print("Registro exitoso")
        del otp_almacen[destinatario]
        return True
    else:
        print("otp incorrecto")
        return False


def manejar_otp(correo, otp_ingresado=None):
    print(f"Correo recibido: {correo}")  # Verifica el valor de correo
    if correo not in otp_almacen:
        enviar_otp(correo)
    else:
        if otp_ingresado:
            if verificar_otp(correo, otp_ingresado):
                print("Exito")
            else:
                print("Error")


