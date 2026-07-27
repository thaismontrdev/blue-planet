from ursina import *

app = Ursina()

window.title = 'Blue Planet - Protótipo 3D'
window.color = color.black

globo = Entity(
    model='sphere',
    texture='../assets/earth1.jpg',
    scale=2,
)

editor_camera = EditorCamera()

VELOCIDADE_ROTACAO = 10

def update():
    globo.rotation_y += VELOCIDADE_ROTACAO * time.dt

app.run()