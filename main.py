import tkinter as tk
import random

janela = tk.Tk()

estrelas = []

def explorar_planeta():
    pass

def entrar_botao(event):
    event.widget.config(bg='#2A2A2A')

def sair_botao(event):
    event.widget.config(bg=event.widget.cor_original)
   
janela.title("Blue Planet")
janela.geometry("900x600")
janela.configure(bg='#000000')

fundo = tk.Canvas(
    janela,
    bg="#000814",
    highlightthickness=0,
    bd=0
)

fundo.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1
)

def desenhar_fundo(event=None):
    fundo.delete("all")

    largura = janela.winfo_width()
    altura = janela.winfo_height()

    for y in range(altura):
        r = 0
        g = min(255, 15 + y // 18)
        b = min(255, 40 + y // 6)

        cor = f'#{r:02x}{g:02x}{b:02x}'

        fundo.create_line(
            0,
            y,
            largura,
            y,
            fill=cor
        )

    # Estrelas
    estrelas.clear()

    for _ in range(120):
        x = random.randint(0, largura)
        y = random.randint(0, altura)

        tamanho = random.choice([1,2])

        estrela = fundo.create_oval(
            x,
            y,
            x + tamanho,
            y + tamanho,
            fill="white",
            outline=""
        )

        estrelas.append({
            "id": estrela,
            "x": x,
            "y": y,
            "tamanho": tamanho,
            "vel": random.uniform(0.2, 0.7)
        })

def animar_estrelas():

    largura = janela.winfo_width()

    for estrela in estrelas:

        estrela["x"] -= estrela["vel"]

        if estrela["x"] < 0:
            estrela["x"] = largura

        fundo.coords(
            estrela["id"],
            estrela["x"],
            estrela["y"],
            estrela["x"] + estrela["tamanho"],
            estrela["y"] + estrela["tamanho"]
        )

janela.after(30, animar_estrelas)

janela.bind("<Configure>", desenhar_fundo)
desenhar_fundo()

container = tk.Frame(
    janela,
    bg='#111111',
    padx=40,
    pady=40
)

header = tk.Frame(
    janela,
    bg="#0A0A0A",
    height=55
)

header.pack(fill="x")

logo = tk.Label(
    header,
    text="Blue Planet",
    font=("Montserrat", 14, "bold"),
    bg="#0A0A0A",
    fg="#FFFFFF"
)

logo.pack(side="left", padx=20, pady=12)

container.place(
    relx=0.5,
    rely=0.56,
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

botao.cor_original = '#1E88E5'

botao.pack(pady=(50, 0))

botao.bind('<Enter>', entrar_botao)
botao.bind('<Leave>', sair_botao)

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

botao_paises.cor_original = '#1A1A1A'

botao_paises.pack(pady=(15, 0))

botao_paises.bind('<Enter>', entrar_botao)
botao_paises.bind('<Leave>', sair_botao)

janela.mainloop()