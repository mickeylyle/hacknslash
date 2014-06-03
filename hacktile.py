import pygame

class hacktile:
    def __init__(self, new_tile):
        self.name = new_tile
        # load images
        self.image = pygame.image.load('images/tiles/' + new_tile + '.png').convert_alpha()
        # load info
        self.properties = {}
        with open("tiles/" + new_tile + ".tile", "r") as myfile:
            data = myfile.readlines()
        for line in data:
            line = line.replace("\n", "").split()
            if line[1] == "True": line[1] = True
            elif line[1] == "False": line[1] = False
            self.properties[line[0]] = line[1]
