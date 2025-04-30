from src.Logica.Validaciones import validar_texto, validar_numero
from src.Modelos.Productos import crear_producto, obtener_ultimo_producto, buscar_producto
from src.Modelos.Sabores import crear_sabor

def agregar_sabor(sabor, sabores_lista, lista_sabores_widget=None):
    valido, resultado = validar_texto(sabor)
    if not valido:
        return sabores_lista, resultado

    sabor_validado = resultado.strip().capitalize()
    sabores_lista.append(sabor_validado)

    if lista_sabores_widget:
        lista_sabores_widget.insert("end", f"{sabor_validado}\n")

    return sabores_lista, "Sabor agregado correctamente"


def eliminar_ultimo_sabor(sabores, textbox):
    sabores = list(sabores)  # Asegurar que sea lista, no tupla

    if sabores:
        sabores.pop()
        textbox.delete("0.0", "end")
        textbox.insert("0.0", "Sabores añadidos:\n" + "\n".join(sabores))

    return sabores

def guardar_producto(nombre, precio_compra, precio_venta, sabores):
    # Validar nombre
    nombre_valido, resultado_nombre = validar_texto(nombre)
    if not nombre_valido:
        return False, resultado_nombre
    nombre_limpio = resultado_nombre.strip().capitalize()

    # Verificar si ya existe
    if buscar_producto(nombre_limpio):
        return False, f"El producto {nombre_limpio} ya existe"

    # Validar precios como números
    pc_valido, resultado_pc = validar_numero(precio_compra)
    if not pc_valido:
        return False, resultado_pc

    pv_valido, resultado_pv = validar_numero(precio_venta)
    if not pv_valido:
        return False, resultado_pv

    if resultado_pv <= resultado_pc:
        return False, "El precio de venta debe ser mayor al precio de compra"

    # Crear producto en la base de datos
    crear_producto(nombre_limpio, resultado_pc, resultado_pv)

    # Verificar si se creó correctamente
    id_producto = obtener_ultimo_producto()
    if not id_producto:
        return False, f"El producto {nombre_limpio} no fue creado correctamente"

    # Guardar sabores
    for sabor in sabores:
        crear_sabor(id_producto, sabor.strip().capitalize())

    return True, "Producto guardado correctamente"
