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
VELOCIDADE_MOUSE = 100

def update():
    globo.rotation_y += VELOCIDADE_ROTACAO * time.dt

    if mouse.left:
        globo.rotation_y -= mouse.velocity[0] * VELOCIDADE_MOUSE
        globo.rotation_x += mouse.velocity[1] * VELOCIDADE_MOUSE

app.run()