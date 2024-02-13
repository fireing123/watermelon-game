from pygame_phyics import StaticObject as _Static
from pygame_phyics import Manger

class DeathLine(_Static):
    def __init__(self, name, layer, tag, visible, position, rotation, parent_name, scale, shape_type, collide_visible):
        super().__init__(name, layer, tag, visible, position, rotation, parent_name, scale, shape_type, collide_visible)

    def on_collision_enter(self, collision):
        Manger.death = True