from pygame_phyics import StaticObject as _Static
from pygame_phyics import Manger

class DeathLine(_Static):
    def __init__(self, supe):
        super().__init__(*supe)

    def on_collision_enter(self, collision):
        Manger.death = True