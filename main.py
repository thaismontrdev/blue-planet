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

planeta = tk.Canvas(
    janela,
    width=260,
    height=260,
    bg='#000000',
    highlightthickness=0
)

planeta.pack()

planeta.create_oval(
    10,
    10,
    250,
    250,
    fill='#0D47A1',
    outline=''
)

planeta.create_oval(
    20,
    20,
    240,
    240,
    fill='#1565C0',
    outline=''
)

planeta.create_oval(
    40,
    40,
    220,
    220,
    fill='#1E88E5',
    outline='#42A5F5',
    width=3
)

planeta.create_oval(
    75,
    80,
    120,
    120,
    fill='#43A047',
    outline=''
)

planeta.create_oval(
    135,
    95,
    175,
    145,
    fill='#43A047',
    outline=''
)

planeta.create_oval(
    95,
    145,
    140,
    180,
    fill='#43A047',
    outline=''
)

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