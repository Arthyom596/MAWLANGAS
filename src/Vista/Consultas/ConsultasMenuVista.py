from pathlib import Path

import customtkinter as ctk
from PIL import Image

class ConsultasMenuVista:
    def __init__(self, root):
        self.app = root
        self.app.geometry("850x650")
        self.app.title("Menu")
        self.app.configure(fg_color="white")
        ruta_imagen = Path(__file__).resolve().parent.parent.parent / "assets" / "Cat.png"
        imagen_gato_pequeno = ctk.CTkImage(Image.open(ruta_imagen), size=(120, 120))


        for col in (0, 1, 2, 3):
            self.app.columnconfigure(col, weight=1)

        for row in (0, 1, 2, 3, 4, 5):
            self.app.rowconfigure(row, weight=1)
        #FRAME SUPERIOR
        self.frame_superior = ctk.CTkFrame(self.app,width=850, height=20,fg_color="#1a1e30",border_width=5,border_color="white")
        self.frame_superior.grid(row=0, column=0, sticky="ew")
        self.frame_superior.grid_propagate(True)

        self.mawlangas = ctk.CTkLabel(self.frame_superior, text="CONSULTAS", text_color="white", font=("Forte Normal", 60, "bold"))
        self.mawlangas.grid(row=0, column=2, padx=60, pady=10)

        self.label_imagen1 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen1.grid(row=0, column=0, padx=35, pady=10, sticky="w")

        self.label_imagen2 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen2.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.label_imagen1 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen1.grid(row=0, column=0, padx=35, pady=10, sticky="w")

        self.label_imagen2 = ctk.CTkLabel(self.frame_superior, image=imagen_gato_pequeno, text="")
        self.label_imagen2.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.bienvenido = ctk.CTkLabel(self.app,text="¡Bienvenido a Consultas!\n Aqui podrás manejar todas las opciones"
                                                     " del programa.",font=("Arial", 20, "bold"))

        self.bienvenido.grid(row=1, column=0, padx=20, sticky="n")
        #FRAME INFERIOR QUE CONTIENE LOS BOTONES
        self.frame_inferior = ctk.CTkFrame(self.app,width=700,height=400,border_width=5,border_color="#1a1e30",
                                           fg_color="white")
        self.frame_inferior.grid(row=3, column=0)
        self.frame_inferior.grid_propagate(False)

        for col in (0, 1, 2, 3):
            self.frame_inferior.columnconfigure(col, weight=1)

        for row in (0, 1, 2, 3, 4, 5):
            self.frame_inferior.rowconfigure(row, weight=1)

        self.botton_inventario = ctk.CTkButton(self.frame_inferior,text="Inventario",text_color="white",font=("Arial", 25, "bold"),fg_color="#1017ed",
                                               height=50,width=150,hover_color="#080b68",corner_radius=100)
        self.botton_inventario.grid(row=0, column=0,sticky="nsew",padx=20,pady=10,columnspan=4)

        self.botton_finanzas = ctk.CTkButton(self.frame_inferior, text="Finanzas", text_color="white",
                                               font=("Arial", 25, "bold"), fg_color="#09ca15",
                                               height=50, width=150, hover_color="#07730e",corner_radius=100)
        self.botton_finanzas.grid(row=1, column=0,sticky="nsew",padx=20,pady=10,columnspan=4)

        self.botton_productos = ctk.CTkButton(self.frame_inferior, text="Productos", text_color="white",
                                             font=("Arial", 25, "bold"), fg_color="#e3f316",
                                             height=50, width=150, hover_color="#9ea90f",corner_radius=100)
        self.botton_productos.grid(row=2, column=0,sticky="nsew",padx=20,pady=10,columnspan=4)

        self.botton_usuarios = ctk.CTkButton(self.frame_inferior, text="Usuarios", text_color="white",
                                               font=("Arial", 25, "bold"), fg_color="#8f13f0",
                                               height=50, width=150, hover_color="#410471", corner_radius=100)
        self.botton_usuarios.grid(row=3, column=0,sticky="nsew",padx=20,pady=10,columnspan=4)

        self.botton_sabores = ctk.CTkButton(self.frame_inferior, text="Sabores", text_color="white",
                                             font=("Arial", 25, "bold"), fg_color="#f32727",
                                             height=50, width=150, hover_color="#8c0c0c", corner_radius=100)
        self.botton_sabores.grid(row=4, column=0,sticky="nsew",padx=20,pady=10,columnspan=4)

if __name__ == "__main__":
    app = ctk.CTk()
    vista = ConsultasMenuVista(app)
    app.mainloop()