import customtkinter as ctk
from PIL import Image
from pathlib import Path

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x600")
app.title("Login")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

contenedor_visual = ctk.CTkFrame(app, fg_color="#1E1E1E", corner_radius=0)
contenedor_visual.grid(row=0, column=0, sticky="nsew")
contenedor_visual.grid_columnconfigure(0, weight=1)
contenedor_visual.grid_rowconfigure((0, 1), weight=1)

ruta_imagen = Path(__file__).resolve().parent.parent.parent / "assets" / "Cat.png"
imagen_gato = ctk.CTkImage(Image.open(ruta_imagen), size=(300, 300))

imagen_label = ctk.CTkLabel(contenedor_visual, image=imagen_gato, text="")
imagen_label.grid(row=0, column=0, pady=(60, 10))

texto_mawlangas = ctk.CTkLabel(contenedor_visual, text="Mawlangas", font=("Arial", 30, "bold"), text_color="white")
texto_mawlangas.grid(row=1, column=0)

contenedor_datos1 = ctk.CTkFrame(app, fg_color="#1E1E1E", corner_radius=0)
contenedor_datos1.grid(row=0, column=1, sticky="nsew")
contenedor_datos1.grid_rowconfigure(0, weight=1)
contenedor_datos1.grid_columnconfigure(0, weight=1)

contenedor_datos2 = ctk.CTkFrame(contenedor_datos1, fg_color="white", corner_radius=10)
contenedor_datos2.grid(row=0, column=0, padx=20, pady=60, sticky="nsew")

for i in range(7):
    contenedor_datos2.grid_rowconfigure(i, weight=1)
contenedor_datos2.grid_columnconfigure(0, weight=1)

login_label = ctk.CTkLabel(contenedor_datos2, text="LOGIN", text_color="#1E1E1E", font=("Arial", 20, "bold"))
login_label.grid(row=0, column=0, pady=(20, 10), sticky="w", padx=20)

user_entry = ctk.CTkEntry(contenedor_datos2, placeholder_text="USER", border_width=1, corner_radius=0)
user_entry.grid(row=1, column=0, padx=20, sticky="ew")

password_entry = ctk.CTkEntry(contenedor_datos2, placeholder_text="PASSWORD", border_width=1, corner_radius=0, show="*")
password_entry.grid(row=2, column=0, padx=20, sticky="ew")

login_button = ctk.CTkButton(contenedor_datos2, text="LOGIN", fg_color="white", text_color="black",
                             hover_color="#e6e6e6", border_width=1, border_color="black", corner_radius=10)
login_button.grid(row=3, column=0, pady=(10, 0), padx=60)

register_button = ctk.CTkButton(contenedor_datos2, text="REGISTER", fg_color="white", text_color="black",
                                hover_color="#e6e6e6", border_width=1, border_color="black", corner_radius=10)
register_button.grid(row=4, column=0, pady=10, padx=60)

remember_checkbox = ctk.CTkCheckBox(contenedor_datos2, text="REMEMBER ME", text_color="black", checkbox_height=15, checkbox_width=15)
remember_checkbox.grid(row=5, column=0, sticky="w", padx=20)

app.mainloop()
