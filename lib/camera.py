from .settings import Settings

class Camera(object):
    def __init__(self, startx=0, starty=0):
        self.x = startx
        self.y = starty
        self.w = Settings.FIELD_WIDTH_X
        self.h = Settings.SCREEN_HEIGHT

    def scroll(self, amount, dt):
        self.y += amount * dt
        if self.y < 0:
            self.y = 0
        if self.y > Settings.FIELD_HEIGHT_Y - Settings.SCREEN_HEIGHT:
            self.y = Settings.FIELD_HEIGHT_Y - Settings.SCREEN_HEIGHT
    
