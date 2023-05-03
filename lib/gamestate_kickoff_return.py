import pygame
from .settings import Settings
from .gamestate import GameState
from .camera import Camera

from .mixin_field import FieldMixin

class KickoffReturnGameState(GameState, FieldMixin):
    def __init__(self, player):
        self.player = player
        self.player.gamestate = self
        self.camera = Camera()
        self.camera.set_scroll_bottom()
        
        self.player.py = self.get_yardline_y(48)
        self.player.px = self.get_field_center_x() - (Settings.TILE_WIDTH // 2)
        
        self.background = pygame.image.load("img/background.bmp").convert()
        self.field_tile = pygame.image.load("img/field.bmp").convert()
        self.yards_tile = pygame.image.load("img/yards.bmp").convert()
        self.yards_line_1_tile = pygame.image.load("img/yards_line_1.bmp").convert()
        self.yards_line_2_tile = pygame.image.load("img/yards_line_2.bmp").convert()
        self.endzone_tile = pygame.image.load("img/endzone.bmp").convert()
        self.endzone_top_tile = pygame.image.load("img/endzone_top.bmp").convert()

    def update(self, dt):
        self.player.update(dt)
        
        #scrolling code
        top_margin = 4 * Settings.TILE_HEIGHT;
        bottom_margin = Settings.SCREEN_HEIGHT - (4 * Settings.TILE_HEIGHT)
        
        if self.camera.y > self.camera.MIN_SCROLL:
            amt = top_margin - self.player.py
            if amt > 0:
                self.camera.scroll(-amt)
                self.player.py = top_margin
        
        if self.camera.y < self.camera.MAX_SCROLL:
            amt = bottom_margin - self.player.py
            if amt < 0:
                self.camera.scroll(-amt)
                self.player.py = bottom_margin
            

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.draw_field(screen)
        self.player.render(screen)
