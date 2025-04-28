import sqlite3
import os

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
        CREATE TABLE IF NOT EXISTS Inventario(
            IDInventario INTEGER PRIMARY KEY AUTOINCREMENT,
            IDProducto INTEGER NOT NULL,
            IDSabor INTEGER NOT NULL,
            Cantidad INTEGER NOT NULL,
            FechaActualizacion TEXT NOT NULL,
            FOREIGN KEY(IDProducto) REFERENCES Productos(IDProducto) ON DELETE CASCADE,
            FOREIGN KEY(IDSabor) REFERENCES Sabores(IDSabor) ON DELETE CASCADE
        );
        """)
        conexion.commit()
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Crear inventario
def crear_inventario(id_producto, id_sabor, cantidad, fecha_actualizacion):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
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
    if not conexion:
        return []
    try:
        return conexion.execute("SELECT * FROM Inventario").fetchall()
    finally:
        conexion.close()

# Actualizar inventario
def actualizar_inventario(id_inventario, id_producto, id_sabor, cantidad, fecha_actualizacion):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            UPDATE Inventario
            SET IDProducto = ?, IDSabor = ?, Cantidad = ?, FechaActualizacion = ?
            WHERE IDInventario = ?
        """, (id_producto, id_sabor, cantidad, fecha_actualizacion, id_inventario))
        conexion.commit()
    finally:
        conexion.close()

# Eliminar inventario
def eliminar_inventario(id_inventario):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("DELETE FROM Inventario WHERE IDInventario = ?", (id_inventario,))
        conexion.commit()
    finally:
        conexion.close()

