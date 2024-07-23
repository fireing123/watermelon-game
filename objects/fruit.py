import pygame
from pygame_phyics import DynamicObject as _DyObj
from pygame_phyics import Manger
from pygame_phyics import PPM

fruitscale = [0.5, 1, 2, 3, 4, 6, 7]
fruitcolor = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 180), (255, 0, 132), (0, 255, 132)]

class Fruit(_DyObj):
    def __init__(self, name, tag, position,):
        super().__init__(name, 3, tag, True,  position, 0, 'parent', fruitscale[int(tag)], "circle", True, 0.5, 1)
        self.color = fruitcolor[tag]
        
    def on_collision_enter(self, collision):
        if collision.gameobject.tag == self.tag:
            collision.gameobject.delete()
            if self.tag != 6:
                prefab = Fruit("fr", self.tag+1, self.location.position)
                prefab.set_parent()
                prefab.set_location()
                prefab.instantiate()
            Manger.score += self.tag * 5
            self.delete()
            
    def delete(self):
        try:
            super().delete()
        except ValueError as e:
            pass
        
    def render(self, surface, camera):
        try:
            circle = self.body.fixtures[0].shape
            body = self.body
            position = body.transform * circle.pos * PPM
            position = (position[0] - camera.location.position.x, Manger.HEIGHT - position[1] - camera.location.position.y)
            pygame.draw.circle(surface, self.color, [int(
                x) for x in position], int(circle.radius * PPM))
        except:
            try:
                self.delete()
            except:
                pass