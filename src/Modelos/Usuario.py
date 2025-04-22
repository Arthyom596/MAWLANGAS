import sqlite3

nombre_bd = "Mawlangas.db"

def conectar():
    return sqlite3.connect(nombre_bd)

def crear_usuario(usuario, contrasena, nombre, apellido_p, apellido_m, correo):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO Usuarios (Usuario, Contrasena, Nombre, ApellidoPaterno, ApellidoMaterno, Correo)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (usuario, contrasena, nombre, apellido_p, apellido_m, correo))
        conexion.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conexion.close()

def obtener_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def actualizar_usuario(id_usuario, usuario, contrasena, nombre, apellido_p, apellido_m, correo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE Usuarios
        SET Usuario = ?, Contrasena = ?, Nombre = ?, ApellidoPaterno = ?, ApellidoMaterno = ?, CorreoElectronico = ?
        WHERE IDUsuario = ?
    """, (usuario, contrasena, nombre, apellido_p, apellido_m, correo, id_usuario))
    conexion.commit()
    conexion.close()

def eliminar_usuario(id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE IDUsuario = ?", (id_usuario,))
    conexion.commit()
    conexion.close()

# Prueba
crear_usuario("Luis596", "contrasena123", "Luis", "Ramirez", "Sanchez", "Luiseduardo@gmail.com")
