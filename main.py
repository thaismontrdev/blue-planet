import tkinter as tk

janela = tk.Tk()

janela.title("Blue Planet")
janela.geometry("900x600")

titulo = tk.Label(
    janela,
    text="Blue Planet",
    font=("Arial", 24, "bold"),
)

titulo.pack(pady=20)

janela.mainloop()