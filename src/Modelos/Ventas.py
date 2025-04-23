import sqlite3

nombre_bd = "Mawlangas.bd"

def conectar():
    conexion = sqlite3.connect(nombre_bd)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

#Crear una venta
def crear_venta(fecha, id_producto, id_sabor, cantidad_vendida, preparado, precio_venta):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO Ventas(Fecha, IDProducto, IDSabor, CantidadVendida, Preparado, PrecioVenta)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (fecha, id_producto, id_sabor, cantidad_vendida, preparado, precio_venta))
        conexion.commit()
        print("Venta registrada correctamente.")
    except sqlite3.IntegrityError:
        print("Error: No se pudo registrar la venta (clave foránea inválida o conflicto).")
    finally:
        conexion.close()

#Consulta Ventas
def obtener_ventas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Ventas")
    ventas=cursor.fetchall()
    conexion.close()
    return ventas

#No se pueden modificar las ventas por integridad

#No se pueden eliminar ventas por integridad
