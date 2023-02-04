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

def drawing_layers(win, lis):
    from main import scene_position_to_view_port_position
    for tile in lis:
        projected_position = scene_position_to_view_port_position( (tile[1][0],tile[1][1]) )  
        win.blit(tile[0], projected_position )
        #win.blit(tile[0], (tile[1][0] - scroll[0], tile[1][1] - scroll[1]))

class Tiledmap:

    current = None

    def __init__(self):

        # --- let us assume for now that there can only be once Tiledmap at a time.
        # store it in "current" for easy access.
        Tiledmap.current = self
        # --

        self.color = (255,255,255)
        self.game_map = get_json('map/swamp.ldtk')["levels"][0]["layerInstances"]
        self.tiles = []
        self.size = get_obj(self.game_map, "Grid_set")["__gridSize"]
        self.cells = dict()

        #   just use this this func to get a 2D list of the images and their positions
        #   the first 2 parameters will be the same for all
        #   the third parameter will the layer's name in LDtk
        #   the fourth parameter is the image's path
        self.TileL1 = get_tile_imgs(self.game_map, self.size, "Tiles", "map/Terrain_and_Props.png")

        self.csvMap = csvMAP = get_obj(self.game_map, "Grid_set")
        x = 0
        y = 0
        cx = 0
        cy = 0
        for block in csvMAP["intGridCsv"]:
            if block != 0:
                self.tiles.append(pygame.Rect(x, y, self.size, self.size))
                self.cells[(cx,cy)] = block
            x += self.size
            cx += 1

            if x == self.size * csvMAP["__cWid"]:
                y += self.size
                x = 0
                cx = 0
                cy += 1

    # old: (remove later)
    def _draw(self, win):
        from main import scene_position_to_view_port_position
        for tile in self.TileL2 + self.TileL1:
            # NOTE/TODO should we check for screen_check here?
            projected_position = scene_position_to_view_port_position( (tile[1][0],tile[1][1]) )  
            win.blit(tile[0], projected_position )



    def get_cell( self, cell_position ):
        #print(sorted(self.cells.keys()))
        return self.cells.get( cell_position, 0)
    
    def draw(self, pl, win):

        pl.draw(win)

        drawing_layers(win, self.TileL1)
