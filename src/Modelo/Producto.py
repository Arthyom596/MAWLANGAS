
from src.Modelo.Validaciones import validar_texto, validar_numero
from src.DAO.ProductosDAO import crear_producto, obtener_ultimo_producto, buscar_producto
from src.DAO.SaboresDAO import crear_sabor

"""
Esta clase se encarga de conectar la vista con el modelo. Recibe las acciones del usuario desde 
la interfaz (vista) y decide qué hacer con ellas, usando las funciones del modelo para procesar 
la información.

El controlador valida, actualiza y devuelve respuestas a la vista usando los metodos del modelo
como mensajes o cambios en la interfaz. También manda a llamar la lógica 
para agregar, eliminar o guardar sabores, asegurando que el 
usuario vea siempre una interfaz actualizada y funcionando correctamente
"""


#Este metodo espera recibir un sabor y la lista de la interfaz
def agregar_sabor(sabor, sabores_lista):
    valido, resultado = validar_texto(sabor) #Valida el texto del sabor
    if not valido: #Si no devuelve true en "valido" se retorna la lista vacia y el mensaje de error
        return sabores_lista, resultado
    #El valor de resultado se le pasa a sabor valido
    sabor_validado = resultado.strip().capitalize() #Se limpia de espacios y se inicia en mayuscula
    sabores_lista.append(sabor_validado) #Se agrega a la lista

    return sabores_lista, "Sabor agregado correctamente" #Retorna la lista y el mensaje de exito

def eliminar_ultimo_sabor(sabores): #Se recibe la lista de sabores del controlador
    sabores = list(sabores)
    if sabores: #Verifica que la lista no este vacia
        sabores.pop() #Elimina el ultimo elemento
    return sabores #Retorna la nueva lista

def guardar_producto(nombre, precio_compra, precio_venta, sabores):
    nombre_valido, resultado_nombre = validar_texto(nombre) #Si el nombre es valido continua el flujo
    if not nombre_valido:
        return False, resultado_nombre #Retorno en caso de error al validar nombre
    #el resultado se limpia y se pone la primera letra mayuscula
    nombre_limpio = resultado_nombre.strip().capitalize()
    #Si el producto ya existe retorna false y un mensaje de error
    if buscar_producto(nombre_limpio):
        return False, f"El producto {nombre_limpio} ya existe"
    #Se valida el precio de compra si es valido continua el flujo
    pc_valido, resultado_pc = validar_numero(precio_compra)
    if not pc_valido:
        return False, resultado_pc #Si el precio de compra es invalido retorna el error
    # Se valida el precio de venta si es valido continua el flujo
    pv_valido, resultado_pv = validar_numero(precio_venta)
    if not pv_valido:
        return False, resultado_pv #Si el precio de venta es invalido retorna el error

    if resultado_pv <= resultado_pc: #Si el precio de venta es menor que el de compra retorna false
        return False, "El precio de venta debe ser mayor al precio de compra"
    #Finalmente si las entradas pasas todas las validaciones se manda a llamar
    # el metodo del DAO para insertarlo en la base de datos
    crear_producto(nombre_limpio, resultado_pc, resultado_pv)
    #Se obtiene el id del ultimo producto agregado (el de arriba)
    id_producto = obtener_ultimo_producto()
    if not id_producto: #Si no lo encuentra retorna False
        return False, f"El producto {nombre_limpio} no fue creado correctamente"
    #Mediante un bucle se añaden los sabores a la tabla con su nuevo formato
    for sabor in sabores:
        crear_sabor(id_producto, sabor.strip().capitalize())

    return True, "Producto guardado correctamente"
