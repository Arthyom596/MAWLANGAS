from src.Modelo.Validaciones import validar_numero, obtener_fecha_exacta_actual
from src.DAO.VentasDAO import crear_venta
from src.DAO.InventarioDAO import obtener_cantidad_existente, descontar_producto
from src.DAO.FinanzaDAO import agregar_finanza
from src.DAO.SaboresDAO import obtener_sabores_por_producto  # Necesario para validar si tiene sabores

class Venta:
    def __init__(self):
        pass

    def realizar_venta(self, id_producto, id_sabor, cantidad_str, precio_unitario, nombre_producto, nombre_sabor):
        if id_producto is None:
            return False, "Producto no válido"

        # Validar cantidad como número positivo entero
        cantidad_valida, resultado = validar_numero(cantidad_str)
        if not cantidad_valida:
            return False, f"Cantidad inválida: {resultado}"

        cantidad = int(float(resultado))
        if cantidad <= 0:
            return False, "Ingrese una cantidad mayor a cero"

        fecha = obtener_fecha_exacta_actual()

        # VALIDACIÓN NUEVA: Verificar si el producto tiene sabores, pero el usuario no eligió uno
        lista_sabores = obtener_sabores_por_producto(id_producto)
        if lista_sabores and id_sabor is None:
            return False, "Error, Este producto tiene sabores"

        # Verificar inventario
        cantidad_disponible, _ = obtener_cantidad_existente(id_producto, id_sabor)
        if cantidad_disponible < cantidad:
            return False, f"No hay suficiente inventario. Disponible: {cantidad_disponible}"

        # Descontar del inventario
        descontar_producto(id_producto, id_sabor, cantidad, fecha)

        # Registrar en VentasDAO
        crear_venta(id_producto, id_sabor, cantidad, fecha)

        # Registrar en FinanzasDAO
        total = cantidad * precio_unitario
        descripcion = f"Venta de {cantidad} {nombre_producto} {nombre_sabor if id_sabor else ''}"
        agregar_finanza(fecha, "Venta", total, descripcion)

        return True, "Venta registrada exitosamente"
