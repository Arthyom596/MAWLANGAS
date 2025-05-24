import customtkinter as ctk
from tkinter import messagebox
from src.Controlador.RegistroControlador import registrar_usuario_controlador

class Registro:
    def __init__(self, parent, controlador_maestro):
        self.parent = parent
        self.controlador_maestro = controlador_maestro

        self.parent.configure(fg_color="black")
        self.contenedor = ctk.CTkFrame(self.parent, fg_color="white", corner_radius=10)
        self.frame = self.contenedor
        self.contenedor.pack(expand=True, fill="both", padx=100, pady=40)

        # Solo la columna 1 (inputs) tendrá peso para expandirse
        for i in range(10):
            self.contenedor.grid_rowconfigure(i, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=0)  # etiquetas no se expanden
        self.contenedor.grid_columnconfigure(1, weight=1)  # entradas sí se expanden

        self.etiqueta_registro = ctk.CTkLabel(
            self.contenedor, text="REGISTRO", text_color="black", font=("Arial", 20, "bold")
        )
        self.etiqueta_registro.grid(row=0, column=0, columnspan=2, pady=20, padx=20, sticky="nsew")

        self.campos = {}

        # Usuario
        usuario_label = ctk.CTkLabel(self.contenedor, text="Usuario", text_color="black", font=("Arial", 14))
        usuario_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        usuario_entry = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10, width=300)
        usuario_entry.grid(row=1, column=1, padx=20, pady=5, sticky="ew")
        self.campos["usuario"] = usuario_entry

        # Contraseña
        contrasena_label = ctk.CTkLabel(self.contenedor, text="Contraseña", text_color="black", font=("Arial", 14))
        contrasena_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        contrasena_entry = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10, show="*", width=300)
        contrasena_entry.grid(row=2, column=1, padx=20, pady=5, sticky="ew")
        self.campos["contrasena"] = contrasena_entry

        # Nombres
        nombre_label = ctk.CTkLabel(self.contenedor, text="Nombres", text_color="black", font=("Arial", 14))
        nombre_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        nombre_entry = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10, width=300)
        nombre_entry.grid(row=3, column=1, padx=20, pady=5, sticky="ew")
        self.campos["nombre"] = nombre_entry

        # Apellido Paterno
        apellido_p_label = ctk.CTkLabel(self.contenedor, text="Apellido Paterno", text_color="black", font=("Arial", 14))
        apellido_p_label.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        apellido_p_entry = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10, width=300)
        apellido_p_entry.grid(row=4, column=1, padx=20, pady=5, sticky="ew")
        self.campos["apellido_p"] = apellido_p_entry

        # Apellido Materno
        apellido_m_label = ctk.CTkLabel(self.contenedor, text="Apellido Materno", text_color="black", font=("Arial", 14))
        apellido_m_label.grid(row=5, column=0, padx=20, pady=5, sticky="w")
        apellido_m_entry = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10, width=300)
        apellido_m_entry.grid(row=5, column=1, padx=20, pady=5, sticky="ew")
        self.campos["apellido_m"] = apellido_m_entry

        # Correo Electrónico
        correo_label = ctk.CTkLabel(self.contenedor, text="Correo Electrónico", text_color="black", font=("Arial", 14))
        correo_label.grid(row=6, column=0, padx=20, pady=5, sticky="w")
        correo_entry = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10, width=300)
        correo_entry.grid(row=6, column=1, padx=20, pady=5, sticky="ew")
        self.campos["correo"] = correo_entry

        # Código OTP
        otp_label = ctk.CTkLabel(self.contenedor, text="Código OTP", text_color="black", font=("Arial", 14))
        otp_label.grid(row=7, column=0, padx=20, pady=5, sticky="w")
        otp_entry = ctk.CTkEntry(self.contenedor, border_width=1, corner_radius=10, width=300)
        otp_entry.grid(row=7, column=1, padx=20, pady=5, sticky="ew")
        self.campos["otp"] = otp_entry

        # Etiqueta dinámica
        self.etiqueta_dinamica = ctk.CTkLabel(
            self.contenedor, text="", text_color="black", font=("Arial", 14)
        )
        self.etiqueta_dinamica.grid(row=8, column=1, padx=20, pady=5, sticky="ew")

        # Botón enviar código
        self.boton_enviar_codigo = ctk.CTkButton(
            self.contenedor, text="Enviar código", corner_radius=10, command=self.enviar_codigo
        )
        self.boton_enviar_codigo.grid(row=8, column=1, pady=10, padx=10, sticky="ew")

        # Botón registrar
        self.boton_registrar = ctk.CTkButton(
            self.contenedor, text="Registrar", corner_radius=10, command=self.registrar
        )
        self.boton_registrar.grid(row=10, column=1, padx=20, pady=10, sticky="ew")

        # Botón Cancelar
        self.boton_cancelar = ctk.CTkButton(
            self.contenedor, text="Cancelar", corner_radius=10, command=self.cancelar
        )
        self.boton_cancelar.grid(row=10, column=0, pady=10, padx=10, sticky="ew")

    def enviar_codigo(self):
        from src.Modelo.Otp import manejar_otp
        correo = self.campos["correo"].get()
        manejar_otp(correo)

    def registrar(self):
        datos = {clave: campo.get() for clave, campo in self.campos.items()}
        exito, mensaje = registrar_usuario_controlador(datos)

        if exito:
            self.etiqueta_dinamica.configure(text="Registro exitoso ✅", text_color="green")
            messagebox.showinfo("Registro", mensaje)
            for campo in self.campos.values():
                campo.delete(0, "end")
        else:
            self.etiqueta_dinamica.configure(text=mensaje, text_color="red")
            messagebox.showerror("Error", mensaje)

    def cancelar(self):
        self.controlador_maestro.mostrar_login()

class ControladorMaestroFalso:
    def mostrar_login(self):
        print("Regresando al login")

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("850x650")
    root.title("Productos")

    falso_maestro = ControladorMaestroFalso()
    Registro(root, controlador_maestro=falso_maestro)

    root.mainloop()