import os
import sqlite3

# Ruta del proyecto y base de datos
proyecto_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta_db = os.path.join(proyecto_base, 'BaseDatos')
os.makedirs(ruta_db, exist_ok=True)
nombre_bd = os.path.join(ruta_db, 'Mawlangas.db')


def conectar():
    try:
        conexion = sqlite3.connect(nombre_bd)
        conexion.execute("PRAGMA foreign_keys = ON")
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios(
                IDUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                Usuario TEXT UNIQUE NOT NULL,
                Contrasena TEXT NOT NULL,
                Nombre TEXT NOT NULL,
                ApellidoPaterno TEXT NOT NULL,
                ApellidoMaterno TEXT,
                Correo TEXT NOT NULL
            );
        """)
        conexion.commit()
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def crear_usuario(usuario, contrasena, nombre, apellido_p, apellido_m, correo):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            INSERT INTO Usuarios (Usuario, Contrasena, Nombre, ApellidoPaterno, ApellidoMaterno, Correo)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (usuario, contrasena, nombre, apellido_p, apellido_m, correo))
        conexion.commit()
    finally:
        conexion.close()


def obtener_usuarios():
    conexion = conectar()
    if not conexion:
        return []
    try:
        return conexion.execute("SELECT * FROM Usuarios").fetchall()
    finally:
        conexion.close()


def actualizar_usuario(id_usuario, usuario, contrasena, nombre, apellido_p, apellido_m, correo):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            UPDATE Usuarios
            SET Usuario = ?, Contrasena = ?, Nombre = ?, ApellidoPaterno = ?, ApellidoMaterno = ?, Correo = ?
            WHERE IDUsuario = ?
        """, (usuario, contrasena, nombre, apellido_p, apellido_m, correo, id_usuario))
        conexion.commit()
    finally:
        conexion.close()


def eliminar_usuario(id_usuario):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("DELETE FROM Usuarios WHERE IDUsuario = ?", (id_usuario,))
        conexion.commit()
    finally:
        conexion.close()
