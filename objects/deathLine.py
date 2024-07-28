from pygame_phyics import StaticObject as _Static
from pygame_phyics import Manger

class DeathLine(_Static):
    def __init__(self, name, layer, tag, visible, position, rotation, parent_name, scale, shape_type):
        super().__init__(name, layer, tag, visible, position, rotation, parent_name, scale, shape_type, True)

    def on_collision_enter(self, collision):
        pass
        #Manger.death = True