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
            CREATE TABLE IF NOT EXISTS Productos(
                IDProducto INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT NOT NULL,
                PrecioCompra REAL NOT NULL,
                PrecioVenta REAL NOT NULL
            );
        """)
        conexion.commit()
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def crear_producto(nombre, precio_compra, precio_venta):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            INSERT INTO Productos (Nombre, PrecioCompra, PrecioVenta)
            VALUES (?, ?, ?)
        """, (nombre, precio_compra, precio_venta))
        conexion.commit()
    finally:
        conexion.close()


def obtener_productos():
    conexion = conectar()
    if not conexion:
        return []
    try:
        return conexion.execute("SELECT * FROM Productos").fetchall()
    finally:
        conexion.close()


def actualizar_producto(id_producto, nombre, precio_compra, precio_venta):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            UPDATE Productos
            SET Nombre = ?, PrecioCompra = ?, PrecioVenta = ?
            WHERE IDProducto = ?
        """, (nombre, precio_compra, precio_venta, id_producto))
        conexion.commit()
    finally:
        conexion.close()


def eliminar_producto(id_producto):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("DELETE FROM Productos WHERE IDProducto = ?", (id_producto,))
        conexion.commit()
    finally:
        conexion.close()


# buscar producto por nombre
def buscar_producto(nombre_producto):
    conexion = conectar()
    if not conexion:
        return None
    try:
        result = conexion.execute("SELECT * FROM Productos WHERE Nombre = ?", (nombre_producto,)).fetchone()
        return result
    finally:
        conexion.close()

def obtener_ultimo_producto():
    conexion = conectar()
    try:
        resultado = conexion.execute("SELECT IDProducto FROM Productos ORDER BY IDProducto DESC LIMIT 1").fetchone()
        if resultado:
            return resultado[0]
        else:
            return None
    finally:
        conexion.close()