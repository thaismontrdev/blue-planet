import tkinter as tk

janela = tk.Tk()

janela.title("Blue Planet")
janela.geometry("900x600")
janela.configure(bg='#000000')

titulo = tk.Label(
    janela,
    text="Blue Planet",
    font=("Arial", 24, "bold"),
    bg='#000000',
    fg='#FFFFFF'
)

titulo.pack(pady=20)

botao = tk.Button(
    janela,
    text="Explorar o Planeta",
    font=("Arial", 16),
    bg='#121212',
    fg='#FFFFFF',
    activebackground='#1E1E1E',
    activeforeground='#FFFFFF',
    relief='flat',
    padx=15,
    pady=8
)

botao.pack(pady=10)

janela.mainloop()