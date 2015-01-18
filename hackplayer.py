import pygame

class hackplayer:
    def __init__(self, world):
        self.world = world
        self.image = pygame.image.load('images/player.png').convert_alpha()

    def get_x_position(self):
        return (self.world.ISCREEN_WIDTH / 2) + self.world.camera_x_position

    def get_y_position(self):
        return (self.world.ISCREEN_HEIGHT / 2) + self.world.camera_y_position

    def get_tile_position(self):
        return self.world.main_map.get_tile_from_xy(self.get_x_position(), self.get_y_position())
