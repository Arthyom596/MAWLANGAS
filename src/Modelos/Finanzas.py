
import sqlite3


name_bd="Mawlangas.bd"

def conectar():
    conexion = sqlite3.connect(name_bd)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion

def agregar_finanza(fecha,tipo,monto,descripcion):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""INSERT INTO Finanzas(Fecha,Tipo,Monto,Descripcion)
        VALUES(?,?,?,?)""",(fecha,tipo,monto,descripcion))
        conexion.commit()
    except sqlite3.IntegrityError:
        print("El registro no existe")
    finally:
        conexion.close()

def consultar_finanzas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Finanzas")
    ventas=cursor.fetchall()
    conexion.close()
    return ventas

#Por integridad no se permite modificar ni eliminar finanzas

