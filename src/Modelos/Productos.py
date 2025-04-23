import sqlite3

nombre_bd = "Mawlangas.db"

def conectar():
    conexion = sqlite3.connect(nombre_bd)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def crear_producto(nombre, preciocompra, precioventa):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        INSERT INTO productos (Nombre, PrecioCompra, PrecioVenta) VALUES (?, ?, ?)
        """, (nombre, preciocompra, precioventa))
        conexion.commit()
    except sqlite3.IntegrityError:
        print("Error: Integridad de datos violada (posible clave duplicada u otro conflicto).")
    finally:
        conexion.close()

def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return productos

def actualizar_producto(id_producto,nombre, preciocompra, precioventa):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    UPDATE productos
    SET Nombre = ?,PrecioCompra = ?,PrecioVenta = ?
    WHERE IDProducto = ?
    """,(nombre, preciocompra, precioventa, id_producto))
    conexion.commit()
    conexion.close()


def eliminar_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE IDProducto = ?", (id_producto,))
    conexion.commit()
    conexion.close()


