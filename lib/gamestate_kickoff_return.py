import pygame
from .gamestate import GameState
from .camera import Camera

from .mixin_field import FieldMixin

class KickoffReturnGameState(GameState, FieldMixin):
    def __init__(self, player):
        self.player = player
        self.player.gamestate = self
        self.camera = Camera()
        
        self.background = pygame.image.load("img/background.bmp").convert()
        self.field_tile = pygame.image.load("img/field.bmp").convert()
        self.yards_tile = pygame.image.load("img/yards.bmp").convert()
        self.yards_line_1_tile = pygame.image.load("img/yards_line_1.bmp").convert()
        self.yards_line_2_tile = pygame.image.load("img/yards_line_2.bmp").convert()
        self.endzone_tile = pygame.image.load("img/endzone.bmp").convert()
        self.endzone_top_tile = pygame.image.load("img/endzone_top.bmp").convert()

    def update(self, dt):
        self.player.update(dt)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.draw_field(screen)
        self.player.render(screen)
