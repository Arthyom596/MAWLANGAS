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
            IDSabor INTEGER,  -- PERMITE NULL
            Cantidad INTEGER NOT NULL,
            FechaActualizacion TEXT NOT NULL,
            Usuario TEXT NOT NULL,
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
def crear_inventario(id_producto, id_sabor, cantidad, fecha_actualizacion, usuario):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            INSERT INTO Inventario (IDProducto, IDSabor, Cantidad, FechaActualizacion, Usuario)
            VALUES (?, ?, ?, ?, ?)
        """, (id_producto, id_sabor, cantidad, fecha_actualizacion, usuario))
        conexion.commit()
        print("Inventario creado correctamente.")
    except sqlite3.IntegrityError:
        print("Error: No se pudo crear el inventario (posible clave duplicada o conflicto).")
    finally:
        conexion.close()
# Obtener inventarios
def obtener_inventario_completo():
    conexion = conectar()
    if not conexion:
        return []

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT 
                i.IDInventario,
                p.Nombre,           -- Nombre del producto
                s.NombreSabor,      -- Nombre del sabor (puede ser NULL)
                i.Cantidad,
                i.FechaActualizacion,
                i.Usuario           -- ← Aquí se obtiene el usuario
            FROM Inventario i
            JOIN Productos p ON i.IDProducto = p.IDProducto
            LEFT JOIN Sabores s ON i.IDSabor = s.IDSabor
        """)
        return cursor.fetchall()
    finally:
        conexion.close()




# Actualizar inventario
def actualizar_inventario(id_inventario, id_producto, id_sabor, cantidad, fecha_actualizacion, usuario):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            UPDATE Inventario
            SET IDProducto = ?, IDSabor = ?, Cantidad = ?, FechaActualizacion = ?, Usuario = ?
            WHERE IDInventario = ?
        """, (id_producto, id_sabor, cantidad, fecha_actualizacion, usuario, id_inventario))
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



# Obtener cantidad existente y IDInventario para un producto y sabor
def obtener_cantidad_existente(id_producto, id_sabor):
    conexion = conectar()
    if not conexion:
        return 0, None
    try:
        if id_sabor is None:
            resultado = conexion.execute("""
                SELECT Cantidad, IDInventario FROM Inventario
                WHERE IDProducto = ? AND IDSabor IS NULL
            """, (id_producto,)).fetchone()
        else:
            resultado = conexion.execute("""
                SELECT Cantidad, IDInventario FROM Inventario
                WHERE IDProducto = ? AND IDSabor = ?
            """, (id_producto, id_sabor)).fetchone()
        if resultado:
            return resultado[0], resultado[1]
        else:
            return 0, None
    finally:
        conexion.close()

# Descontar producto del inventario
# Descontar producto del inventario
def descontar_producto(id_producto, id_sabor, cantidad_a_descontar, fecha_actualizacion, usuario):
    conexion = conectar()
    if not conexion:
        return False
    try:
        cantidad_actual, id_inventario = obtener_cantidad_existente(id_producto, id_sabor)

        if id_inventario is None:
            print("No existe inventario para este producto y sabor.")
            return False

        if cantidad_actual < cantidad_a_descontar:
            print("No hay suficiente inventario para realizar la venta.")
            return False

        nueva_cantidad = cantidad_actual - cantidad_a_descontar

        conexion.execute("""
            UPDATE Inventario
            SET Cantidad = ?, FechaActualizacion = ?, Usuario = ?
            WHERE IDInventario = ?
        """, (nueva_cantidad, fecha_actualizacion, usuario, id_inventario))

        conexion.commit()
        print("Inventario actualizado correctamente.")
        return True
    except sqlite3.Error as e:
        print(f"Error al descontar producto del inventario: {e}")
        return False
    finally:
        conexion.close()


