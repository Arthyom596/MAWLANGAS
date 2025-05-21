import customtkinter as ctk
from tkinter import ttk

class ConsultaProducto:
    def __init__(self, root):
        self.app = root
        self.app.geometry("850x650")
        self.app.title("Consultar Producto")
        self.app.configure(fg_color="#bec752")

        for col in (0, 1, 2, 3):
            app.columnconfigure(col, weight=1)

        for row in (0, 1, 2, 3, 4, 5):
            app.rowconfigure(row, weight=1)

        self.consulta = ctk.CTkLabel(self.app,text="Consulta de Productos",font=("Arial",30,"bold"),text_color="black")
        self.consulta.grid(column=2,row=0,sticky="w",padx=80, pady=5)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 15, "bold"))

        # --- Treeview ---
        self.tree = ttk.Treeview(self.app, columns=("ID", "Producto", "P. Compra", "P. Venta"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("P. Compra", text="P. Compra")
        self.tree.heading("P. Venta", text="P. Venta")

        # Opcional: ancho de columnas
        self.tree.column("ID", width=100)
        self.tree.column("Producto", width=200)
        self.tree.column("P. Compra", width=100)
        self.tree.column("P. Venta", width=100)

        self.tree.grid(row=1, column=0, columnspan=4, rowspan=5, padx=20, pady=20, sticky="nsew")

if __name__ == "__main__":
    app = ctk.CTk()
    vista = ConsultaProducto(app)
    app.mainloop()