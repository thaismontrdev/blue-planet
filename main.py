import tkinter as tk

janela = tk.Tk()

def explorar_planeta():
    pass

janela.title("Blue Planet")
janela.geometry("900x600")
janela.configure(bg='#000000')

container = tk.Frame(
    janela,
    bg='#111111',
    padx=40,
    pady=40
)

container.place(
    relx=0.5,
    rely=0.5,
    anchor='center'
)

container.configure(
    highlightbackground='#222222',
    highlightthickness=2
)

titulo = tk.Label(
    container,
    text="Blue Planet",
    font=("Montserrat", 28, "bold"),
    bg='#111111',
    fg='#FFFFFF'
)

titulo.pack(pady=(0, 5))

subtitulo = tk.Label(
    container,
    text="Explore our world",
    font=("Montserrat", 12, 'italic'),
    bg="#111111",
    fg="#7A7A7A"
)

subtitulo.pack(pady=(0, 25))

planeta = tk.Canvas(
    container,
    width=260,
    height=260,
    bg='#111111',
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
    container,
    text="Explorar o Planeta",
    font=("Montserrat", 13, "bold"),
    width=24,
    height=2,
    bg='#1E88E5',
    fg='#FFFFFF',
    activebackground='#1565C0',
    activeforeground='#FFFFFF',
    relief='flat',
    padx=20,
    pady=10,
    cursor='hand2',
    command=explorar_planeta,
)

botao.pack(pady=(50, 0))

botao_paises = tk.Button(
    container,
    text='Países',
    font=('Montserrat', 11),
    width=24,
    bg='#1A1A1A',
    fg='#FFFFFF',
    activebackground='#2A2A2A',
    activeforeground='#FFFFFF',
    relief='flat',
    padx=20,
    pady=8,
    cursor='hand2'
)

botao_paises.pack(pady=(15, 0))

janela.mainloop()