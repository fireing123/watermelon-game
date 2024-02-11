import pygame
from pygame_phyics import DynamicObject
from pygame_phyics import GameObject
from pygame_phyics import Manger
from pygame_phyics import PPM


fruitscale = [0.5, 0.7, 1, 1.2, 1.7, 2.3, 3]
fruitcolor = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

class Fruit(DynamicObject):
    def __init__(self, supe):
        name, tag, position = supe
        super().__init__((((name, 3, tag), True,  position, 0, 'parent'),), fruitscale[int(tag)], "circle", True, 0.5, 1)
        self.color = fruitcolor[tag]
        
    def on_collision_enter(self, collision):
        if collision.tag == self.tag:
            collision.delete()
            if self.tag != 6:
                prefab = Fruit(("fr", self.tag+1, self.location.position),)
                prefab.instantiate()
            Manger.score += self.tag * 5
            self.delete()
            
    def delete(self):
        try:
            super().delete()
        except ValueError as e:
            print(e)
        
    def render(self, surface, camera):
        circle = self.body.fixtures[0].shape
        body = self.body
        position = body.transform * circle.pos * PPM
        position = (position[0] - camera[0], Manger.HEIGHT - position[1] - camera[1])
        pygame.draw.circle(surface, self.color, [int(
            x) for x in position], int(circle.radius * PPM))