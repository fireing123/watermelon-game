from pygame_phyics import StaticObject as _Static
from pygame_phyics import ImageObject

class Wall(_Static):
    def __init__(self, name, position, scale):
        super().__init__(name, 3, 'wall', True,  position, 0, 'parent', scale, "polygon", True)
        self.scale = scale

class ImageWall(Wall):
    def __init__(self, name, position, scale, rect):
        super().__init__(name, position, scale)
        image = ImageObject(self, surface=rect, type="topleft", collide=True)
        image.og_image.fill((255, 255, 255))
        self.components.append(image)