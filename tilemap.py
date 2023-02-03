import pygame
import json
from main import W, H

def get_map(name):
    with open(name, 'r') as f:
        f = f.read()
        return f.split('\n')

def get_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

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
        self.game_map = get_json('map/forest.json')
        self.tiles = []
        self.size = self.game_map["levels"][0]["layerInstances"][0]["__gridSize"]
        self.scroll = [0, 0]

        self.csvMAP = self.game_map["levels"][0]["layerInstances"][0]

        x = 0
        y = 0
        for block in self.csvMAP["intGridCsv"]:
            if block == 1:
                self.tiles.append(pygame.Rect(x, y, self.size, self.size))
            x += self.size

            if x == self.size * self.csvMAP["__cWid"]:
                y += self.size
                x = 0

    def draw(self, win):
        for tile in self.tiles:
            pygame.draw.rect(win, self.color, (tile.x - self.scroll[0], tile.y - self.scroll[1], tile.width, tile.height))

    def camera(self, pl):
        speed = 10
        self.scroll[0] += (pl.rect.x - self.scroll[0] - W/2) / speed
        self.scroll[1] += (pl.rect.y - self.scroll[1] - H/2) / speed
