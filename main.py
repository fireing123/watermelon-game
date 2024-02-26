import pygame
from pygame_phyics import game, mouse, Game, Manger
from pygame_phyics.input import Input
from objects.fruit import Fruit, fruitcolor, fruitscale
from objects.next import Next
from pygame_phyics.save import save
import random
Game.init((400, 800), "WaterMelon Game")

Game.import_objects("objects/", debug='detail')

furit_tag = random.randint(0, 3)
fruitscale = [0.5, 1, 2, 3]
fruitcolor = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
@game.world("map.json")
def main():
    score_text : object.Text = Manger.scene.get_objects("score")[0]
    next : Next = Manger.scene.get_objects("next")[0]
    
    def start(cls): 
        score_text.text = "score : 0"
        
    def event(cls, event):
        pass
    
    def update(cls):
        
        if Manger.death == True:
            Game.stop()
        
        global furit_tag
        score_text.text = f"score : {Manger.score}"
        Manger.screen.fill((0, 0, 0))
        if Input.get_mouse_down(0) or Input.get_key_down(pygame.K_k) or Input.get_key_down(pygame.K_g):
            x = mouse.get_pos()[0]
            if 60 < x < 340:
                pos = x, 750
                prefab = Fruit("f", furit_tag, pos)
                furit_tag = random.randint(0, 3)
                next.color = fruitcolor[furit_tag]
                next.scale = fruitscale[furit_tag] * 10
                prefab.set_parent()
                prefab.set_location()
                prefab.instantiate()
        if Input.get_key_down(pygame.K_q):
            save('./save.json', score=Manger.score)
    return start, event, update

main()