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
        # Tabla Ventas
        conexion.execute("""
        CREATE TABLE IF NOT EXISTS Ventas(
            IDVenta INTEGER PRIMARY KEY AUTOINCREMENT,
            Fecha TEXT NOT NULL,
            IDProducto INTEGER NOT NULL,
            IDSabor INTEGER NOT NULL,
            CantidadVendida INTEGER NOT NULL,
            Preparado BOOLEAN NOT NULL,
            PrecioVenta INTEGER NOT NULL,
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

# Obtener todas las ventas
def obtener_ventas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Ventas")
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

# No se pueden modificar las ventas por integridad

# No se pueden eliminar ventas por integridad
