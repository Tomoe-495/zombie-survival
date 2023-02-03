import pygame
from framework import move

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.image = pygame.Surface((20, 30))
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        self.right = False
        self.left = False
        self.speed = 0
        self.max_speed = 2
        self.vel = 0
        self.acc = 0.5
        self.ACC = 0.4
        self.jump_count = 0
        self.jump_limit = 9
        self.jump_power = -4
    
    def draw(self, win, scroll):
        from main import scene_position_to_view_port_position
        projected_position = scene_position_to_view_port_position( self.rect[:2] )  
        win.blit(
            self.image, 
            projected_position
        )

    def jump(self):
        if self.jump_count < self.jump_limit:
            self.vel = self.jump_power
            self.jump_count += 1    
    
    def update(self, movement):
        if self.right:
            if self.speed < self.max_speed:
                self.speed += self.acc
        elif self.left:
            if self.speed > -self.max_speed:
                self.speed -= self.acc
        else:
            if self.speed > 0:
                self.speed -= self.acc
            elif self.speed < 0:
                self.speed += self.acc
        
        movement[0] += self.speed

        #   gravity
        movement[1] += self.vel
        self.vel += self.ACC

    def platformer(self, movement, tiles):
        self.rect, collisions = move(self.rect, movement, tiles)

        if collisions["bottom"]:
            self.vel = 0
            self.jump_count = 0
