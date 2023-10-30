import pygame
from pygame_phyics.object import GameObject
from pygame_phyics.vector import Vector

class Next(GameObject):
    def __init__(self, name: str, tag, visible, layer, color, scale, position):
        super().__init__(name, tag, visible, layer)
        self.color = color
        self.scale = scale
        self.position = Vector(*position)
        
    def render(self, surface, camera):
        pygame.draw.circle(surface, self.color, self.position.xy, self.scale)