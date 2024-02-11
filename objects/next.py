import pygame
from pygame_phyics import GameObject
from pygame_phyics.vector import Vector

class Next(GameObject):
    def __init__(self, supe, color, scale):
        super().__init__(supe)
        self.color = color
        self.scale = scale
        
    def render(self, surface, camera):
        pygame.draw.circle(surface, self.color, self.render_position.xy, self.scale)