from ursina import *

app = Ursina()

window.title = 'Blue Planet - Protótipo 3D'
window.color = color.black
globo = Entity(
    model='sphere',
    color=color.azure,
    scale=2,
)

editor_camera = EditorCamera()

app.run()