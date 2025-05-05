
from src.Modelo.Producto import agregar_sabor, eliminar_ultimo_sabor, guardar_producto

class ProductoControlador:
    def __init__(self, vista): #El constructor espera a ProductoVista como parametro
        self.vista = vista #Se crea una instancia de ProductosVista
        self.sabores = [] #Se crea una lista vacia para los sabores

    def agregar_sabor(self, sabor):
        self.sabores, mensaje = agregar_sabor(sabor, self.sabores) #espera el retorno del true o el msj de error
        self.vista.mostrar_mensaje(mensaje) #Hace que la etiqueta dinamica muestre el mensaje
        self.vista.actualizar_textbox_sabores(self.sabores) #Actualiza el texbox mandando la lista de sabores
        self.vista.limpiar_entry_sabor() #Limpia la entrada
        self.vista.actualizar_estado_boton(self.sabores) #Activa los botones

    def eliminar_sabor(self):
        self.sabores = eliminar_ultimo_sabor(self.sabores)  #Elimina el ultimo sabor agregado
        self.vista.mostrar_mensaje("Último sabor eliminado.") #Cambia la etiqueta dinamica
        self.vista.actualizar_textbox_sabores(self.sabores) #Actualiza la textbox con los nuevos sabores
        self.vista.actualizar_estado_boton(self.sabores) #Actualiza el estado para ver si sigue on u off

    def guardar_producto(self, nombre, precio_compra, precio_venta, usar_sabores):
        sabores_a_guardar = self.sabores if usar_sabores else []  # Si se usa el switch, guarda los sabores, si no, manda lista vacia

        if not nombre.strip():  # Si el campo nombre esta vacio, manda mensaje y no continua
            self.vista.mostrar_mensaje("El nombre no puede estar vacio")
            return

        exito, mensaje = guardar_producto(nombre, precio_compra, precio_venta,
                                          sabores_a_guardar)  # Guarda el producto con o sin sabores
        self.vista.mostrar_mensaje(mensaje)  # Muestra el mensaje de confirmacion o error

        if exito:  # Si se guardo correctamente, limpia los contenedores
            self.sabores.clear()  # Vacía la lista de sabores
            self.vista.reiniciar_formulario()  # Reinicia el formulario
            self.vista.actualizar_textbox_sabores(self.sabores)  # Limpia el textbox
            self.vista.actualizar_estado_boton(self.sabores)  # Desactiva los botones si es necesario
