import sqlite3

nombre_bd = "Mawlangas.db"

def conectar():
    return sqlite3.connect(nombre_bd)

# Crear sabor
def crear_sabor(id_producto, nombre_sabor):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        INSERT INTO Sabores (IDProducto, NombreSabor) VALUES (?, ?)
        """, (id_producto, nombre_sabor))
        conexion.commit()
        print("Sabor creado correctamente.")
    except sqlite3.IntegrityError:
        print("Error: El sabor no se pudo crear ")
    finally:
        conexion.close()

# Obtener todos los sabores
def obtener_sabores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Sabores")
    sabores = cursor.fetchall()
    conexion.close()
    return sabores

# Actualizar sabor
def actualizar_sabor(id_sabor, id_producto, nombre_sabor):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    UPDATE Sabores
    SET IDProducto = ?, NombreSabor = ?
    WHERE IDSabor = ?
    """, (id_producto, nombre_sabor, id_sabor))
    conexion.commit()
    conexion.close()

# Eliminar sabor
def eliminar_sabor(id_sabor):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM Sabores WHERE IDSabor = ?", (id_sabor,))
    conexion.commit()
    conexion.close()
