# src/Controlador/InventarioControlador.py
from src.Modelo.Inventario import Inventario

class InventarioControlador:
    def __init__(self, vista):
        self.vista = vista
        self.vista.set_controlador(self)
        self.productos = Inventario.obtener_productos()
        self.vista.set_productos(self.productos)

    def obtener_id_producto(self):
        seleccionado = self.vista.combo_producto.get()
        return self.vista.productos_dict.get(seleccionado)

    def actualizar_sabores(self, _=None):
        id_producto = self.obtener_id_producto()
        if id_producto is not None:
            sabores = Inventario.obtener_sabores(id_producto)
            self.vista.set_sabores(sabores)

            tiene_sabores = bool(sabores)
            self.vista.habilitar_sabores(tiene_sabores)

            # Cambiar estado del switch automáticamente
            if tiene_sabores:
                self.vista.switch_usar_sabor.configure(state="normal")  # Habilita el switch
                self.vista.switch_usar_sabor.select()  # Activa el switch (encendido por defecto)
            else:
                self.vista.switch_usar_sabor.deselect()  # Apaga el switch
                self.vista.switch_usar_sabor.configure(
                    state="disabled")  # Deshabilita el switch para que no lo activen manualmente

    def agregar_producto(self):
        id_producto = self.obtener_id_producto()
        cantidad = self.obtener_cantidad(self.vista.entrada_cantidad_agregar.get())
        id_sabor = None

        # Obtener sabores actuales para validar
        sabores = Inventario.obtener_sabores(id_producto)
        tiene_sabores = bool(sabores)

        # Validación: si el producto tiene sabores, pero el switch está desactivado (no usar sabor), bloquear
        if tiene_sabores and not self.vista.switch_usar_sabor.get():
            self.vista.mostrar_mensaje("Debe seleccionar un sabor para este producto.", "red")
            return

        # Si el switch está activo, obtener el sabor seleccionado
        if self.vista.switch_usar_sabor.get():
            nombre_sabor = self.vista.combo_sabores_agregar.get()
            id_sabor = self.vista.sabores_dict.get(nombre_sabor)
            if id_sabor is None:
                self.vista.mostrar_mensaje("Error: Seleccione un sabor válido.", "red")
                return

        if id_producto is None or cantidad is None:
            self.vista.mostrar_mensaje("Faltan datos", "red")
            return

        modelo = Inventario(id_producto, id_sabor, cantidad)
        ok, mensaje = modelo.actualizar()
        if not ok:
            ok, mensaje = modelo.guardar()

        self.vista.mostrar_mensaje(mensaje, "green" if ok else "red")
        if ok:
            self.vista.resetear_campos()

    def mermar_producto(self):
        id_producto = self.obtener_id_producto()
        cantidad = self.obtener_cantidad(self.vista.entrada_cantidad_mermar.get())
        id_sabor = None

        # Obtener sabores actuales para validar
        sabores = Inventario.obtener_sabores(id_producto)
        tiene_sabores = bool(sabores)

        # Validación: si el producto tiene sabores, pero el switch está desactivado, bloquear
        if tiene_sabores and not self.vista.switch_usar_sabor.get():
            self.vista.mostrar_mensaje("Debe seleccionar un sabor para este producto.", "red")
            return

        # Si el switch está activo, obtener sabor seleccionado
        if self.vista.switch_usar_sabor.get():
            nombre_sabor = self.vista.combo_sabores_mermar.get()
            id_sabor = self.vista.sabores_dict.get(nombre_sabor)
            if id_sabor is None:
                self.vista.mostrar_mensaje("Error: Campos inválidos", "red")
                return

        if id_producto is None or cantidad is None:
            self.vista.mostrar_mensaje("Faltan datos", "red")
            return

        modelo = Inventario(id_producto, id_sabor, cantidad)
        ok, mensaje = modelo.mermar_cantidad()

        self.vista.mostrar_mensaje(mensaje, "green" if ok else "red")
        if ok:
            self.vista.resetear_campos()

    def obtener_cantidad(self, entrada: str):
        try:
            return int(entrada)
        except ValueError:
            return None
