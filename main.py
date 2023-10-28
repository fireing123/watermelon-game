import pygame
from pygame_phyics import *
from pygame_phyics.input import Input
from objects.fruit import Fruit
import random
Game.init((400, 800), "WaterMelon Game")

Game.import_classes("objects/")

fruitscale = [0.5, 1, 2, 3]
fruitcolor = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
@game.world("map.json")
def main():
    score_text : object.Text = Manger.scene.get_objects("score")[0]
    def start(cls): 
        Manger.score = 0
        score_text.text = "score : 0"
    def event(cls, event):
        pass
    def update(cls):
        score_text.text = f"score : {Manger.score}"
        Manger.screen.fill((0, 0, 0))
        if Input.get_mouse_down(0):
            x = mouse.get_pos()[0]
            if 60 < x < 340:
                pos = x, 750
                furit_tag = random.randint(0, 3)
                prefab = Fruit("f", furit_tag, True, pos, True)
                GameObject.instantiate(prefab)
    return start, event, update

main()