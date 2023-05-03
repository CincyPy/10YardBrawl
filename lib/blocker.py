import pygame

from .settings import Settings

class Blocker(object):
    
    def __init__(self, x, y):
        self.px = x
        self.py = y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        
        self.image = pygame.image.load("img/blocker.bmp").converto()
        
     def update(self, dt):
         pass
     
     def render(self, screen):
         screen.blit(self.image, (self.px, self.py))