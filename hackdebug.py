import pygame

class hackdebug:
    def __init__(self, game):
        self.game = game
        self.render = True
        self.font = pygame.font.SysFont("sans", 12)
        self.color = (255,255,255)
        self.shadow_color = (0,0,0)
        self.values = {}

    def set_value(self, key, value):
        self.values[key] = value

    def text_lines(self):
        lines = ["Debug"]
        for key in self.values:
            lines.append(str(key) + ": " + str(self.values[key]))
        return lines

    def render_it(self):
        self.surface = pygame.Surface([self.game.SCREEN_WIDTH, \
            self.game.SCREEN_HEIGHT], pygame.SRCALPHA, 32)
        text = self.text_lines()
        for line in text:
            self.surface.blit(self.font.render(line, True, self.shadow_color), \
                [11, (15 * (text.index(line) + 1) - 4)])
            self.surface.blit(self.font.render(line, True, self.color), \
                [10, (15 * (text.index(line) + 1) - 5)])
        return self.surface
