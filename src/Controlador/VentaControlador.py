from src.Modelo.Venta import Venta as ModeloVenta
from src.DAO.ProductosDAO import obtener_productos_id_nombre, obtener_productos_completos
from src.DAO.SaboresDAO import obtener_sabores_por_producto, obtener_id_sabor
from src.DAO.InventarioDAO import obtener_cantidad_existente


class ControladorVenta:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = ModeloVenta()

        # Configurar el botón de la vista
        self.vista.boton_venta.configure(command=self.crear_venta)

        # Cargar productos y sabores cuando se inicie el controlador
        self.cargar_productos()
        self.vista.combo_productos.bind("<<ComboboxSelected>>", self.actualizar_sabores)

    def cargar_productos(self):
        productos = obtener_productos_id_nombre()
        print(f"[DEBUG] Productos cargados: {productos}")

        self.vista.productos_dict = {producto[1]: producto[0] for producto in productos}
        nombres = [producto[1] for producto in productos]
        self.vista.combo_productos.configure(values=nombres)

        # Limpiar la lista de sabores al cargar productos
        self.vista.combo_sabor.configure(values=[], state="disabled")
        self.vista.sabores_dict = {}

    def actualizar_sabores(self, event=None):
        producto_seleccionado = self.vista.combo_productos.get()
        print(f"[DEBUG] Producto seleccionado: {producto_seleccionado}")

        id_producto = self.obtener_id_producto()
        print(f"[DEBUG] ID del producto seleccionado: {id_producto}")

        if id_producto:
            sabores = obtener_sabores_por_producto(id_producto)
            print(f"[DEBUG] Sabores obtenidos desde la base de datos: {sabores}")

            if sabores:
                self.vista.combo_sabor.configure(state="readonly")
                self.vista.sabores_dict = {sabor[1]: sabor[0] for sabor in sabores}
                nombres = [sabor[1] for sabor in sabores]
                self.vista.combo_sabor.configure(values=nombres)
                self.vista.combo_sabor.set("Sabor")
            else:
                self.vista.combo_sabor.configure(state="disabled")
                self.vista.combo_sabor.set("Sin sabor")
                self.vista.sabores_dict = {}
        else:
            print("[DEBUG] No se seleccionó un producto válido.")

    def obtener_id_producto(self):
        seleccionado = self.vista.combo_productos.get()
        return self.vista.productos_dict.get(seleccionado)

    def obtener_id_sabor(self):
        nombre_sabor = self.vista.combo_sabor.get()
        if nombre_sabor in ["", "Sabor", None, "Sin sabor"]:
            return None
        id_producto = self.obtener_id_producto()
        return obtener_id_sabor(nombre_sabor, id_producto)

    def crear_venta(self):
        nombre_producto = self.vista.combo_productos.get()
        nombre_sabor = self.vista.combo_sabor.get() if self.vista.combo_sabor.cget("state") != "disabled" else "Sin sabor"
        cantidad_str = self.vista.entrada_cantidad.get()

        if not cantidad_str.isdigit() or int(cantidad_str) <= 0:
            self.vista.etiqueta_dinamica.configure(text="Ingrese una cantidad válida", text_color="red")
            return

        cantidad = int(cantidad_str)

        if nombre_producto == "Producto":
            self.vista.etiqueta_dinamica.configure(text="Seleccione un producto", text_color="red")
            return

        id_producto = self.obtener_id_producto()
        id_sabor = self.obtener_id_sabor()

        if id_producto is None:
            self.vista.etiqueta_dinamica.configure(text="Producto no válido", text_color="red")
            return

        cantidad_disponible, _ = obtener_cantidad_existente(id_producto, id_sabor)
        if cantidad_disponible < cantidad:
            self.vista.etiqueta_dinamica.configure(
                text=f"Inventario insuficiente. Disponible: {cantidad_disponible}", text_color="red"
            )
            return

        producto = next((prod for prod in obtener_productos_completos() if prod[0] == id_producto), None)

        if producto:
            precio_unitario = producto[2]
        else:
            self.vista.etiqueta_dinamica.configure(text="Error al obtener precio", text_color="red")
            return

        exito, mensaje, *_ = self.modelo.realizar_venta(
            id_producto, id_sabor, cantidad, precio_unitario, nombre_producto, nombre_sabor
        )

        self.vista.etiqueta_dinamica.configure(text=mensaje, text_color="green" if exito else "red")

        if exito:
            self.vista.entrada_cantidad.delete(0, "end")
            self.vista.combo_productos.set("Producto")
            self.vista.combo_sabor.set("Sabor")
            self.vista.combo_sabor.configure(state="disabled")
            self.vista.etiqueta_dinamica.configure(text="", text_color="white")
