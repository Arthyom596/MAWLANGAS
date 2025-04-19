import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("800x600")
app.title("Consultas")

for i in range(3):
    app.columnconfigure(i, weight=1)

for i in range(4):
    app.rowconfigure(i, weight=1)

etiqueta_consultas=ctk.CTkLabel(app,text="Consultas",font=("Helvetica", 36, "bold"),text_color="white")
etiqueta_consultas.grid(row=0, column=1,sticky="nsew")

btn_inventario=ctk.CTkButton(app,text="Inventario")
btn_inventario.grid(row=1, column=0)


btn_finanzas=ctk.CTkButton(app,text="Finanzas")
btn_finanzas.grid(row=1, column=2)



app.mainloop()