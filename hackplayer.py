import pygame
import math

class hackplayer:
    def __init__(self, game, x_tile, y_tile, speed):
        self.game = game
        self.image = pygame.image.load('images/player.png').convert_alpha()
        coords = self.game.main_map.get_xy_from_tile(x_tile, y_tile)
        self.position = [float(coords[0]), float(coords[1])]
        self.speed = speed # should be a whole number
        self.diagonal_speed = math.floor(math.sqrt(math.pow(self.speed, 2) / 2))
        if self.diagonal_speed == 0.0: self.diagonal_speed = 1.0

    def get_tile_position(self):
        return self.game.main_map.get_tile_from_xy(self.position[0], self.position[1])

    def move(self, x_speed, y_speed):
        if self.game.main_map.collide_pixel(self.position[0] + x_speed, self.position[1] + y_speed) \
            and self.moving(x_speed, y_speed):
            if x_speed != 0:
                if x_speed > 0: x_speed -= 1
                else: x_speed += 1
            if y_speed != 0:
                if y_speed > 0: y_speed -= 1
                else: y_speed += 1
            self.move(x_speed, y_speed)
        else:
            self.position[0] += x_speed
            self.position[1] += y_speed

    def moving(self, dx, dy):
        if dx == 0 and dy == 0: return False
        else: return True

    def move_n(self): self.move(0.0, self.speed * -1)
    def move_e(self): self.move(self.speed, 0.0)
    def move_s(self): self.move(0.0, self.speed)
    def move_w(self): self.move(self.speed * -1, 0.0)
    def move_ne(self): self.move(self.diagonal_speed, self.diagonal_speed * -1)
    def move_se(self): self.move(self.diagonal_speed, self.diagonal_speed)
    def move_sw(self): self.move(self.diagonal_speed * -1, self.diagonal_speed)
    def move_nw(self): self.move(self.diagonal_speed * -1, self.diagonal_speed * -1)
