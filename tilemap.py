import pygame
import json
from spritesheet import Sprite
from main import W, H

def get_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def get_obj(obj, name):
    for o in obj:
        if o["__identifier"] == name:
            return o

def get_tile_imgs(game_map, size, obj, img_name):
    IMGs = []
    allTiles = get_obj(game_map, obj)
    tileimg = Sprite(img_name)

    for tile in allTiles["gridTiles"]:
        IMGs.append([tileimg.get_sprite(tile["src"], size), tile["px"]])

    return IMGs

class Tiledmap:
    def __init__(self):
        self.color = (255,255,255)
        self.game_map = get_json('map/forest.json')["levels"][0]["layerInstances"]
        self.tiles = []
        self.size = get_obj(self.game_map, "Grid_set")["__gridSize"]
        self.scroll = [0, 0]

        #   just use this this func to get a 2D list of the images and their positions
        #   the first 2 parameters will be the same for all
        #   the third parameter will the layer's name in LDtk
        #   the fourth parameter is the image's path
        self.TileL1 = get_tile_imgs(self.game_map, self.size, "TilesExamples", "map/TilesExamples.png")
        self.TileL2 = get_tile_imgs(self.game_map, self.size, "Trees", "map/Trees.png")

        csvMAP = get_obj(self.game_map, "Grid_set")
        x = 0
        y = 0
        for block in csvMAP["intGridCsv"]:
            if block == 1:
                self.tiles.append(pygame.Rect(x, y, self.size, self.size))
            x += self.size

            if x == self.size * csvMAP["__cWid"]:
                y += self.size
                x = 0

    def draw(self, win):
        for tile in self.TileL2:
            win.blit(tile[0], (tile[1][0] - self.scroll[0], tile[1][1] - self.scroll[1]))
        for tile in self.TileL1:
            win.blit(tile[0], (tile[1][0] - self.scroll[0], tile[1][1] - self.scroll[1]))

    def camera(self, pl):
        speed = 10
        self.scroll[0] += (pl.rect.x - self.scroll[0] - W/2) / speed
        self.scroll[1] += (pl.rect.y - self.scroll[1] - H/2) / speed
