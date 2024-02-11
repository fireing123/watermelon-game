from pygame_phyics import StaticObject
from pygame_phyics import GameObject
from pygame_phyics import Manger

class DeathLine(StaticObject):
    def __init__(self, supe):
        super().__init__(*supe)

    def on_collision_enter(self, collision: GameObject):
        Manger.death = True