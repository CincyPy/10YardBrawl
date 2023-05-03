import pygame

from .settings import Settings

class Player(object):

    def __init__(self):
        self.px = 400
        self.py = 300
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0

        self.image = pygame.image.load("img/player.bmp").convert()
        
        self.gamestate = None
    
    def get_input(self, dt):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.ay = -.1
        if keystate[pygame.K_DOWN]:
            self.ay = .1
        if keystate[pygame.K_LEFT]:
            self.ax = -.1
        if keystate[pygame.K_RIGHT]:
            self.ax = .1
            
    def update(self, dt):

        self.ax = 0
        self.ay = 0
        
        self.get_input(dt)
        
        if self.vx > 0:
            self.vx -= Settings.FRICTION
        elif self.vx < 0:
            self.vx += Settings.FRICTION
     
        self.vx += self.ax
        if self.vx > 3:
            self.vx = 3
        if self.vx < -3:
            self.vx = -3

        if self.vy > 0:
            self.vy -= Settings.FRICTION
        elif self.vy < 0:
            self.vy += Settings.FRICTION
        
        self.vy += self.ay
        if self.vy > 3:
            self.vy = 3
        if self.vy < -3:
            self.vy = -3

        if self.vx > -.01 and self.vx < .01:
            self.vx = 0
            self.ax = 0
        if self.vy > -.01 and self.vy < .01:
            self.vy = 0
            self.ay = 0
            
        self.px += self.vx * dt
        self.py += self.vy * dt
        
        self.px = int(self.px)
        self.py = int(self.py)
        
        if self.py < 0:
            self.py = 0
        if self.py > Settings.SCREEN_HEIGHT - Settings.TILE_HEIGHT:
            self.py = Settings.SCREEN_HEIGHT - Settings.TILE_HEIGHT

    def render(self, screen):
        screen.blit(self.image, (self.px, self.py))

