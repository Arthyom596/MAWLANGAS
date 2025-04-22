import customtkinter as ctk

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("800x600")
app.title("Eliminar")

for i in range(3):
    app.grid_columnconfigure(i, weight=1)
for i in range(7):
    app.grid_rowconfigure(i, weight=1)

etiqueta_titulo = ctk.CTkLabel(app, text="Eliminar", font=("Arial", 36, "bold"), text_color="white")
etiqueta_titulo.grid(row=0, column=0, columnspan=3, pady=20, sticky="nsew")

etiqueta_subtitulo = ctk.CTkLabel(app, text="En proceso", font=("Arial", 18, "bold"), text_color="white")
etiqueta_subtitulo.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")


app.mainloop()