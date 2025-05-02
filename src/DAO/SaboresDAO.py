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
            NombreSabor TEXT NOT NULL,
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




