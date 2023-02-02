import pygame
from main import W, H

class Tiledmap:
    def __init__(self):
        self.w = 10
        self.color = (255,255,255)
        self.tiles = [
            pygame.Rect(0, H-self.w, W, self.w),
            pygame.Rect(0, 0, self.w, H),
            pygame.Rect(W-self.w, 0, self.w, H)]
    
    def draw(self, win):
        for tile in self.tiles:
            pygame.draw.rect(win, self.color, tile)
