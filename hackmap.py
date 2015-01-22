import pygame
import math
from hacktile import hacktile

class hackmap:
    def __init__(self, game, mapfile):
        self.game = game
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
        self.map_dimension = len(self.mapset)
        
        # this is used by get_tile_from_xy()
        self.iso_plane_dimension = math.sqrt(2 * (math.pow(((self.map_dimension * self.tile_width) / 2),2)))

    def get_xy_from_tile(self, tile_x, tile_y):
        x_pos = ((tile_x + self.map_dimension - tile_y - 1) * self.tile_width / 2) + self.tile_width / 2
        y_pos = ((tile_y + tile_x) * self.tile_height / 2) + self.tile_height / 2
        return [x_pos, y_pos]

    def get_tile_from_xy(self, x_pos, y_pos):
        # figure out the distances when they're at angles - scale the y value so it's useful
        x_leg = math.sqrt((math.pow(x_pos, 2)) / 2)
        if x_pos < 0: x_leg *= -1
        y_leg = math.sqrt((math.pow(y_pos * 2, 2)) / 2)
        if y_pos < 0: y_leg *= -1
        # combine those distances and factor in the different origin
        iso_x = y_leg + x_leg - (self.iso_plane_dimension / 2)
        iso_y = y_leg - x_leg + (self.iso_plane_dimension / 2)
        # use the ratio of the iso coord to the iso size to get the tile
        tile_x = int(math.floor((iso_x / self.iso_plane_dimension) * self.map_dimension))
        tile_y = int(math.floor((iso_y / self.iso_plane_dimension) * self.map_dimension))
        return [tile_x, tile_y]

    def get_tile_properties(self, tile_x, tile_y):
        return self.tileset[self.mapset[tile_y][tile_x]].properties
    
    def collide_pixel(self, x, y):
        tile = self.get_tile_from_xy(x, y)
        if tile[0] < 0 or tile[0] > self.map_dimension - 1 or tile[1] < 0 or tile[1] > self.map_dimension - 1:
            return True
        return not self.get_tile_properties(tile[0], tile[1])["walkable"]

    def draw(self):
        map_surface = pygame.Surface([self.map_dimension * self.tile_width + self.buffer, \
            self.map_dimension * self.tile_height + self.buffer], pygame.SRCALPHA, 32)
        i = 0
        j = 0
        while i != self.map_dimension and j != self.map_dimension:
            y = (j * self.tile_height / 2) + (i * self.tile_width / 4) + 10
            x = (i * self.tile_width / 2) - (j * self.tile_width / 2) + \
                ((self.map_dimension-1) * self.tile_width / 2) + 10
            if self.tileset[self.mapset[j][i]].properties['base'] != "none":
                for key in self.tileset:
                    if self.tileset[key].properties["name"] == \
                        self.tileset[self.mapset[j][i]].properties['base']:
                        map_surface.blit(self.tileset[key].image, [x, y])
            y = y - self.tileset[self.mapset[j][i]].image.get_height() + self.tile_height
            x = x - self.tileset[self.mapset[j][i]].image.get_width() / 2 + self.tile_width / 2
            map_surface.blit(self.tileset[self.mapset[j][i]].image, [x, y])
            if j == self.map_dimension - 1:
                j = i + 1
                i = self.map_dimension - 1
            elif i == 0:
                i = j + 1
                j = 0
            else:
                i -= 1
                j += 1
        return map_surface
