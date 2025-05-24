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
        CREATE TABLE IF NOT EXISTS Sabores (
            IDSabor INTEGER PRIMARY KEY AUTOINCREMENT,
            IDProducto INTEGER NOT NULL,
            NombreSabor TEXT,
            FOREIGN KEY (IDProducto) REFERENCES Productos(IDProducto) ON DELETE CASCADE
        );
        """)
        conexion.commit()
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Crear sabor
def crear_sabor(id_producto, nombre_sabor):
    conexion = conectar()
    if not conexion:
        return
    try:
        # Si el nombre del sabor es vacío, "Sin sabor" o None, lo dejamos como NULL
        if nombre_sabor == "Sin sabor" or nombre_sabor is None:
            nombre_sabor = None  # Permitimos NULL para 'Sin sabor'

        conexion.execute("""
            INSERT INTO Sabores (IDProducto, NombreSabor) VALUES (?, ?)
        """, (id_producto, nombre_sabor))
        conexion.commit()
        print("Sabor creado correctamente.")
    except sqlite3.IntegrityError:
        print("Error: El sabor no se pudo crear")
    finally:
        conexion.close()


# Obtener todos los sabores
def obtener_sabores():
    conexion = conectar()
    if not conexion:
        return []
    try:
        return conexion.execute("SELECT * FROM Sabores").fetchall()
    finally:
        conexion.close()

# Actualizar sabor
def actualizar_sabor(id_sabor, id_producto, nombre_sabor):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            UPDATE Sabores
            SET IDProducto = ?, NombreSabor = ?
            WHERE IDSabor = ?
        """, (id_producto, nombre_sabor, id_sabor))
        conexion.commit()
    finally:
        conexion.close()

# Eliminar sabor
def eliminar_sabor(id_sabor):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("DELETE FROM Sabores WHERE IDSabor = ?", (id_sabor,))
        conexion.commit()
    finally:
        conexion.close()

def obtener_sabores_por_producto(id_producto):
    conexion = conectar()
    if not conexion:
        return []
    try:
        return conexion.execute("""
            SELECT IDSabor, NombreSabor FROM Sabores
            WHERE IDProducto = ?
        """, (id_producto,)).fetchall()
    finally:
        conexion.close()



# Obtener el ID de un sabor por nombre
def obtener_id_sabor(nombre_sabor, id_producto):
    conexion = conectar()
    if not conexion:
        return None
    try:
        result = conexion.execute("""
            SELECT IDSabor FROM Sabores
            WHERE NombreSabor = ? AND IDProducto = ?
        """, (nombre_sabor, id_producto)).fetchone()
        return result[0] if result else None
    finally:
        conexion.close()


def obtener_nombre_sabor_por_id(id_sabor):
    conexion = conectar()
    if not conexion:
        return None
    try:
        resultado = conexion.execute("""
            SELECT NombreSabor FROM Sabores
            WHERE IDSabor = ?
        """, (id_sabor,)).fetchone()
        return resultado[0] if resultado else None
    finally:
        conexion.close()

def obtener_sabores_con_nombre_producto():
    conexion = conectar()
    if not conexion:
        return []
    try:
        return conexion.execute("""
            SELECT s.IDSabor, p.Nombre, s.NombreSabor
            FROM Sabores s
            JOIN Productos p ON s.IDProducto = p.IDProducto
        """).fetchall()
    finally:
        conexion.close()




