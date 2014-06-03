import pygame
from hacktile import hacktile

class hackmap:
    def __init__(self, mapfile):
        self.title = mapfile
        self.tileset = {}
        self.mapset = []
        with open("maps/" + mapfile + ".map", "r") as myfile:
            data = myfile.readlines()
        for line in data:
            line = line.replace("\n", "")
            if '=' in line:
                self.tileset[line.split('=')[0]] = hacktile(line.split('=')[1])
            elif ':' not in line and len(line) > 1:
                chars = []
                for c in line:
                    chars.append(c)
                self.mapset.append(chars)

    def draw(self):
        tile_width = 32
        tile_height = 16
        map_dimension = len(self.mapset)
        map_surface = pygame.Surface([map_dimension * tile_width, \
            map_dimension * tile_height], pygame.SRCALPHA, 32)
        for i in range(0, map_dimension):
            for j in range (0, map_dimension):

                # draw tile
                x = (j * tile_width / 2) + (i * tile_width / 2)
                y = (i * tile_height / 2) - (j * tile_height / 2) + \
                    (map_dimension * tile_height / 2 - tile_height / 2)
                if self.tileset[self.mapset[i][j]].properties['base'] != "none":
                    for key in self.tileset:
                        if self.tileset[key].name == self.tileset[self.mapset[i][j]].properties['base']:
                            map_surface.blit(self.tileset[key].image, [x, y])
                y = y - self.tileset[self.mapset[i][j]].image.get_height() + tile_height
                x = x - self.tileset[self.mapset[i][j]].image.get_width() / 2 + tile_width / 2
                map_surface.blit(self.tileset[self.mapset[i][j]].image, [x, y])
        return map_surface
