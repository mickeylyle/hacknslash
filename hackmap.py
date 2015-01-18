import pygame
from hacktile import hacktile

class hackmap:
    def __init__(self, mapfile):
        self.title = mapfile
        self.tileset = {}
        self.mapset = []
        self.tile_width = 32
        self.tile_height = 16
        self.buffer = 10
        with open("maps/" + mapfile + ".map", "r") as myfile:
            data = myfile.readlines()
        for line in data:
            line = line.replace("\n", "")
            if '=' in line:
                self.tileset[line.split('=')[0]] = hacktile(line.split('=')[1])
            elif ':' not in line and len(line) > 1:
                chars = []
                for c in line.split(','):
                    chars.append(c)
                self.mapset.append(chars)

    def get_tile_from_xy(self, x_pos, y_pos):
        # this is completely broken
        tile_x = y_pos / self.tile_height + x_pos / (2 * self.tile_width)
        tile_y = y_pos / self.tile_height - x_pos / (2 * self.tile_width)
        return [tile_x, tile_y]

    def draw(self):
        map_dimension = len(self.mapset)
        map_surface = pygame.Surface([map_dimension * self.tile_width + self.buffer, \
            map_dimension * self.tile_height + self.buffer], pygame.SRCALPHA, 32)
        i = 0
        j = 0
        while i != map_dimension and j != map_dimension:
            y = (j * self.tile_height / 2) + (i * self.tile_width / 4) + 10
            x = (i * self.tile_width / 2) - (j * self.tile_width / 2) + ((map_dimension-1) * self.tile_width / 2) + 10
            if self.tileset[self.mapset[j][i]].properties['base'] != "none":
                for key in self.tileset:
                    if self.tileset[key].name == \
                        self.tileset[self.mapset[j][i]].properties['base']:
                        map_surface.blit(self.tileset[key].image, [x, y])
            y = y - self.tileset[self.mapset[j][i]].image.get_height() + self.tile_height
            x = x - self.tileset[self.mapset[j][i]].image.get_width() / 2 + self.tile_width / 2
            map_surface.blit(self.tileset[self.mapset[j][i]].image, [x, y])
            if j == map_dimension - 1:
                j = i + 1
                i = map_dimension - 1
            elif i == 0:
                i = j + 1
                j = 0
            else:
                i -= 1
                j += 1
        return map_surface
