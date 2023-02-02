import pygame
from main import W, H

def get_map(name):
    with open(name, 'r') as f:
        f = f.read()
        return f.split('\n')

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
        for tile in self.tiles:
            pygame.draw.rect(win, self.color, (tile.x - self.scroll[0], tile.y - self.scroll[1], tile.width, tile.height))

    def camera(self, pl):
        speed = 10
        self.scroll[0] += (pl.rect.x - self.scroll[0] - W/2) / speed
        self.scroll[1] += (pl.rect.y - self.scroll[1] - H/2) / speed
