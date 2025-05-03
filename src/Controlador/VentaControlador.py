from src.Modelo.Venta import Venta as ModeloVenta
from src.DAO.ProductosDAO import obtener_productos_id_nombre,obtener_productos_completos
from src.DAO.SaboresDAO import obtener_sabores_por_producto, obtener_id_sabor
from src.DAO.InventarioDAO import obtener_cantidad_existente


class ControladorVenta:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = ModeloVenta()

        # Configurar el botón de la vista
        self.vista.boton_venta.configure(command=self.realizar_venta)

        # Cargar productos y sabores cuando se inicie el controlador
        self.cargar_productos()
        self.vista.combo_productos.bind("<<ComboboxSelected>>", self.cargar_sabores)

    def cargar_productos(self):
        productos = obtener_productos_id_nombre()
        print(f"[DEBUG] Productos cargados: {productos}")  # <--- Agrega esto

        self.vista.productos_dict = {producto[1]: producto[0] for producto in productos}
        nombres = [producto[1] for producto in productos]
        self.vista.combo_productos.configure(values=nombres)

    def cargar_sabores(self, event=None):
        print("[DEBUG] cargar_sabores fue llamado")  # <- LÍNEA CLAVE AGREGADA

        id_producto = self.obtener_id_producto()
        print(f"[DEBUG] ID del producto seleccionado: {id_producto}")  # <--- Ya estaba bien

        if id_producto:
            sabores = obtener_sabores_por_producto(id_producto)
            print(f"[DEBUG] Sabores obtenidos desde la base de datos: {sabores}")

            self.vista.sabores_dict = {sabor[1]: sabor[0] for sabor in sabores}
            nombres = [sabor[1] for sabor in sabores]
            self.vista.combo_sabor.configure(values=nombres)
        else:
            print("[DEBUG] No se seleccionó un producto válido.")

    def obtener_id_producto(self):
        # Obtener ID del producto seleccionado
        seleccionado = self.vista.combo_productos.get()
        return self.vista.productos_dict.get(seleccionado)

    def obtener_id_sabor(self):
        # Obtener ID del sabor seleccionado
        nombre_sabor = self.vista.combo_sabor.get()
        id_producto = self.obtener_id_producto()
        return obtener_id_sabor(nombre_sabor, id_producto)

    def realizar_venta(self):
        # Obtener datos de la vista
        nombre_producto = self.vista.combo_productos.get()
        nombre_sabor = self.vista.combo_sabor.get()
        cantidad = self.vista.entrada_cantidad.get()

        # Verificar que se haya seleccionado un producto y un sabor
        if nombre_producto == "Producto" or nombre_sabor == "Sabor":
            self.vista.etiqueta_dinamica.configure(text="Seleccione producto y sabor")
            return

        # Obtener ID del producto y sabor
        id_producto = self.obtener_id_producto()
        id_sabor = self.obtener_id_sabor()

        # Verificar si el producto y sabor son válidos
        if id_producto is None or id_sabor is None:
            self.vista.etiqueta_dinamica.configure(text="Producto o sabor no válido", text_color="red")
            return

        # Verificar disponibilidad en inventario
        cantidad_disponible, _ = obtener_cantidad_existente(id_producto, id_sabor)
        if cantidad_disponible < int(cantidad):
            self.vista.etiqueta_dinamica.configure(text=f"Inventario insuficiente. Disponible: {cantidad_disponible}",
                                                   text_color="red")
            return

        # Obtener precio del producto
        producto = next((prod for prod in obtener_productos_completos() if prod[0] == id_producto), None)

        if producto:
            precio_unitario = producto[2]  # PrecioVenta es el tercer valor en la tupla
        else:
            self.vista.etiqueta_dinamica.configure(text="Error al obtener precio", text_color="red")
            return

        # Realizar la venta usando el modelo

        exito, mensaje, *_ = self.modelo.realizar_venta(
            id_producto, id_sabor, cantidad, precio_unitario, nombre_producto, nombre_sabor
        )

        # Actualizar mensaje de la venta
        self.vista.etiqueta_dinamica.configure(text=mensaje, text_color="green" if exito else "red")

        # Si la venta fue exitosa, limpiar los campos
        if exito:
            self.vista.entrada_cantidad.delete(0, "end")
            self.vista.combo_productos.set("Producto")
            self.vista.combo_sabor.set("Sabor")
