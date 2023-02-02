import pygame
from main import W, H

def get_map(name):
    with open(name, 'r') as f:
        f = f.read()
        return f.split('\n')

def screen_check(rect, scroll):
    if rect.x - scroll[0] < -rect.width:
        return False
    elif rect.x -scroll[0] > W: 
        return False
    elif rect.y - scroll[1] < -rect.width:
        return False
    elif rect.y - scroll[1] > H:
        return False
    return True

class Tiledmap:
    def __init__(self):
        self.color = (255,255,255)
        self.map = get_map("map.txt")
        self.tiles = []
        self.size = 32
        self.scroll = [0, 0]

        x = 0
        y = 0
        for block in self.map:
            for b in block:
                if b == "x":
                    self.tiles.append(pygame.Rect(x, y, self.size, self.size))
                x += self.size
            y += self.size
            x = 0
    
    def draw(self, win):
        from main import scene_position_to_view_port_position
        for tile in self.tiles:


            #if screen_check(tile, self.scroll): # I skip this for now. It doesn't seem to work after refactor.
                                                 # It might even be so we do not need it. the code might take more time to make a screen check
                                                 # for every tile instead of just draw some of them outside. pygame might even ignore outside rects 
            if True: 
                projected_position = scene_position_to_view_port_position( (tile.x,tile.y) )  
                pygame.draw.rect(win, self.color, ( *projected_position, tile.width, tile.height))

    def camera(self, pl):
        speed = 10
        self.scroll[0] += (pl.rect.x - self.scroll[0] - W/2) / speed
        self.scroll[1] += (pl.rect.y - self.scroll[1] - H/2) / speed
