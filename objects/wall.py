from pygame_phyics import StaticObject
from pygame_phyics import ImageObject

class Wall(StaticObject):
    def __init__(self, name, position, scale):
        super().__init__((((name, 3, 'wall'), True,  position, 0, 'parent'),), scale, "polygon", True)
        self.scale = scale


class ImageWall(Wall):
    def __init__(self, name, position, scale, rect):
        super().__init__(name, position, scale)
        self.image = ImageObject(self, surface=rect, type="topleft", collide=True)
        self.image.og_image.fill((255, 255, 255))
    
    def update(self):
        self.image.update()
    
    def render(self, surface, camera):
        super().render(surface, camera)
        self.image.render(surface, camera)