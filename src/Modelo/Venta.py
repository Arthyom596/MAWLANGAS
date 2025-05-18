from src.Modelo.Validaciones import validar_numero, obtener_fecha_exacta_actual
from src.DAO.VentasDAO import crear_venta
from src.DAO.InventarioDAO import obtener_cantidad_existente, descontar_producto
from src.DAO.FinanzaDAO import agregar_finanza


class Venta:
    def __init__(self):
        pass

    def realizar_venta(self, id_producto, id_sabor, cantidad, precio_unitario, nombre_producto, nombre_sabor):
        # Validar cantidad como número positivo
        cantidad_valida, resultado = validar_numero(cantidad)
        if not cantidad_valida:
            return False, resultado

        cantidad = int(cantidad)
        fecha = obtener_fecha_exacta_actual()

        # Si el id_sabor es None, asignar None
        if id_sabor is None:
            id_sabor = None

        # Obtener cantidad disponible desde InventarioDAO
        cantidad_disponible, _ = obtener_cantidad_existente(id_producto, id_sabor)
        if cantidad_disponible < cantidad:
            return False, f"No hay suficiente inventario. Disponible: {cantidad_disponible}"

        # Descontar del inventario
        descontar_producto(id_producto, id_sabor, cantidad, fecha)

        # Registrar en VentasDAO
        total = cantidad * precio_unitario
        crear_venta(id_producto, id_sabor, cantidad, fecha)

        # Registrar en FinanzasDAO
        descripcion = f"Venta de {cantidad} {nombre_producto} {nombre_sabor if id_sabor else ''}"
        agregar_finanza(fecha, "Venta", total, descripcion)

        return True, "Venta registrada exitosamente"
