import customtkinter as ctk
from tkinter import ttk

class ConsultaSabor:
    def __init__(self, root):
        self.app = root
        self.app.geometry("850x650")
        self.app.title("Consultar Sabor")
        self.app.configure(fg_color="#69d3a8")

        for col in (0, 1, 2, 3):
            app.columnconfigure(col, weight=1)

        for row in (0, 1, 2, 3, 4, 5):
            app.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(self.app,text="Consulta de Sabores",font=("Arial",30,"bold"),text_color="black")
        self.consulta.grid(column=2,row=0,sticky="w",padx=80, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"))

        # --- Treeview ---
        self.tree = ttk.Treeview(self.app, columns=("ID Sabor", "ID Producto", "Nombre del Sabor"), show="headings")
        self.tree.heading("ID Sabor", text="ID Sabor")
        self.tree.heading("ID Producto", text="ID Producto")
        self.tree.heading("Nombre del Sabor", text="Nombre del Sabor")

        # Opcional: ancho de columnas
        self.tree.column("ID Sabor", width=100)
        self.tree.column("ID Producto", width=200)
        self.tree.column("Nombre del Sabor", width=100)

        self.tree.grid(row=1, column=0, columnspan=4, rowspan=5, padx=20, pady=20, sticky="nsew")

if __name__ == "__main__":
    app = ctk.CTk()
    vista = ConsultaSabor(app)
    app.mainloop()