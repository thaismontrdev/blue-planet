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

botao = tk.Button(
    janela,
    text="Explorar o Planeta",
    font=("Arial", 16),
)

botao.pack(pady=10)

janela.mainloop()