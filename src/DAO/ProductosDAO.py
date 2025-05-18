import os
import sqlite3

"""
Esta clase tiene como proposito centralizar todos los metodos de interaccion con la base de datos
relacionados con la tabla de productos. Aqui se implementan tanto la creación de la tabla como
las operaciones CRUD (crear, leer, actualizar, eliminar), incluyendo variantes específicas según
los requerimientos del sistema. Esta clase es la única responsable de acceder directamente a la
base de datos para garantizar el encapsulamiento y la separación de responsabilidades.
"""





# Ruta del proyecto y base de datos
proyecto_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ruta_db = os.path.join(proyecto_base, 'BaseDatos') #Crea la ruta absoluta donde se almacenara la bd
os.makedirs(ruta_db, exist_ok=True) #Crea la ruta si es que esta no existe
nombre_bd = os.path.join(ruta_db, 'Mawlangas.db')  #construye la ruta completa del archivo de la base de datos Mawlangas.bd


def conectar():
    try:
        conexion = sqlite3.connect(nombre_bd) #Establece la conexion con Mawlangas.bd
        conexion.execute("PRAGMA foreign_keys = ON") #Activa las llaves foraneas por si acaso
        conexion.execute("""  
            CREATE TABLE IF NOT EXISTS Productos(
                IDProducto INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT NOT NULL,
                PrecioCompra REAL NOT NULL,
                PrecioVenta REAL NOT NULL
            ); 
        """)#Crea la tabla Productos si esta no existe con todas sus especificaciones
        conexion.commit() #Guarda los cambios
        return conexion #Devuelve la conexion para que se pueda usar en otro apartado
    except sqlite3.Error as e: #Captura cualquier error y retorna false para que no truene
        print(f"Error al conectar a la base de datos: {e}")
        return None

#El metodo para crear cualquier producto espera 3 argumentos
def crear_producto(nombre, precio_compra, precio_venta):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            INSERT INTO Productos (Nombre, PrecioCompra, PrecioVenta)
            VALUES (?, ?, ?)
        """, (nombre, precio_compra, precio_venta)) #Crea el producto y lo agrega a la bd
        conexion.commit() #Guarda Cambios
    finally:
        conexion.close()#Cierra la conexion




#El metodo para actualizar producto espera 4 argumentos
def actualizar_producto(id_producto, nombre, precio_compra, precio_venta):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("""
            UPDATE Productos
            SET Nombre = ?, PrecioCompra = ?, PrecioVenta = ?
            WHERE IDProducto = ?
        """, (nombre, precio_compra, precio_venta, id_producto))
        #Se pasan los valores a los placeholder y se reemplazan los viejos por los nuevos
        conexion.commit() #Se guardan los cambios
    finally:
        conexion.close()#Se cierra la conexion



def eliminar_producto(id_producto):
    conexion = conectar()
    if not conexion:
        return
    try:
        conexion.execute("DELETE FROM Productos WHERE IDProducto = ?", (id_producto,))
        #Ejecuta un DELETE que elimina un producto de la tabla Productos cuyo IDProducto coincide
        conexion.commit()
    finally:
        conexion.close()


# Espera como parametro el nombre del producto que se desea buscar en la base de datos
def buscar_producto(nombre_producto):
    conexion = conectar()
    if not conexion:
        return None
    try:
        result = conexion.execute("SELECT * FROM Productos WHERE Nombre = ?", (nombre_producto,)).fetchone()
        #Ejecuta un SELECT que busca en la tabla productos un registro cuyo nombre coincida con el parametro
        return result
    finally:
        conexion.close()


def obtener_ultimo_producto():
    conexion = conectar()
    try:
        #Selecciona el campo de IDproducto de la tabla,los ordena desde el mas reciente y solo toma el primer res.
        resultado = conexion.execute("SELECT IDProducto FROM Productos ORDER BY IDProducto DESC LIMIT 1").fetchone()
        if resultado:
            #Retorna el id si encuentra el ultimo producto
            return resultado[0]
        else:
            return None #Se devuelve None si la tabla de productos esta vacia
    finally:
        conexion.close() #Se cierra la conexion

def obtener_productos_id_nombre():
    conexion = conectar()
    if not conexion:
        return [] #Si la conexion falla retorna una lista vacia
    try:
        #Ejecuta un SELECT que selecciona las columnas IDProducto y Nombre de todos los registros
        return conexion.execute("SELECT IDProducto, Nombre FROM Productos").fetchall()
    finally:
        conexion.close() #Cierra la conexion

def obtener_productos_completos():
    conexion = conectar()
    cursor = conexion.cursor()
    #Selecciona 3 columnas de la tabla
    cursor.execute("SELECT IDProducto, Nombre, PrecioVenta FROM Productos")
    productos = cursor.fetchall() #Lo convierte en una lista de tuplas
    conexion.close() #Cierra la conexion
    return productos #Retorna la lista

def obtener_productos_consulta():
    conexion = conectar()
    if not conexion:
        return [] #Si no encuentra la conexion retorna una lista vacia
    try:
        #Recupera todos los datos de la tabla y los manda en forma de lista de tuplas
        return conexion.execute("SELECT * FROM Productos").fetchall()
    finally:
        conexion.close()#Cierra la conexion

def obtener_precio_compra(id_producto):
    conexion = conectar()
    if not conexion:
        return None
    try:
        resultado = conexion.execute("""
            SELECT PrecioCompra FROM Productos WHERE IDProducto = ?
        """, (id_producto,)).fetchone()
        return resultado[0] if resultado else None
    finally:
        conexion.close()

def obtener_nombre_producto_por_id(id_producto):
    conexion = conectar()
    if not conexion:
        return None
    try:
        resultado = conexion.execute("""
            SELECT Nombre FROM Productos WHERE IDProducto = ?
        """, (id_producto,)).fetchone()
        return resultado[0] if resultado else None
    finally:
        conexion.close()




