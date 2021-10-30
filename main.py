from ursina import *
from ursina import texture
from ursina.prefabs.first_person_controller import FirstPersonController
from tqdm import tqdm

global ch
global ls
ch = 0
ls = ['dirt.png','cobblestone.png','bricks.png','dark_oak_planks.png','mossy_stone_bricks.png','prismarine_bricks.png','quartz_pillar_top.png','red_sandstone_bottom.png','red_nether_bricks.png']

def update():
    global ch
    if held_keys['1']: ch = 0
    if held_keys['2']: ch = 1
    if held_keys['3']: ch = 2
    if held_keys['4']: ch = 3
    if held_keys['5']: ch = 4
    if held_keys['6']: ch = 5
    if held_keys['7']: ch = 6
    if held_keys['8']: ch = 7
    if held_keys['9']: ch = 8

class Voxel(Button):
    def __init__(self,position = (0,0,0)):
        super().__init__(
            parent = scene,
            model  = 'cube',
            position = position,
            origin_y = 0.5,
            color = color.white,
            highlight_color = color.light_gray,
            texture = 'textures/'+ls[ch]
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            if key == 'left mouse down':
                destroy(self)


app = Ursina()

for i in tqdm(range(25)):
    for j in range(25):
        voxel = Voxel(position = (i,0,j))

player = FirstPersonController()

window.borderless = False
window.exit_button.visible = False
app.run()
