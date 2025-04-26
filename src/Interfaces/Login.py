import customtkinter as ctk
from PIL import Image
from pathlib import Path


class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("800x600")

        ctk.set_appearance_mode("dark")

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        self.contenedor_visual = ctk.CTkFrame(self.master, fg_color="#1E1E1E", corner_radius=0)
        self.contenedor_visual.grid(row=0, column=0, sticky="nsew")
        self.contenedor_visual.grid_columnconfigure(0, weight=1)
        self.contenedor_visual.grid_rowconfigure((0, 1), weight=1)

        ruta_imagen = Path(__file__).resolve().parent.parent.parent / "assets" / "Cat.png"
        imagen_gato = ctk.CTkImage(Image.open(ruta_imagen), size=(300, 300))

        self.imagen_label = ctk.CTkLabel(self.contenedor_visual, image=imagen_gato, text="")
        self.imagen_label.grid(row=0, column=0, pady=(60, 10))

        self.texto_mawlangas = ctk.CTkLabel(self.contenedor_visual, text="Mawlangas", font=("Arial", 30, "bold"),
                                            text_color="white")
        self.texto_mawlangas.grid(row=1, column=0)

        self.contenedor_datos1 = ctk.CTkFrame(self.master, fg_color="#1E1E1E", corner_radius=0)
        self.contenedor_datos1.grid(row=0, column=1, sticky="nsew")
        self.contenedor_datos1.grid_rowconfigure(0, weight=1)
        self.contenedor_datos1.grid_columnconfigure(0, weight=1)

        self.contenedor_datos2 = ctk.CTkFrame(self.contenedor_datos1, fg_color="white", corner_radius=10)
        self.contenedor_datos2.grid(row=0, column=0, padx=20, pady=60, sticky="nsew")

        for i in range(7):
            self.contenedor_datos2.grid_rowconfigure(i, weight=1)
        self.contenedor_datos2.grid_columnconfigure(0, weight=1)

        self.login_label = ctk.CTkLabel(self.contenedor_datos2, text="LOGIN", text_color="#1E1E1E",
                                        font=("Arial", 20, "bold"))
        self.login_label.grid(row=0, column=0, pady=(20, 10), sticky="w", padx=20)

        self.user_entry = ctk.CTkEntry(self.contenedor_datos2, placeholder_text="USER", border_width=1, corner_radius=0)
        self.user_entry.grid(row=1, column=0, padx=20, sticky="ew")

        self.password_entry = ctk.CTkEntry(self.contenedor_datos2, placeholder_text="PASSWORD", border_width=1,
                                           corner_radius=0, show="*")
        self.password_entry.grid(row=2, column=0, padx=20, sticky="ew")

        self.login_button = ctk.CTkButton(self.contenedor_datos2, text="LOGIN", fg_color="white", text_color="black",
                                          hover_color="#e6e6e6", border_width=1, border_color="black", corner_radius=10)
        self.login_button.grid(row=3, column=0, pady=(10, 0), padx=60)

        self.register_button = ctk.CTkButton(self.contenedor_datos2, text="REGISTER", fg_color="white",
                                             text_color="black",
                                             hover_color="#e6e6e6", border_width=1, border_color="black",
                                             corner_radius=10)
        self.register_button.grid(row=4, column=0, pady=10, padx=60)

        self.remember_checkbox = ctk.CTkCheckBox(self.contenedor_datos2, text="REMEMBER ME", text_color="black",
                                                 checkbox_height=15, checkbox_width=15)
        self.remember_checkbox.grid(row=5, column=0, sticky="w", padx=20)


# Inicialización de la ventana
if __name__ == "__main__":
    root = ctk.CTk()
    app = Login(root)
    root.mainloop()
