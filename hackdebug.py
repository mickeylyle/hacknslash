import pygame

class hackdebug:
    def __init__(self, game):
        self.render = True
        self.font = pygame.font.SysFont("sans", 12)
        self.color = (128, 128, 128)
        self.title = "Debug"
        self.tile_x = "-"
        self.tile_y = "-"
        self.game = game

    def text_lines(self):
        return [self.title,
                "Tile: [" + self.tile_x + ", " + self.tile_y + "] <- this is broken",
                "Player XY: " + str(self.game.player.get_x_position()) + ", " + str(self.game.player.get_y_position()),
                "Camera XY: " + str(self.game.camera_x_position) + ", " + str(self.game.camera_y_position),
                "Screen size: " + str(self.game.SCREEN_WIDTH) + " x " + str(self.game.SCREEN_HEIGHT),
                "iScreen size: " + str(self.game.ISCREEN_WIDTH) + " x " + str(self.game.ISCREEN_HEIGHT),
                "offset size: " + str(self.game.SCREEN_X_OFFSET) + " x " + str(self.game.SCREEN_Y_OFFSET)]

    def render_it(self):
        self.surface = pygame.Surface([self.game.SCREEN_WIDTH, self.game.SCREEN_HEIGHT], pygame.SRCALPHA, 32)
        text = self.text_lines()
        for line in text:
            self.surface.blit(self.font.render(line, True, self.color), [10, (15 * (text.index(line) + 1) - 5)])
        return self.surface
