from .settings import Settings

class Camera(object):
    def __init__(self, startx=0, starty=0):
        self.x = startx
        self.y = starty
        self.w = Settings.FIELD_WIDTH_X
        self.h = Settings.SCREEN_HEIGHT
        
        self.MAX_SCROLL = Settings.FIELD_HEIGHT_Y - Settings.SCREEN_HEIGHT
        self.MIN_SCROLL = 0
        
    def set_scroll_bottom(self):
        self.y = Settings.FIELD_HEIGHT_Y - Settings.SCREEN_HEIGHT
        
    def set_scroll_top(self):
        self.y = 0

    def scroll(self, amount):
        self.y += amount
        self.y = self.y
        if self.y < self.MIN_SCROLL:
            self.y = self.MIN_SCROLL
        if self.y > self.MAX_SCROLL:
            self.y = self.MAX_SCROLL
    
