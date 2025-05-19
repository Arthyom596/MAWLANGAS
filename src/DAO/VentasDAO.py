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
        # Tabla Ventas (IDSabor ahora permite NULL)
        conexion.execute("""
        CREATE TABLE IF NOT EXISTS Ventas(
            IDVenta INTEGER PRIMARY KEY AUTOINCREMENT,
            IDProducto INTEGER NOT NULL,
            IDSabor INTEGER,  -- Aquí se eliminó NOT NULL
            CantidadVendida INTEGER NOT NULL,
            Fecha TEXT NOT NULL,
            FOREIGN KEY (IDProducto) REFERENCES Productos(IDProducto) ON DELETE CASCADE,
            FOREIGN KEY (IDSabor) REFERENCES Sabores(IDSabor) ON DELETE CASCADE
        );
        """)
        conexion.commit()
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Crear una venta
def crear_venta(id_producto, id_sabor, cantidad_vendida, fecha):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO Ventas(IDProducto, IDSabor, CantidadVendida, Fecha)
            VALUES (?, ?, ?, ?)
        """, (id_producto, id_sabor if id_sabor is not None else None, cantidad_vendida, fecha))
        conexion.commit()
        print("Venta registrada correctamente.")
    except sqlite3.IntegrityError:
        print("Error: No se pudo registrar la venta (clave foránea inválida o conflicto).")
    finally:
        conexion.close()

# Obtener todas las ventas
def obtener_ventas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Ventas")
    ventas = cursor.fetchall()
    conexion.close()
    return ventas



