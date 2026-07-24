import tkinter as tk

janela = tk.Tk()

janela.title("Blue Planet")
janela.geometry("900x600")
janela.configure(bg='#000000')

titulo = tk.Label(
    janela,
    text="Blue Planet",
    font=("Segoe UI", 28, "bold"),
    bg='#000000',
    fg='#FFFFFF'
)

titulo.pack(pady=(35, 5))

subtitulo = tk.Label(
    janela,
    text="Explore our world",
    font=("Segoe UI", 12, 'italic'),
    bg="#000000",
    fg="#7A7A7A"
)

subtitulo.pack(pady=(0, 40))

botao = tk.Button(
    janela,
    text="Explorar o Planeta",
    font=("Segoe UI", 13, "bold"),
    bg='#121212',
    fg='#FFFFFF',
    activebackground='#1E1E1E',
    activeforeground='#FFFFFF',
    relief='flat',
    padx=20,
    pady=10,
    cursor='hand2'
)

botao.pack()

janela.mainloop()