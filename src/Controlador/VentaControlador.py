from src.Modelo.Venta import Venta as ModeloVenta
from src.DAO.ProductosDAO import obtener_productos_id_nombre, obtener_productos_completos
from src.DAO.SaboresDAO import obtener_sabores_por_producto, obtener_id_sabor
from src.DAO.InventarioDAO import obtener_cantidad_existente
from src.Modelo.Validaciones import validar_texto

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
        self.vista.productos_dict = {producto[1]: producto[0] for producto in productos}
        nombres = [producto[1] for producto in productos]
        self.vista.combo_productos.configure(values=nombres)

        # Limpiar la lista de sabores al cargar productos
        self.vista.combo_sabor.configure(values=[], state="disabled")
        self.vista.sabores_dict = {}

    def actualizar_sabores(self, event=None):
        id_producto = self.obtener_id_producto()

        if id_producto:
            sabores = obtener_sabores_por_producto(id_producto)
            if sabores:
                self.vista.combo_sabor.configure(state="normal")
                self.vista.combo_sabor.set("")
                self.vista.combo_sabor.configure(values=[sabor[1] for sabor in sabores])
                self.vista.combo_sabor.configure(state="readonly")
                self.vista.combo_sabor.set("Sabor")
                self.vista.sabores_dict = {sabor[1]: sabor[0] for sabor in sabores}

                self.vista.switch_sabor.configure(state="normal")
                self.vista.switch_sabor.select()
            else:
                self.vista.combo_sabor.configure(state="disabled")
                self.vista.combo_sabor.set("Sin sabor")
                self.vista.sabores_dict = {}

                self.vista.switch_sabor.deselect()
                self.vista.switch_sabor.configure(state="disabled")
        else:
            print("No se seleccionó un producto válido.")

    def obtener_id_producto(self):
        seleccionado = self.vista.combo_productos.get()
        return self.vista.productos_dict.get(seleccionado)

    def obtener_id_sabor(self):
        nombre_sabor = self.vista.combo_sabor.get()
        if nombre_sabor in ["", "Sabor", None, "Sin sabor"]:
            return None
        id_producto = self.obtener_id_producto()
        return obtener_id_sabor(nombre_sabor, id_producto)

    def obtener_precio_producto(self, id_producto):
        producto = next((prod for prod in obtener_productos_completos() if prod[0] == id_producto), None)
        if producto:
            return producto[2]
        return None

    def crear_venta(self):
        nombre_producto = self.vista.combo_productos.get()
        cantidad_str = self.vista.entrada_cantidad.get()
        nombre_sabor = self.vista.combo_sabor.get() if self.vista.combo_sabor.cget("state") != "disabled" else "Sin sabor"


        valido, resultado = validar_texto(nombre_producto)
        if not valido or nombre_producto == "Producto":
            self.vista.etiqueta_dinamica.configure(text=f"Producto inválido: {resultado}", text_color="red")
            return

        if not cantidad_str.strip():
            self.vista.etiqueta_dinamica.configure(text="Ingrese cantidad", text_color="red")
            return

        id_producto = self.obtener_id_producto()
        id_sabor = self.obtener_id_sabor()

        precio_unitario = self.obtener_precio_producto(id_producto)
        if precio_unitario is None:
            self.vista.etiqueta_dinamica.configure(text="Error al obtener precio", text_color="red")
            return


        exito, mensaje = self.modelo.realizar_venta(
            id_producto, id_sabor, cantidad_str, precio_unitario, nombre_producto, nombre_sabor
        )

        self.vista.etiqueta_dinamica.configure(text=mensaje, text_color="green" if exito else "red")

        if exito:
            # Limpiar campos tras venta exitosa
            self.vista.entrada_cantidad.delete(0, "end")
            self.vista.combo_productos.set("Producto")
            self.vista.combo_sabor.set("Sabor")
            self.vista.combo_sabor.configure(state="disabled")
