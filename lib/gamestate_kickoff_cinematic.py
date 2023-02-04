import pygame
from .gamestate import GameState

class GamestateKickoffCinematic(GameState):
    def __init__(self, game_config, player):
        self.game_config = game_config
        self.player = player
        self.background = pygame.image.load("img/background.bmp").convert()

        #self.camerax = 
        
    def update(self, dt):
        #self.player.update(dt)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.player.render(screen)

    #def draw_field(self, screen):
        
