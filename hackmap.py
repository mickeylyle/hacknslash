import pygame
from hacktile import hacktile

class hackmap:
    def __init__(self, mapfile):
        self.title = mapfile
        self.tileset = []
        self.mapset = []
        with open("maps/" + mapfile + ".map", "r") as myfile:
            data = myfile.readlines()
        for line in data:
            line = line.replace("\n", "")
            if '=' in line:
                self.tileset.append(hacktile(line.split('=')[1]))
            elif ':' not in line and len(line) > 1:
                chars = []
                for c in line:
                    chars.append(int(c))
                self.mapset.append(chars)

    def draw(self):
        tile_width = 32
        tile_height = 16
        map_dimension = len(self.mapset)
        map_surface = pygame.Surface([map_dimension * tile_width, \
            map_dimension * tile_height], pygame.SRCALPHA, 32)
        for i in range(0, map_dimension):
            for j in range (0, map_dimension):
                x = ((map_dimension -1 - j) * tile_width / 2) + (i * tile_width / 2)
                y = (i * tile_height / 2) - ((map_dimension - 1 - j) * tile_height / 2) + \
                    (map_dimension * tile_height / 2 - tile_height / 2)
                map_surface.blit(self.tileset[self.mapset[i][j]].nw, [x, y])
                map_surface.blit(self.tileset[self.mapset[i][j]].ne, [x + tile_width / 2, y])
                map_surface.blit(self.tileset[self.mapset[i][j]].sw, [x, y + tile_height / 2])
                map_surface.blit(self.tileset[self.mapset[i][j]].se, [x + tile_width / 2, y + tile_height / 2])
        return map_surface
