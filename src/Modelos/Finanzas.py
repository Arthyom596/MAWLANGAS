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
        # Tabla Finanzas
        conexion.execute("""
        CREATE TABLE IF NOT EXISTS Finanzas(
            IDFinanza INTEGER PRIMARY KEY AUTOINCREMENT,
            Fecha TEXT NOT NULL,
            Tipo TEXT NOT NULL,
            Monto REAL NOT NULL,
            Descripcion TEXT NOT NULL
        );
        """)
        conexion.commit()
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Agregar una finanza
def agregar_finanza(fecha, tipo, monto, descripcion):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO Finanzas(Fecha, Tipo, Monto, Descripcion)
            VALUES(?, ?, ?, ?)
        """, (fecha, tipo, monto, descripcion))
        conexion.commit()
        print("Finanza registrada correctamente.")
    except sqlite3.IntegrityError:
        print("Error: El registro no existe o clave duplicada.")
    finally:
        conexion.close()

# Consultar finanzas
def consultar_finanzas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Finanzas")
    finanzas = cursor.fetchall()
    conexion.close()
    return finanzas

# No se pueden modificar ni eliminar finanzas por integridad
