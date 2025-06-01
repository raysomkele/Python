import ursina
from ursina import *
from ursina import texture
from ursina.prefabs import button
from ursina.prefabs.first_person_controller \
    import FirstPersonController


app = Ursina()
Sky()
mountains = Terrain(heightmap='mountains', skip=4)
player = FirstPersonController()
camera.position = (0, 5, -10)
terrain = Entity(model='mountains',
                 scale=(20,4,20),
                 texture='white_box',
                 )


def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt
    player.y += held_keys['w'] * time.dt
    player.y -= held_keys['s'] * time.dt

app.run()
