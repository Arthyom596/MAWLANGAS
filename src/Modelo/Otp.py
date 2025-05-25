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

        return False, "Correo no encontrado o OTP no enviado"

    otp_generado = datos["otp"]
    tiempo_envio = datos["fecha_envio"]

    if time.time() - tiempo_envio > 300:

        del otp_almacen[destinatario]
        return False, "OTP expirado. Por favor, solicite un nuevo código."

    # Convertimos ambos a str para comparar sin problema
    if str(otp_generado) == str(otp_ingresado):

        del otp_almacen[destinatario]
        return True, "OTP verificado correctamente"
    else:

        return False, "OTP incorrecto, verifique su código"



def manejar_otp(correo, otp_ingresado=None):
    if correo not in otp_almacen:
        enviar_otp(correo)
    else:
        if otp_ingresado:
            if verificar_otp(correo, otp_ingresado):
                print("Exito")
            else:
                print("Error")


