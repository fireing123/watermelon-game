import pygame
from pygame_phyics import DynamicObject
from pygame_phyics import GameObject
from pygame_phyics import Manger
from pygame_phyics import PPM


fruitscale = [0.5, 1, 2, 2.5, 3, 3.5, 4]
fruitcolor = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

class Fruit(DynamicObject):
    def __init__(self, name, tag, visible, position, collid_visible):
        super().__init__(name, tag, visible, 3, position, 0, fruitscale[tag], "circle", collid_visible, 1, 0.3)
        self.color = fruitcolor[tag]
        
    def on_collision_enter(self, collision):
        if collision.tag == self.tag:
            collision.delete()
            if self.tag != 6:
                prefab = Fruit("fr", self.tag+1, True, self.position, True)
                GameObject.instantiate(prefab)
            Manger.score += self.tag * 5
            self.delete()
            
        
    def render(self, surface, camera):
        circle = self.body.fixtures[0].shape
        body = self.body
        position = body.transform * circle.pos * PPM
        position = (position[0] - camera[0], Manger.HEIGHT - position[1] - camera[1])
        pygame.draw.circle(surface, self.color, [int(
            x) for x in position], int(circle.radius * PPM), 1)