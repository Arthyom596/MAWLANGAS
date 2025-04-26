import customtkinter as ctk
from src.Interfaces.Login import Login



# Inicialización de la ventana principal
if __name__ == "__main__":
    root = ctk.CTk()
    app = Login(root)
    root.mainloop()

