import sqlite3

nombre_bd = "Mawlangas.db"

def conectar():
    return sqlite3.connect(nombre_bd)

def crear_usuario(usuario, contrasena, nombre, apellido_p, apellido_m):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO Usuarios (Usuario, Contrasena, Nombre, ApellidoPaterno, ApellidoMaterno)
            VALUES (?, ?, ?, ?, ?)
        """, (usuario, contrasena, nombre, apellido_p, apellido_m))
        conexion.commit()
        print("Usuario creado correctamente.")
    except sqlite3.IntegrityError:
        print("El nombre de usuario ya existe.")
    finally:
        conexion.close()

def obtener_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    return usuarios

def buscar_usuario_por_nombre(nombre_usuario):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE Usuario = ?", (nombre_usuario,))
    usuario = cursor.fetchone()
    conexion.close()
    return usuario

def actualizar_usuario(id_usuario, usuario, contrasena, nombre, apellido_p, apellido_m,correo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE Usuarios
        SET Usuario = ?, Contrasena = ?, Nombre = ?, ApellidoPaterno = ?, ApellidoMaterno = ?, Correo = ?
        WHERE IDUsuario = ?
    """, (usuario, contrasena, nombre, apellido_p, apellido_m, id_usuario,correo))
    conexion.commit()
    conexion.close()


def eliminar_usuario(id_usuario):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Usuarios WHERE IDUsuario = ?", (id_usuario,))
    conexion.commit()
    conexion.close()
