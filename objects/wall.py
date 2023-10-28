from pygame_phyics import StaticObject
from pygame_phyics import ImageObject

class Wall(StaticObject):
    def __init__(self, name, tag, position, scale: tuple | float, collide_visible):
        super().__init__(name, tag, True, 3, position, 0, scale, "polygon", collide_visible)

class ImageWall(Wall):
    def __init__(self, name, tag, position, scale: tuple | float, rect):
        super().__init__(name, tag, position, scale, True)
        self.image = ImageObject(self, surface=rect, type="topleft")
        self.image.og_image.fill((255, 255, 255))
        self.rect = self.image.rect
    
    def update(self):
        self.image.update()
        self.rect = self.image.rect
    
    def render(self, surface, camera):
        super().render(surface, camera)
        self.image.render(surface, camera)