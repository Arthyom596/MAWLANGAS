import sqlite3

name_bd = "Mawlangas.db"
conexion = sqlite3.connect(name_bd)
cursor = conexion.cursor()



# Tabla de usuarios
cursor.execute("""
CREATE TABLE Usuarios(
    IDUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
    Usuario TEXT UNIQUE NOT NULL,
    Contrasena TEXT NOT NULL,
    Nombre TEXT NOT NULL,
    ApellidoPaterno TEXT NOT NULL,
    ApellidoMaterno TEXT,
    Correo TEXT NOT NULL
);
""")

# Tabla productos
cursor.execute("""
CREATE TABLE Productos (
    IDProducto INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    PrecioCompra REAL NOT NULL,
    PrecioVenta REAL NOT NULL
);
""")

# Tabla Sabores
cursor.execute("""
CREATE TABLE Sabores (
    IDSabor INTEGER PRIMARY KEY AUTOINCREMENT,
    IDProducto INTEGER NOT NULL,
    NombreSabor TEXT NOT NULL,
    FOREIGN KEY (IDProducto) REFERENCES Productos(IDProducto) ON DELETE CASCADE
);
""")

# Tabla Inventario
cursor.execute("""
CREATE TABLE Inventario(
    IDInventario INTEGER PRIMARY KEY AUTOINCREMENT,
    IDProducto INTEGER NOT NULL,
    IDSabor INTEGER NOT NULL,
    Cantidad INTEGER NOT NULL,
    FechaActualizacion TEXT NOT NULL,
    FOREIGN KEY(IDProducto) REFERENCES Productos(IDProducto) ON DELETE CASCADE,
    FOREIGN KEY(IDSabor) REFERENCES Sabores(IDSabor) ON DELETE CASCADE
);
""")

# Tabla Ventas
cursor.execute("""
CREATE TABLE Ventas(
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

# Tabla Finanzas
cursor.execute("""
CREATE TABLE Finanzas(
    IDFinanza INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha TEXT NOT NULL,
    Tipo TEXT NOT NULL,
    Monto REAL NOT NULL,
    Descripcion TEXT NOT NULL
);
""")

# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()

