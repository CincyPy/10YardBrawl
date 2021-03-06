import pygame
from .settings import Settings

class FieldMixin(object):
    """
    FieldMixin: a mixin for field related functionality for game states
    Implenting class needs:
    - self.field_tile
    - self.yards_tile
    - self.yards_line_1_tile
    - self.yards_line_2_tile
    - self.endzone_tile
    - self.camera
    """
    def get_row_yardlines(self, tile_y):
        yl1 = -60 + Settings.YARDS_PER_TILE * tile_y
        yl2 = yl1 + 1
        return (yl1, yl2)

    def draw_field(self, screen):
        row = 0
        for yy in range(-self.camera.y, Settings.FIELD_HEIGHT_Y, Settings.TILE_HEIGHT ):
            yardlines = self.get_row_yardlines(row)
            for xx in range(Settings.FIELD_X_OFFSET, Settings.FIELD_WIDTH_X, Settings.TILE_WIDTH): 
                if yardlines[0] < -50:
                    screen.blit(self.endzone_tile, (xx,yy))
                elif yardlines[0] == 50:
                    screen.blit(self.endzone_top_tile, (xx,yy))
                elif yardlines[1] > 50:
                    screen.blit(self.endzone_tile, (xx,yy))
                elif xx / Settings.TILE_WIDTH == Settings.LEFT_HASH_TILE_X:
                    screen.blit(self.yards_tile, (xx,yy))
                elif xx/ Settings.TILE_WIDTH == Settings.RIGHT_HASH_TILE_X: 
                    screen.blit(self.yards_tile, (xx,yy))
                elif yardlines[0] % 5 == 0:
                    screen.blit(self.yards_line_2_tile, (xx,yy))
                elif yardlines[1] % 5 == 0:
                    screen.blit(self.yards_line_1_tile, (xx,yy))
                else:
                    screen.blit(self.field_tile, (xx,yy))
            row += 1
