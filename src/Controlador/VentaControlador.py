from src.Modelo.Venta import Venta as ModeloVenta
from src.DAO.ProductosDAO import obtener_productos_id_nombre, obtener_productos_completos
from src.DAO.SaboresDAO import obtener_sabores_por_producto, obtener_id_sabor
from src.Modelo.Validaciones import validar_texto

class ControladorVenta:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = ModeloVenta()

        # Configurar evento de selección en combo productos para actualizar sabores
        self.vista.combo_productos.bind("<<ComboboxSelected>>", self.actualizar_sabores)

        # Configurar botón venta
        self.vista.boton_venta.configure(command=self.crear_venta)

        self.cargar_productos()

    def cargar_productos(self):
        productos = obtener_productos_id_nombre()
        self.vista.productos_dict = {nombre: id_ for id_, nombre in productos}
        self.vista.combo_productos.configure(values=list(self.vista.productos_dict.keys()))
        print(f"[DEBUG] Productos cargados: {self.vista.productos_dict}")

        self.vista.combo_sabor.set("Sabor")
        self.vista.combo_sabor.configure(values=[], state="normal")
        self.vista.sabores_dict = {}

    def actualizar_sabores(self, event=None):
        id_producto = self.obtener_id_producto()
        print(f"[DEBUG] Producto seleccionado: {id_producto}")
        if id_producto is None:
            print("[DEBUG] No se seleccionó producto válido.")
            return

        sabores = obtener_sabores_por_producto(id_producto)
        print(f"[DEBUG] Sabores obtenidos: {sabores}")

        if sabores:
            self.vista.combo_sabor.configure(state="normal")
            self.vista.combo_sabor.configure(values=[s[1] for s in sabores])
            self.vista.sabores_dict = {nombre: id_ for id_, nombre in sabores}
            self.vista.switch_sabor.configure(state="normal")
            self.vista.switch_sabor.select()
        else:
            self.vista.combo_sabor.configure(state="disabled")
            self.vista.combo_sabor.set("Sin sabor")
            self.vista.sabores_dict = {}
            self.vista.switch_sabor.deselect()
            self.vista.switch_sabor.configure(state="disabled")
        print(f"[DEBUG] Sabores dict actualizado: {self.vista.sabores_dict}")

    def obtener_id_producto(self):
        nombre = self.vista.combo_productos.get()
        id_producto = self.vista.productos_dict.get(nombre)
        print(f"[DEBUG] obtener_id_producto: {nombre} -> {id_producto}")
        return id_producto

    def obtener_id_sabor(self):
        nombre_sabor = self.vista.combo_sabor.get()
        if nombre_sabor in ["", "Sabor", None, "Sin sabor"]:
            print("[DEBUG] No se seleccionó sabor válido.")
            return None
        id_sabor = self.vista.sabores_dict.get(nombre_sabor)
        print(f"[DEBUG] obtener_id_sabor: {nombre_sabor} -> {id_sabor}")
        return id_sabor

    def obtener_precio_producto(self, id_producto):
        productos = obtener_productos_completos()
        for producto in productos:
            if producto[0] == id_producto:
                print(f"[DEBUG] Precio encontrado para producto {id_producto}: {producto[2]}")
                return producto[2]
        print(f"[DEBUG] No se encontró precio para producto {id_producto}")
        return None

    def crear_venta(self):
        print("[DEBUG] Intentando crear venta...")
        nombre_producto = self.vista.combo_productos.get()
        cantidad_str = self.vista.entrada_cantidad.get()
        nombre_sabor = self.vista.combo_sabor.get() if self.vista.combo_sabor.cget("state") != "disabled" else "Sin sabor"

        # Validaciones
        valido, mensaje = validar_texto(nombre_producto)
        if not valido or nombre_producto == "Producto":
            self.vista.etiqueta_dinamica.configure(text=f"Producto inválido: {mensaje}", text_color="red")
            print(f"[ERROR] Producto inválido: {mensaje}")
            return

        if not cantidad_str.strip():
            self.vista.etiqueta_dinamica.configure(text="Ingrese cantidad", text_color="red")
            print("[ERROR] Cantidad vacía")
            return

        id_producto = self.obtener_id_producto()
        id_sabor = self.obtener_id_sabor()
        precio_unitario = self.obtener_precio_producto(id_producto)

        if precio_unitario is None:
            self.vista.etiqueta_dinamica.configure(text="Error al obtener precio", text_color="red")
            print("[ERROR] Precio unitario es None")
            return

        exito, resultado = self.modelo.realizar_venta(
            id_producto, id_sabor, cantidad_str, precio_unitario, nombre_producto, nombre_sabor
        )

        self.vista.etiqueta_dinamica.configure(
            text=resultado,
            text_color="green" if exito else "red"
        )

        print(f"[DEBUG] Resultado venta: {resultado}, Éxito: {exito}")

        if exito:
            self.vista.entrada_cantidad.delete(0, "end")
            self.vista.combo_productos.set("Producto")
            self.vista.combo_sabor.set("Sabor")
            self.vista.combo_sabor.configure(state="disabled")
