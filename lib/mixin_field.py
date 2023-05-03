import pygame
from .settings import Settings

class FieldMixin(object):
    """
    FieldMixin: a mixin for field related functionality for game states
    
    The field yarlines are represented as being from -60 (the top of the
    top end zone) to 59 (the bottom of the bottom endzone), which is
    120 yards. 


    Implenting class needs:
    - self.field_tile
    - self.yards_tile
    - self.yards_line_1_tile
    - self.yards_line_2_tile
    - self.endzone_tile
    - self.camera
    """
    
    def get_yardline_y(self, yl):
        """
        converts the yardline, (-60[top] to 59[bottom] and, with the camera, finds the proper y coord
        """
        
        total_y = (yl + 60) * (Settings.TILE_HEIGHT // Settings.YARDS_PER_TILE)
        return total_y - self.camera.y
        
    def get_field_center_x(self):
        return (Settings.FIELD_WIDTH_X // 2) + Settings.FIELD_X_OFFSET
        
    
    def get_row_yardlines(self, tile_y):
        """
        This method returns the yardlines for a given tile row.  So,
        starting at -60 (the top), the yardline will be the rows of
        tiles multiplied by how many yards per row.

        Returns a list of yardlines, where rv[0] is the top most 
        yard line in the row, and rv[-1] is the lower most yardline.
        """
        yl = -60 + Settings.YARDS_PER_TILE * tile_y
        return [yl + x for x in range(0, Settings.YARDS_PER_TILE)]

    def draw_field(self, screen):
        row = 0 
        for yy in range(-self.camera.y, Settings.FIELD_HEIGHT_Y, Settings.TILE_HEIGHT ):
            yardlines = self.get_row_yardlines(row)
            for xx in range(Settings.FIELD_X_OFFSET, Settings.FIELD_WIDTH_X, Settings.TILE_WIDTH): 
                if yardlines[0] < -50:
                    screen.blit(self.endzone_tile, (xx,yy))
                elif yardlines[0] == 50:
                    screen.blit(self.endzone_top_tile, (xx,yy))
                elif yardlines[-1] > 50:
                    screen.blit(self.endzone_tile, (xx,yy))
                elif xx / Settings.TILE_WIDTH == Settings.LEFT_HASH_TILE_X:
                    screen.blit(self.yards_tile, (xx,yy))
                elif xx / Settings.TILE_WIDTH == Settings.RIGHT_HASH_TILE_X: 
                    screen.blit(self.yards_tile, (xx,yy))
                elif yardlines[0] % 5 == 0:
                    screen.blit(self.yards_line_2_tile, (xx,yy))
                elif yardlines[-1] % 5 == 0:
                    screen.blit(self.yards_line_1_tile, (xx,yy))
                else:
                    screen.blit(self.field_tile, (xx,yy))
            row += 1
