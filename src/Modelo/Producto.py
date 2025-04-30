# src/Modelo/Producto.py

from src.Modelo.Validaciones import validar_texto, validar_numero
from src.DAO.ProductosDAO import crear_producto, obtener_ultimo_producto, buscar_producto
from src.DAO.SaboresDAO import crear_sabor

def agregar_sabor(sabor, sabores_lista):
    valido, resultado = validar_texto(sabor)
    if not valido:
        return sabores_lista, resultado

    sabor_validado = resultado.strip().capitalize()
    sabores_lista.append(sabor_validado)

    return sabores_lista, "Sabor agregado correctamente"

def eliminar_ultimo_sabor(sabores):
    sabores = list(sabores)
    if sabores:
        sabores.pop()
    return sabores

def guardar_producto(nombre, precio_compra, precio_venta, sabores):
    nombre_valido, resultado_nombre = validar_texto(nombre)
    if not nombre_valido:
        return False, resultado_nombre
    nombre_limpio = resultado_nombre.strip().capitalize()

    if buscar_producto(nombre_limpio):
        return False, f"El producto {nombre_limpio} ya existe"

    pc_valido, resultado_pc = validar_numero(precio_compra)
    if not pc_valido:
        return False, resultado_pc

    pv_valido, resultado_pv = validar_numero(precio_venta)
    if not pv_valido:
        return False, resultado_pv

    if resultado_pv <= resultado_pc:
        return False, "El precio de venta debe ser mayor al precio de compra"

    crear_producto(nombre_limpio, resultado_pc, resultado_pv)

    id_producto = obtener_ultimo_producto()
    if not id_producto:
        return False, f"El producto {nombre_limpio} no fue creado correctamente"

    for sabor in sabores:
        crear_sabor(id_producto, sabor.strip().capitalize())

    return True, "Producto guardado correctamente"
