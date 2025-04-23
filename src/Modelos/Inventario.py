import sqlite3

nombre_bd = "Mawlangas.db"

def conectar():
    conexion = sqlite3.connect(nombre_bd)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

# Crear inventario
def crear_inventario(id_producto, id_sabor, cantidad, fecha_actualizacion):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        INSERT INTO Inventario (IDProducto, IDSabor, Cantidad, FechaActualizacion)
        VALUES (?, ?, ?, ?)
        """, (id_producto, id_sabor, cantidad, fecha_actualizacion))
        conexion.commit()
        print("Inventario creado correctamente.")
    except sqlite3.IntegrityError:
        print("Error: No se pudo crear el inventario (posible clave duplicada o conflicto).")
    finally:
        conexion.close()

# Obtener inventarios
def obtener_inventarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Inventario")
    inventarios = cursor.fetchall()
    conexion.close()
    return inventarios

# Actualizar inventario
def actualizar_inventario(id_inventario, id_producto, id_sabor, cantidad, fecha_actualizacion):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    UPDATE Inventario
    SET IDProducto = ?, IDSabor = ?, Cantidad = ?, FechaActualizacion = ?
    WHERE IDInventario = ?
    """, (id_producto, id_sabor, cantidad, fecha_actualizacion, id_inventario))
    conexion.commit()
    conexion.close()

# Eliminar inventario
def eliminar_inventario(id_inventario):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Inventario WHERE IDInventario = ?", (id_inventario,))
    conexion.commit()
    conexion.close()
